# Running the Application

## Combined Application (Recommended)

The web application and API have been **combined into a single application** that runs on port 5555.

```bash
python src/web_app/app.py
```

This single command starts both:
- **Web Interface:** http://localhost:5555
- **API Endpoints:** http://localhost:5555/api/*

### Available Endpoints

| Endpoint | Type | Description |
|----------|------|-------------|
| http://localhost:5555 | Web UI | Interactive web interface with manual controls |
| http://localhost:5555/health | JSON | Health check endpoint |
| http://localhost:5555/api/number | JSON | Current number with metadata |
| http://localhost:5555/api/status | JSON | API status and uptime |
| http://localhost:5555/api/sequence | JSON | Sequence configuration |

### Features

- **Unified Port:** Everything accessible on port 5555
- **CORS Enabled:** API supports cross-origin requests
- **Server Sync Mode:** Web UI can optionally sync with server-side number rotation
- **Network Access:** Available at `http://<your-ip>:5555` from other devices

See [Quick Start Guide](../getting-started/quickstart.md) for installation details.
