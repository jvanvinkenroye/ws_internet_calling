# Number Transmitter Web Application

The Number Transmitter Web Application is an interactive, browser-based interface that displays numbers 1-9 in continuous rotation.

## Overview

The web application provides a visual representation of the number transmission system with real-time updates and user controls.

## Features

- **Automatic Number Rotation**: Numbers change from 1 to 9 every second
- **Interactive Controls**: Start, Stop, and Reset functionality
- **Server Sync Mode**: Optional synchronization with server-side API rotation
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Visual Feedback**: Large, animated number display
- **Cycle Counter**: Tracks complete rotation cycles
- **Modern UI**: Gradient backgrounds and smooth animations
- **Combined with API**: Web interface and REST API in one application

## Architecture

### Backend (Flask)

**File**: `src/web_app/app.py`

```python
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for API endpoints

@app.route('/')
def index():
    return render_template('index.html', local_ip=local_ip, port=port)

@app.route('/api/number')
def get_number():
    # Returns current number with metadata
    return jsonify({...})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
```

The backend serves:
- HTML template at root route `/`
- Static files (CSS, JavaScript)
- REST API endpoints at `/api/*`
- Health check endpoint at `/health`
- CORS-enabled for cross-origin requests

### Frontend

**Files**:
- `src/web_app/templates/index.html` - HTML structure
- `src/web_app/static/css/style.css` - Styling
- `src/web_app/static/js/main.js` - JavaScript logic

## Running the Application

### Development Mode

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the combined application (from project root)
python src/web_app/app.py
```

Access at:
- **Web Interface:** [http://localhost:5555](http://localhost:5555)
- **API Endpoints:** [http://localhost:5555/api/number](http://localhost:5555/api/number)

### Production Mode

```bash
# Install gunicorn
uv add gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5555 src.web_app.app:app
```

## User Interface

### Number Display

The central number display shows the current number (1-9) in large, bold text with animation effects.

### Controls

- **Server Sync Mode Toggle**: Enable/disable synchronization with server API
  - When enabled: Displays server-side number rotation (disables manual controls)
  - When disabled: Uses client-side rotation with manual controls
- **Start Button**: Begin automatic number rotation (manual mode only)
- **Stop Button**: Pause the rotation (manual mode only)
- **Reset Button**: Return to number 1 and reset cycle counter (manual mode only)

### Status Information

- **Current Status**: Running, Stopped, or Syncing with Server
- **Rotation Count**: Number of complete 1-9 cycles

## Technical Details

### Number Rotation Logic

JavaScript handles the client-side number rotation:

```javascript
rotateNumber() {
    this.currentNumber++;

    if (this.currentNumber > 9) {
        this.currentNumber = 1;
        this.rotationCount++;
    }

    this.updateDisplay();
}
```

### Update Interval

Numbers change every 1000ms (1 second) using `setInterval`:

```javascript
this.intervalId = setInterval(() => {
    this.rotateNumber();
}, 1000);
```

### Animation

CSS transitions provide smooth visual feedback:

```css
.number {
    transition: transform 0.3s ease;
}

.number:hover {
    transform: scale(1.1);
}
```

## Customization

### Change Rotation Speed

Edit `main.js`:

```javascript
// Change interval (in milliseconds)
this.intervalId = setInterval(() => {
    this.rotateNumber();
}, 500);  // Now rotates every 0.5 seconds
```

### Change Number Range

Edit `main.js`:

```javascript
// Change from 1-9 to 1-5
if (this.currentNumber > 5) {
    this.currentNumber = 1;
    this.rotationCount++;
}
```

### Customize Styling

Edit `static/css/style.css`:

- Change colors in gradient background
- Modify button styles
- Adjust responsive breakpoints
- Update fonts and sizes

## Browser Compatibility

Tested and working on:

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## Troubleshooting

### Port Already in Use

```bash
# Change port in src/web_app/app.py
port = 5556  # Use any available port

# Or kill existing process
lsof -ti:5555 | xargs kill -9  # macOS/Linux
netstat -ano | findstr :5555   # Windows (then use taskkill)
```

### Static Files Not Loading

- Check file paths in HTML
- Verify files exist in `static/` directory
- Clear browser cache (Ctrl+Shift+R)

### JavaScript Not Working

- Open browser DevTools (F12)
- Check Console tab for errors
- Verify `main.js` is loaded in Network tab

## Next Steps

- [API Documentation](api.md) - Learn about the REST API
- [Running Applications](running.md) - Deployment guide
- [Pico Integration](../pico/examples/api-consumer.md) - Connect IoT devices

## Code Reference

Full source code:
- `src/web_app/app.py:8` - Flask application
- `src/web_app/templates/index.html` - HTML template
- `src/web_app/static/css/style.css` - Styling
- `src/web_app/static/js/main.js:23` - NumberTransmitter class
