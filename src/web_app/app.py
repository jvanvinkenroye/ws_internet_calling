"""
Number Transmitter Web Application

This Flask application displays numbers 1-9 that automatically rotate every second.
Simulates a Nummernsender (number transmitter) system.
"""

import logging
from flask import Flask, render_template

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create Flask application
app = Flask(__name__)


@app.route('/')
def index():
    """
    Serve the main number transmitter page.

    Returns:
        str: Rendered HTML template
    """
    logger.info("Serving number transmitter web page")
    return render_template('index.html')


@app.route('/health')
def health():
    """
    Health check endpoint.

    Returns:
        dict: Status information
    """
    return {"status": "healthy", "service": "number-transmitter-web"}


if __name__ == '__main__':
    logger.info("Starting Number Transmitter Web Application")
    app.run(host='0.0.0.0', port=5000, debug=True)
