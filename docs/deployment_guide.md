# 🚀 Deployment Guide

## Option A — Streamlit Community Cloud (free, recommended)

1. Push the project to GitHub (see `github_push_guide.md`).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **New app**.
4. Select your `EchoSphere` repository, the `main` branch, and set the
   main file path to `app.py`.
5. Click **Deploy**. Streamlit Cloud will install `requirements.txt`
   automatically and give you a public URL like:
   `https://<your-app-name>.streamlit.app`

### Notes for Streamlit Cloud

- The `data/history.json` file will reset whenever the app redeploys or
  restarts, since Community Cloud's filesystem is ephemeral. For persistent
  history across restarts, consider swapping `core/processor.py`'s storage
  functions for a database (e.g. SQLite via a mounted volume, or a hosted
  service like Supabase/Firebase).
- Add any secrets (API keys, etc.) via the app's **Settings → Secrets** panel
  rather than committing them to the repo.

## Option B — Docker

Create a `Dockerfile` in the project root:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:

```bash
docker build -t echosphere .
docker run -p 8501:8501 echosphere
```

## Option C — Any VM / VPS

```bash
pip install -r requirements.txt
streamlit run app.py --server.port 80 --server.address 0.0.0.0
```

Put a reverse proxy (e.g. Nginx) in front for TLS termination if serving
over HTTPS.
