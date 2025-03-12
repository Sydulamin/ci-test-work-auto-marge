# CI/CD with GitHub Actions

This repository demonstrates the use of GitHub Actions for CI/CD to automate code linting, code quality checks, unit tests, and the merging of feature branches into the `dev` branch after successful checks.

## Features

- **Linting**: Ensures the code follows PEP8 style guides using `flake8`.
- **Code Quality**: Uses `radon` to check the complexity of the code.
- **Unit Testing**: Runs unit tests using `pytest`.
- **Automatic Merge**: Merges the feature branch into the `dev` branch after successful CI checks.

## Setup

### Prerequisites

1. **Python 3.10+** is required to run this project.
2. You will need the following dependencies:
    - `flake8` (for linting)
    - `radon` (for code quality checks)
    - `pytest` (for running tests)

### Steps to Run Locally

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - **For Linux/Mac**:
      ```bash
      source venv/bin/activate
      ```

    - **For Windows**:
      ```bash
      venv\Scripts\activate
      ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Linter

To run the linter with `flake8`, use:
```bash
flake8 main.py
