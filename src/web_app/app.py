"""
Number Transmitter Web Application

This Flask application displays numbers 1-9 that automatically rotate every second.
Simulates a Nummernsender (number transmitter) system.
"""

import logging
import socket
from flask import Flask, render_template

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create Flask application
app = Flask(__name__)


def get_local_ip():
    """
    Get the local IP address of the host.

    Returns:
        str: Local IP address or 'localhost' if unable to determine
    """
    try:
        # Create a socket to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        logger.warning(f"Could not determine local IP: {e}")
        return "localhost"


@app.route("/")
def index():
    """
    Serve the main number transmitter page.

    Returns:
        str: Rendered HTML template
    """
    local_ip = get_local_ip()
    port = 5555
    logger.info(f"Serving number transmitter web page at {local_ip}:{port}")
    return render_template("index.html", local_ip=local_ip, port=port)


@app.route("/health")
def health():
    """
    Health check endpoint.

    Returns:
        dict: Status information
    """
    return {"status": "healthy", "service": "number-transmitter-web"}


if __name__ == "__main__":
    local_ip = get_local_ip()
    port = 5555
    logger.info("Starting Number Transmitter Web Application")
    logger.info(f"Access locally at: http://localhost:{port}")
    logger.info(f"Access from network at: http://{local_ip}:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
