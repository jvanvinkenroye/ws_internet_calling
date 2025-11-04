"""
Number Transmitter Combined Application

This Flask application provides both a web interface and REST API for the number transmitter.
Displays numbers 1-9 that automatically rotate every second via both web UI and JSON API.
Simulates a Nummernsender (number transmitter) system.
"""

import logging
import socket
import time
from datetime import datetime
from flask import Flask, render_template, jsonify
from flask_cors import CORS

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests (needed for API)

# Global state for number rotation
# This simulates a continuous rotation starting from application start
START_TIME = time.time()


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


def get_current_number():
    """
    Calculate the current number based on elapsed time.
    Numbers rotate from 1 to 9, changing every second.

    Returns:
        int: Current number (1-9)
    """
    elapsed_seconds = int(time.time() - START_TIME)
    # Calculate position in 1-9 cycle (0-8 mapped to 1-9)
    current_number = (elapsed_seconds % 9) + 1
    return current_number


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
    Health check endpoint for monitoring.

    Returns:
        JSON response with health status
    """
    return jsonify({"status": "healthy", "service": "number-transmitter-combined"})


# ============================================================================
# API Routes
# ============================================================================


@app.route('/api/number', methods=['GET'])
def get_number():
    """
    Get the current transmitted number.

    Returns:
        JSON response with current number, timestamp, and metadata

    Example response:
    {
        "number": 5,
        "timestamp": "2025-01-15T10:30:45.123456",
        "unix_timestamp": 1736935845.123456,
        "next_change_in": 0.876544,
        "cycle_position": 5,
        "total_cycles": 12345
    }
    """
    current_number = get_current_number()
    now = time.time()
    elapsed = now - START_TIME

    # Calculate when next number change occurs
    next_change_in = 1.0 - (elapsed % 1.0)

    # Calculate total complete cycles
    total_cycles = int(elapsed / 9)

    response = {
        "number": current_number,
        "timestamp": datetime.now().isoformat(),
        "unix_timestamp": now,
        "next_change_in": round(next_change_in, 6),
        "cycle_position": current_number,
        "total_cycles": total_cycles
    }

    logger.debug(f"API request: returning number {current_number}")
    return jsonify(response)


@app.route('/api/sequence', methods=['GET'])
def get_sequence():
    """
    Get information about the number sequence.

    Returns:
        JSON response with sequence configuration

    Example response:
    {
        "sequence": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "length": 9,
        "interval_seconds": 1,
        "description": "Numbers 1-9 rotating every second"
    }
    """
    response = {
        "sequence": list(range(1, 10)),
        "length": 9,
        "interval_seconds": 1,
        "description": "Numbers 1-9 rotating every second"
    }

    return jsonify(response)


@app.route('/api/status', methods=['GET'])
def get_status():
    """
    Get API status and uptime information.

    Returns:
        JSON response with API status

    Example response:
    {
        "status": "running",
        "uptime_seconds": 123.456,
        "current_number": 5,
        "api_version": "1.0.0"
    }
    """
    uptime = time.time() - START_TIME

    response = {
        "status": "running",
        "uptime_seconds": round(uptime, 3),
        "current_number": get_current_number(),
        "api_version": "1.0.0",
        "service": "number-transmitter-combined"
    }

    return jsonify(response)


# ============================================================================
# Error Handlers
# ============================================================================


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.

    Args:
        error: The error object

    Returns:
        JSON response with error message
    """
    return jsonify({
        "error": "Not found",
        "message": "The requested endpoint does not exist"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors.

    Args:
        error: The error object

    Returns:
        JSON response with error message
    """
    logger.error(f"Internal server error: {error}")
    return jsonify({
        "error": "Internal server error",
        "message": "An unexpected error occurred"
    }), 500


if __name__ == "__main__":
    local_ip = get_local_ip()
    port = 5555
    logger.info("Starting Number Transmitter Combined Application")
    logger.info(f"API will rotate through numbers 1-9, changing every second")
    logger.info("")
    logger.info(f"Web Interface:")
    logger.info(f"  Local:   http://localhost:{port}")
    logger.info(f"  Network: http://{local_ip}:{port}")
    logger.info("")
    logger.info(f"API Endpoints:")
    logger.info(f"  Current Number: http://localhost:{port}/api/number")
    logger.info(f"  Sequence Info:  http://localhost:{port}/api/sequence")
    logger.info(f"  API Status:     http://localhost:{port}/api/status")
    logger.info(f"  Health Check:   http://localhost:{port}/health")
    app.run(host="0.0.0.0", port=port, debug=True)
