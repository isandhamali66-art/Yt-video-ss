"""
Free YouTube Video Downloader - Flask + yt-dlp
Run:  pip install -r requirements.txt && python app.py
"""
import os
import re
import uuid
import shutil
import threading
import time

from flask import Flask, request, jsonify, send_file, render_template, after_this_request
import yt_dlp

try:
    import imageio_ffmpeg
    FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:
    FFMPEG = shutil.which("ffmpeg")

app = Flask(__name__)
DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

YT_REGEX = re.compile(r"^(https?://)?(www\.|m\.|music\.)?(youtube\.com|youtu\.be)/.+", re.I)


def base_opts():
    opts = {"quiet": True, "no_warnings": True, "noplaylist": True}
    if FFMPEG:
        opts["ffmpeg_location"] = FFMPEG
    return opts


def cleanup_old_files(max_age=1800):
    """Delete downloaded files older than max_age seconds."""
    while True:
        now = time.time()
        for name in os.listdir(DOWNLOAD_DIR):
            path = os.path.join(DOWNLOAD_DIR, name)
            try:
                if now - os.path.getmtime(path) > max_age:
                    shutil.rmtree(path, ignore_errors=True) if os.path.isdir(path) else os.remove(path)
            except OSError:
                pass
        time.sleep(300)


threading.Thread(target=cleanup_old_files, daemon=True).start()


APP_DIR = os.path.dirname(os.path.abspath(__file__))

# ---- Monetag / ads settings (set these as Environment Variables on Render) ----
#   MONETAG_META : full verification meta tag, e.g. <meta name="monetag" content="abc123">
#   AD_CODE      : the ad <script> code Monetag gives you
def ad_settings():
    return {
        "monetag_meta": os.environ.get("MONETAG_META", ""),
        "ad_code": os.environ.get("AD_CODE", ""),
    }


@app.route("/")
def index():
    return render_template("index.html", **ad_settings())


@app.route("/sw.js")
def monetag_sw():
    """Serves Monetag's sw.js verification file if you put it in the project folder."""
    path = os.path.join(APP_DIR, "sw.js")
    if os.path.exists(path):
        return send_file(path, mimetype="application/javascript")
    return "Not found", 404


@app.post("/api/info")
def info():
    url = (request.json or {}).get("url", "").strip()
    if not YT_REGEX.match(url):
        return jsonify(error="Please enter a valid YouTube link."), 400
    try:
        with yt_dlp.YoutubeDL(base_opts()) as ydl:
            data = ydl.extract_info(url, download=False)
    except Exception as e:
        return jsonify(error=f"Could not fetch video: {str(e)[:300]}"), 400

    heights = sorted(
        {f.get("height") for f in data.get("formats", []) if f.get("height") and f.get("vcodec") != "none"},
        reverse=True,
    )
    heights = [h for h in heights if h in (2160, 1440, 1080, 720, 480, 360, 240, 144)]
    if not FFMPEG:  # without ffmpeg only progressive formats (usually 360p) can be merged
        heights = [h for h in heights if h <= 360][:1] or [360]

    return jsonify(
        title=data.get("title"),
        thumbnail=data.get("thumbnail"),
        duration=data.get("duration_string") or data.get("duration"),
        channel=data.get("uploader"),
        views=data.get("view_count"),
        qualities=heights,
        audio=bool(FFMPEG),
    )


@app.get("/api/download")
def download():
    url = request.args.get("url", "").strip()
    kind = request.args.get("type", "video")  # video | audio
    quality = request.args.get("quality", "720")
    if not YT_REGEX.match(url):
        return jsonify(error="Invalid YouTube link."), 400

    job_dir = os.path.join(DOWNLOAD_DIR, uuid.uuid4().hex)
    os.makedirs(job_dir)
    opts = base_opts()
    opts["outtmpl"] = os.path.join(job_dir, "%(title).150B.%(ext)s")
    opts["restrictfilenames"] = False

    if kind == "audio":
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}]
    else:
        q = int(quality) if quality.isdigit() else 720
        if FFMPEG:
            opts["format"] = (
                f"bestvideo[height<={q}][ext=mp4]+bestaudio[ext=m4a]/"
                f"bestvideo[height<={q}]+bestaudio/best[height<={q}]/best"
            )
            opts["merge_output_format"] = "mp4"
        else:
            opts["format"] = "best[ext=mp4][acodec!=none][vcodec!=none]/best"

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.extract_info(url, download=True)
    except Exception as e:
        shutil.rmtree(job_dir, ignore_errors=True)
        return jsonify(error=f"Download failed: {str(e)[:300]}"), 500

    files = os.listdir(job_dir)
    if not files:
        return jsonify(error="Download failed."), 500
    path = os.path.join(job_dir, files[0])

    @after_this_request
    def _cleanup(resp):
        threading.Timer(60, lambda: shutil.rmtree(job_dir, ignore_errors=True)).start()
        return resp

    return send_file(path, as_attachment=True, download_name=files[0])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, threaded=True)
