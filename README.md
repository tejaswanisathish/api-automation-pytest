# Automation of Reqres API testing using Python

This repository contains the automation of the [Reqres API](https://reqres.in/) using Python

- Requests to the API are done using the [HTTPx](https://www.python-httpx.org/) library.
- The tests are written using the [pytest](https://docs.pytest.org/en/stable/) framework.
- Data validation is done using the [Pydantic](https://pydantic-docs.helpmanual.io/) library.

## Installation

1. Extract this repository to a folder of your choice.
2. Open a terminal and navigate to the folder where you extracted the repository.
3. Create a virtual environment using the following command:

```bash
python -m venv venv
```

4. Activate the virtual environment using the following command:

```bash
venv\Scripts\activate
```

5. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Open a terminal and navigate to the folder where you extracted the repository.

2. Activate the virtual environment using the following command:

```bash
venv\Scripts\activate
```

3. Run the tests using the following command:

```bash
pytest -v
```
