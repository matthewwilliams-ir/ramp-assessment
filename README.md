## Ramp Assessment

> A simple Flask API that transforms a 3x7 dataframe by multiplying it by an input vector

* [Project Assumptions](#project-assumptions)
* [Requirements](#requirements)
* [Installation](#installation)
* [Using the API](#using-the-api)
* [Running Unit Tests](#running-unit-tests)

### Project Assumptions
* The provided input will always be a list of 7 comma-separated decimal values (I've implemented validation to ensure this)
* The original weekly results will remain the same through out:
```
1,1,1,1,1,1,1
2,2,2,2,2,2,2
3,3,3,3,3,3,3
``` 

### Requirements
* Python >= 3.7
* Poetry

#### Python >= 3.7
If you do not have python installed, install the latest version of python for your OS: https://www.python.org/downloads/

#### Poetry
This project uses `poetry` for package and dependency management.

If you do not already have `poetry` installed, follow the installation steps as outlined here: https://python-poetry.org/docs/#installation

Once you have it installed on your environment, verify that it's installed by executing the following command in your terminal:

```bash
poetry --version
```
If you see something like Poetry 0.12.0 then you are ready to use Poetry

### Installation

1. Clone this repository

Clone the repository to a directory of your choice and navigate to the cloned directory:

```bash
cd ramp_assessment
```

2. Activate virtual environment with `poetry shell`

Instantiate a new virtual environment in the `ramp_assessment` directory by creating a new shell with:

```bash
poetry shell
```

3. Install project dependencies

```bash
poetry install
```

4. Run the app

```bash
export FLASK_ENV=development
export FLASK_APP=ramp_assessment
poetry run flask run
```
Once up and running, the app server will be accessible at:
 http://127.0.0.1:5000/

### Using the API

Once the app is up and running, the application is ready to receive API requests. 

The app exposes the following endpoint to submit input data via request body and responds with the modified dataframe in the form of a json object:

```
POST /transform/multiply

Request Body:

{"input": "0.1,0.9,0.123,0.99,0.5,1.0,0.0"}
```
> The input data is assumed to always be a comma-separated list of 7 decimal values. The API will respond with the appropriate HTTP error if not.

Example using `curl`:
```bash
curl --location --request POST 'localhost:5000/transform/multiply' \
--header 'Content-Type: application/json' \
--data-raw '{"input": "0.1,0.9,0.123,0.99,0.5,1.0,0.0"}'
```

Response:

```json
{
    "modified_results": {
        "week_1": {
            "1": 0.2,
            "2": 0.9,
            "3": 0.123,
            "4": 0.99,
            "5": 0.5,
            "6": 1.0,
            "7": 0.0
        },
        "week_2": {
            "1": 0.4,
            "2": 1.8,
            "3": 0.246,
            "4": 1.98,
            "5": 1.0,
            "6": 2.0,
            "7": 0.0
        },
        "week_3": {
            "1": 0.6,
            "2": 2.7,
            "3": 0.369,
            "4": 2.97,
            "5": 1.5,
            "6": 3.0,
            "7": 0.0
        }
    },
    "original_results": {
        "week_1": {
            "1": 1.0,
            "2": 1.0,
            "3": 1.0,
            "4": 1.0,
            "5": 1.0,
            "6": 1.0,
            "7": 1.0
        },
        "week_2": {
            "1": 2.0,
            "2": 2.0,
            "3": 2.0,
            "4": 2.0,
            "5": 2.0,
            "6": 2.0,
            "7": 2.0
        },
        "week_3": {
            "1": 3.0,
            "2": 3.0,
            "3": 3.0,
            "4": 3.0,
            "5": 3.0,
            "6": 3.0,
            "7": 3.0
        }
    }
}
```

### Running Unit Tests

This project uses `pytest` and `coverage` for unit tests. Execute the unit tests as follows:

```bash
poetry run pytest

# With coverage
poetry run coverage run -m pytest
```

Test coverage report

```bash
poetry run coverage report -m
# OR
poetry run coverage html
```
