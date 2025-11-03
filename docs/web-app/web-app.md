# Number Transmitter Web Application

The Number Transmitter Web Application is an interactive, browser-based interface that displays numbers 1-9 in continuous rotation.

## Overview

The web application provides a visual representation of the number transmission system with real-time updates and user controls.

## Features

- **Automatic Number Rotation**: Numbers change from 1 to 9 every second
- **Interactive Controls**: Start, Stop, and Reset functionality
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Visual Feedback**: Large, animated number display
- **Cycle Counter**: Tracks complete rotation cycles
- **Modern UI**: Gradient backgrounds and smooth animations

## Architecture

### Backend (Flask)

**File**: `src/web_app/app.py`

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

The backend serves:
- HTML template at root route `/`
- Static files (CSS, JavaScript)
- Health check endpoint at `/health`

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

# Navigate to web app directory
cd src/web_app

# Run the application
python app.py
```

Access at: [http://localhost:5000](http://localhost:5000)

### Production Mode

```bash
# Install gunicorn
uv add gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 src.web_app.app:app
```

## User Interface

### Number Display

The central number display shows the current number (1-9) in large, bold text with animation effects.

### Controls

- **Start Button**: Begin automatic number rotation
- **Stop Button**: Pause the rotation
- **Reset Button**: Return to number 1 and reset cycle counter

### Status Information

- **Current Status**: Running or Stopped
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
# Change port in app.py
app.run(port=5001)

# Or kill existing process
lsof -ti:5000 | xargs kill -9  # macOS/Linux
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
