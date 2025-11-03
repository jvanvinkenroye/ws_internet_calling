"""
Number Transmitter API

This Flask API provides machine-readable access to number transmissions.
Returns numbers 1-9 in a rotating sequence, changing every second.
"""

import logging
import time
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Global state for number rotation
# This simulates a continuous rotation starting from application start
START_TIME = time.time()


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
        "service": "number-transmitter-api"
    }

    return jsonify(response)


@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint for monitoring.

    Returns:
        JSON response with health status
    """
    return jsonify({"status": "healthy", "service": "number-transmitter-api"})


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


if __name__ == '__main__':
    logger.info("Starting Number Transmitter API")
    logger.info(f"API will rotate through numbers 1-9, changing every second")
    app.run(host='0.0.0.0', port=5001, debug=True)
