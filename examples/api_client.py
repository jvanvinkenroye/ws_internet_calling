"""
Number Transmitter API Client Example

This script demonstrates how to consume the Number Transmitter API.
Shows different API endpoints and how to process the responses.
"""

import argparse
import logging
import sys
import time
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class NumberTransmitterClient:
    """Client for interacting with the Number Transmitter API."""

    def __init__(self, base_url='http://localhost:5001'):
        """
        Initialize the API client.

        Args:
            base_url (str): Base URL of the API server
        """
        self.base_url = base_url.rstrip('/')
        logger.info(f"API Client initialized for {self.base_url}")

    def get_current_number(self):
        """
        Get the current transmitted number.

        Returns:
            dict: API response with current number and metadata

        Raises:
            requests.RequestException: If the API request fails
        """
        try:
            response = requests.get(f"{self.base_url}/api/number", timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            logger.error(f"Failed to get current number: {error}")
            raise

    def get_sequence_info(self):
        """
        Get information about the number sequence.

        Returns:
            dict: API response with sequence configuration

        Raises:
            requests.RequestException: If the API request fails
        """
        try:
            response = requests.get(f"{self.base_url}/api/sequence", timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            logger.error(f"Failed to get sequence info: {error}")
            raise

    def get_status(self):
        """
        Get API status and uptime.

        Returns:
            dict: API response with status information

        Raises:
            requests.RequestException: If the API request fails
        """
        try:
            response = requests.get(f"{self.base_url}/api/status", timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            logger.error(f"Failed to get status: {error}")
            raise

    def monitor(self, duration=10, interval=1):
        """
        Monitor the number transmitter for a specified duration.

        Args:
            duration (int): How long to monitor in seconds
            interval (float): How often to check in seconds
        """
        logger.info(f"Monitoring for {duration} seconds (checking every {interval}s)")
        start_time = time.time()

        try:
            while time.time() - start_time < duration:
                data = self.get_current_number()
                print(f"Number: {data['number']} | "
                      f"Cycle: {data['total_cycles']} | "
                      f"Next change in: {data['next_change_in']:.2f}s")
                time.sleep(interval)
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
        except Exception as error:
            logger.error(f"Monitoring error: {error}")


def main():
    """
    Main entry point for the API client.
    """
    parser = argparse.ArgumentParser(
        description='Number Transmitter API Client',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Get current number
  %(prog)s --current

  # Get API status
  %(prog)s --status

  # Monitor for 30 seconds
  %(prog)s --monitor --duration 30

  # Use custom API URL
  %(prog)s --url http://192.168.1.100:5001 --current
        '''
    )

    parser.add_argument(
        '--url',
        default='http://localhost:5001',
        help='API base URL (default: http://localhost:5001)'
    )
    parser.add_argument(
        '--current',
        action='store_true',
        help='Get the current number'
    )
    parser.add_argument(
        '--status',
        action='store_true',
        help='Get API status'
    )
    parser.add_argument(
        '--sequence',
        action='store_true',
        help='Get sequence information'
    )
    parser.add_argument(
        '--monitor',
        action='store_true',
        help='Monitor number changes continuously'
    )
    parser.add_argument(
        '--duration',
        type=int,
        default=10,
        help='Monitoring duration in seconds (default: 10)'
    )
    parser.add_argument(
        '--interval',
        type=float,
        default=1.0,
        help='Monitoring check interval in seconds (default: 1.0)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )

    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Create client
    client = NumberTransmitterClient(base_url=args.url)

    try:
        # Execute requested action
        if args.current:
            data = client.get_current_number()
            print(f"Current Number: {data['number']}")
            print(f"Timestamp: {data['timestamp']}")
            print(f"Total Cycles: {data['total_cycles']}")

        elif args.status:
            data = client.get_status()
            print(f"Status: {data['status']}")
            print(f"Uptime: {data['uptime_seconds']:.2f} seconds")
            print(f"Current Number: {data['current_number']}")
            print(f"API Version: {data['api_version']}")

        elif args.sequence:
            data = client.get_sequence_info()
            print(f"Sequence: {data['sequence']}")
            print(f"Length: {data['length']}")
            print(f"Interval: {data['interval_seconds']} second(s)")
            print(f"Description: {data['description']}")

        elif args.monitor:
            client.monitor(duration=args.duration, interval=args.interval)

        else:
            parser.print_help()
            sys.exit(1)

    except Exception as error:
        logger.error(f"Error: {error}")
        sys.exit(1)


if __name__ == '__main__':
    main()
