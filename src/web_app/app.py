"""
Number Transmitter Web Application

This Flask application displays numbers 1-9 that automatically rotate every second.
Simulates a Nummernsender (number transmitter) system.
"""

import logging
import socket
import os
from pathlib import Path
from flask import Flask, render_template, send_file, abort

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


def get_pico_examples():
    """
    Get information about all Pico example scripts.

    Returns:
        list: List of dictionaries containing example metadata
    """
    examples = [
        {
            "id": "blink",
            "title": "LED Blink",
            "filename": "01_blink.py",
            "description": "Basic LED blinking - the 'Hello World' of hardware programming"
        },
        {
            "id": "wifi_connect",
            "title": "WiFi Connection",
            "filename": "02_wifi_connect.py",
            "description": "Connect to a WiFi network and display connection information"
        },
        {
            "id": "signal_monitor",
            "title": "WiFi Signal Monitor",
            "filename": "03_wifi_signal_monitor.py",
            "description": "Monitor and display WiFi signal strength in real-time"
        },
        {
            "id": "signal_to_blink",
            "title": "Signal to Blink",
            "filename": "04_wifi_signal_to_blink.py",
            "description": "Convert WiFi signal strength to LED blink frequency"
        },
        {
            "id": "api_consumer",
            "title": "API Consumer",
            "filename": "05_api_consumer.py",
            "description": "Query the Number Transmitter API and blink LED accordingly"
        },
        {
            "id": "access_point",
            "title": "Access Point",
            "filename": "06_access_point_web.py",
            "description": "Create a WiFi access point with web-based LED control"
        }
    ]
    return examples


def get_example_code(filename):
    """
    Read the code for a specific example file.

    Args:
        filename (str): Name of the example file

    Returns:
        str: File contents or None if file not found
    """
    try:
        # Get the path to the pico_scripts directory
        base_dir = Path(__file__).parent.parent
        example_path = base_dir / "pico_scripts" / filename

        if example_path.exists():
            with open(example_path, 'r') as f:
                return f.read()
        else:
            logger.error(f"Example file not found: {example_path}")
            return None
    except Exception as e:
        logger.error(f"Error reading example file {filename}: {e}")
        return None


@app.route("/")
def index():
    """
    Serve the main number transmitter page.

    Returns:
        str: Rendered HTML template
    """
    local_ip = get_local_ip()
    port = 5555
    examples = get_pico_examples()

    # Add code content to each example
    for example in examples:
        example['code'] = get_example_code(example['filename'])

    logger.info(f"Serving number transmitter web page at {local_ip}:{port}")
    return render_template("index.html", local_ip=local_ip, port=port, examples=examples)


@app.route("/download/<filename>")
def download_example(filename):
    """
    Download a specific example file.

    Args:
        filename (str): Name of the file to download

    Returns:
        File download response or 404 error
    """
    try:
        # Security: Only allow downloading from the pico_scripts directory
        # and only .py files
        if not filename.endswith('.py'):
            abort(404)

        # Get the path to the pico_scripts directory
        base_dir = Path(__file__).parent.parent
        example_path = base_dir / "pico_scripts" / filename

        if example_path.exists() and example_path.is_file():
            logger.info(f"Downloading example: {filename}")
            return send_file(
                example_path,
                as_attachment=True,
                download_name=filename,
                mimetype='text/x-python'
            )
        else:
            logger.warning(f"Example file not found: {filename}")
            abort(404)

    except Exception as e:
        logger.error(f"Error downloading file {filename}: {e}")
        abort(500)


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
