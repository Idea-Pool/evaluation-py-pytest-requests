# evaluation-py-pytest-requests

This is a test-ware to evaluate the Pytest automation tool with Python and requests library.

## Prerequisites

In order to execute the implemented test cases, an account is needed on the https://www.themoviedb.org/.
If the account is created the API Key (v3 auth) should be added to the [constants](constants.py) instead of the {YOUR_API_KEY} as a string.

1. Python 3.8+
1. Pip
1. pytest 6.1.2
1. requests 2.25.0

## Framework used

| Framework | Documentation                                                                                                             |
|:----------|:--------------------------------------------------------------------------------------------------------------------------|
| pytest    | [pytest](https://docs.pytest.org/en/stable/index.html) is a framework that makes building simple and scalable tests easy. |
| requests  | [Requests](https://pypi.org/project/requests/) is a simple, yet elegant HTTP library.                                     |

## Test cases

The implemented test cases can be found in [API.md](test_cases/API.md).

## Setup

```shell
pip install -r requirements.txt
```

## Execution
To execute all the test cases:
```shell
pytest
```

To execute one test module:
```shell
pytest test/test_get.py::TestGetMethod
```

To execute one test function:
```shell
pytest test/test_get.py::TestGetMethod::test_get_status_code
```

To log the information during the execution, the following command can be used:
```shell
pytest --log-level=INFO -s
```