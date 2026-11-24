# FreeTube Saver – Free YouTube Video Downloader

A simple website for downloading YouTube videos as **MP4** (144p–4K) or **MP3**.
Built with Flask + [yt-dlp](https://github.com/yt-dlp/yt-dlp). FFmpeg is included via `imageio-ffmpeg`, so you don't need to install anything else.

## Run locally
```bash
pip install -r requirements.txt
python app.py
# open http://localhost:5000
```

## Deploy for free (Render.com example)
1. Push this folder to a GitHub repo.
2. On render.com → New → Web Service → connect the repo.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn -w 2 --threads 4 --timeout 600 -b 0.0.0.0:$PORT app:app`

Railway, Fly.io, and Koyeb also work.

## Tips
- YouTube changes often, so keep yt-dlp updated: `pip install -U yt-dlp`
- YouTube sometimes blocks cloud-server IPs ("Sign in to confirm you're not a bot").
  If that happens, add a `cookiefile` to the yt-dlp options in `base_opts()` or use a residential proxy.
- Downloaded files are deleted automatically (1 minute after they're sent, or after 30 min at most).

## Structure
```
app.py               # Flask backend (info + download API)
templates/index.html # Frontend (single page, no external assets)
requirements.txt
```

⚠️ Only download content you own or have permission to download. Respect copyright and YouTube's Terms of Service.
