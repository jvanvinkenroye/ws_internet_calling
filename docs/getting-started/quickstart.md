# Quick Start Guide

Get up and running with the Nummernsender project in less than 10 minutes!

## Prerequisites Check

Before starting, ensure you have:

- ✅ Python 3.12 or later installed
- ✅ `uv` package manager installed (or pip)
- ✅ Git installed (optional)
- ✅ Terminal/Command Prompt access
- ✅ Web browser

Check Python version:
```bash
python --version
# Should show Python 3.12.x or later
```

## Step 1: Get the Project

### Option A: Clone Repository
```bash
git clone <repository-url>
cd ws_internet_calling
```

### Option B: Download ZIP
1. Download project ZIP
2. Extract to desired location
3. Open terminal in project directory

## Step 2: Set Up Python Environment

### Create Virtual Environment
```bash
# Create venv with uv (recommended)
uv venv --seed

# Or with standard Python
python -m venv .venv
```

### Activate Virtual Environment

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

You should see `(.venv)` in your terminal prompt.

## Step 3: Install Dependencies

```bash
# Using uv (fast)
uv add flask flask-cors requests mkdocs mkdocs-material

# Or using pip
pip install flask flask-cors requests mkdocs mkdocs-material
```

## Step 4: Run the Web Application

### Start the Web App

**Terminal 1:**
```bash
# Make sure venv is activated
cd src/web_app
python app.py
```

You should see:
```
 * Running on http://0.0.0.0:5000
```

**Test it:**
- Open browser to [http://localhost:5000](http://localhost:5000)
- You should see the Number Transmitter interface
- Click "Start" to begin number rotation

### Start the API (Optional)

**Terminal 2:**
```bash
# Make sure venv is activated
cd src/api
python app.py
```

You should see:
```
 * Running on http://0.0.0.0:5001
```

**Test it:**
- Open browser to [http://localhost:5001/api/number](http://localhost:5001/api/number)
- You should see JSON response with current number

## Step 5: Test the API Client

**Terminal 3:**
```bash
# Make sure venv is activated
cd examples
python api_client.py --current
```

You should see:
```
Current Number: 5
Timestamp: 2025-01-15T10:30:45.123456
Total Cycles: 12345
```

### Monitor the API

```bash
# Monitor for 30 seconds
python api_client.py --monitor --duration 30

# Get API status
python api_client.py --status
```

## Step 6: View Documentation

```bash
# From project root
mkdocs serve
```

Open [http://localhost:8000](http://localhost:8000) in your browser to view the full documentation.

## Common Quick Start Issues

### Port Already in Use

**Error:**
```
OSError: [Errno 48] Address already in use
```

**Solution:**
```bash
# Find and kill process on port 5000
# macOS/Linux
lsof -ti:5000 | xargs kill -9

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Or use different port
# Edit app.py and change:
app.run(port=5002)  # Use any available port
```

### Module Not Found

**Error:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
# Make sure venv is activated (you should see (.venv) in prompt)
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Install dependencies again
uv add flask flask-cors
```

### Permission Denied

**Error:**
```
PermissionError: [Errno 13] Permission denied
```

**Solution:**
```bash
# Don't use sudo/admin
# Make sure you're in the project directory
# Recreate venv if needed
rm -rf .venv
uv venv --seed
source .venv/bin/activate
uv add flask flask-cors
```

## What's Next?

### For Web Development
- [Web Application Documentation](../web-app/web-app.md)
- [API Documentation](../web-app/api.md)
- Explore the code in `src/web_app/` and `src/api/`

### For IoT/Pico Development
- [Install Thonny IDE](../guides/thonny_installation.md)
- [Flash Raspberry Pi Pico](../guides/pico_flashing.md)
- [Try Pico Examples](../pico/introduction.md)

### For Learning
- [Project Overview](overview.md) - Understand the architecture
- [Troubleshooting Guide](../troubleshooting/common_issues.md) - Solve common problems
- [Reference](../reference/api.md) - API reference and examples

## Testing Checklist

Verify everything works:

- [ ] Web app runs on http://localhost:5000
- [ ] Number display shows and rotates
- [ ] Start/Stop/Reset buttons work
- [ ] API runs on http://localhost:5001
- [ ] API returns JSON at http://localhost:5001/api/number
- [ ] API client can fetch current number
- [ ] MkDocs documentation serves on http://localhost:8000

## Project Structure Quick Reference

```
ws_internet_calling/
├── src/
│   ├── web_app/          # Flask web application
│   │   ├── app.py        # Main Flask app
│   │   ├── templates/    # HTML templates
│   │   └── static/       # CSS, JS, images
│   ├── api/              # REST API
│   │   └── app.py        # API endpoints
│   └── pico_scripts/     # Raspberry Pi Pico programs
├── examples/
│   └── api_client.py     # API client example
├── docs/                 # MkDocs documentation
├── .venv/                # Virtual environment (created by you)
├── mkdocs.yml           # Documentation config
└── pyproject.toml       # Python project config
```

## Getting Help

If you run into issues:

1. **Check Error Messages** - Read them carefully
2. **Verify Virtual Environment** - Make sure it's activated
3. **Check Dependencies** - Ensure all packages installed
4. **Review Logs** - Look at terminal output
5. **Consult Documentation**:
   - [Troubleshooting Guide](../troubleshooting/common_issues.md)
   - [Installation Guides](../guides/thonny_installation.md)
   - [FAQ](../troubleshooting/faq.md)

## Quick Commands Reference

```bash
# Activate venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Run web app
python src/web_app/app.py

# Run API
python src/api/app.py

# Run API client
python examples/api_client.py --current

# Serve documentation
mkdocs serve

# Deactivate venv
deactivate
```

---

**Ready to dive deeper?** Check out the [full documentation](../index.md) or start with [installing Thonny](../guides/thonny_installation.md) for Pico development!
