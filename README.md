# Python Log Monitor

A Python application that analyzes log files, counts log levels, validates timestamps, and generates a JSON report.

## Features

- Reads and analyzes multiple `.log` files.
- Counts log levels: ERROR, INFO, WARNING, UNKNOWN, and INVALID.
- Validates log timestamps.
- Handles file reading errors.
- Generates a JSON report.
- Includes automated tests using pytest.
- Supports Docker.
- Uses GitHub Actions for continuous integration (CI).

## Project Structure

```text
python-log-monitor/
│
├── main.py
├── log_functions.py
├── test_main.py
├── Dockerfile
├── .dockerignore
├── README.md
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
└── logs/
    ├── server.log
    └── sample.log
```

## Requirements

- Python 3.14 or later
- Docker (optional)
- pytest

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd python-log-monitor
   ```

3. Install pytest:

   ```bash
   python -m pip install pytest
   ```

## Usage

Run the application:

```bash
python main.py
```

The application reads all `.log` files from the `logs/` directory, analyzes their contents, and displays a report in the terminal.

A JSON report named `report.json` is generated after processing the log files.

## Testing

Run the automated tests:

```bash
python -m pytest -v
```

The tests cover log level counting, timestamp validation, and JSON report generation.

## Docker

Build the Docker image:

```bash
docker build -t python-log-monitor .
```

Run the application:

```bash
docker run --rm python-log-monitor
```

### Using Docker Volumes

To use log files from the local `logs/` directory:

```bash
docker run --rm -v "$(pwd)/logs:/app/logs" python-log-monitor
```

This allows the container to access local log files without rebuilding the Docker image whenever the log files change.

## Continuous Integration

This project uses GitHub Actions to automatically run tests on every push.

The CI workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs pytest.
4. Runs the automated tests.