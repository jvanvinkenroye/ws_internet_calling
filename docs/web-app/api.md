# Number Transmitter API

REST API for machine-readable access to the number transmission system.

## Base URL

```
http://localhost:5001
```

## Endpoints

### GET /api/number

Get the current transmitted number with metadata.

**Response:**
```json
{
  "number": 5,
  "timestamp": "2025-01-15T10:30:45.123456",
  "unix_timestamp": 1736935845.123456,
  "next_change_in": 0.876544,
  "cycle_position": 5,
  "total_cycles": 12345
}
```

### GET /api/sequence

Get sequence configuration information.

**Response:**
```json
{
  "sequence": [1, 2, 3, 4, 5, 6, 7, 8, 9],
  "length": 9,
  "interval_seconds": 1,
  "description": "Numbers 1-9 rotating every second"
}
```

### GET /api/status

Get API status and uptime.

**Response:**
```json
{
  "status": "running",
  "uptime_seconds": 123.456,
  "current_number": 5,
  "api_version": "1.0.0",
  "service": "number-transmitter-api"
}
```

## Usage Examples

See [examples/api_client.py](../../examples/api_client.py) for a complete Python client.

**Quick Example:**
```python
import requests

response = requests.get('http://localhost:5001/api/number')
data = response.json()
print(f"Current number: {data['number']}")
```
