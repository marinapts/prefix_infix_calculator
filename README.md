# Prefix & Infix Calculator

A calculator that accepts numerical calculations in prefix and infix notations,
as specified in https://github.com/Kheiron-Medical/swe_take_home_exercise.

I follow the assumptions provided and distinguish between the two notations given the input expression.

* **calculator.py** contains the functionality for parts 1 and 2 (prefix and infix calculation)
* **calculator_api.py** creates a RESTful API served on http://127.0.0.1:5000/, where the user can access and interact through a user interface.
* **test_calculator.py** contains test cases for the functionality of calculator.py.


## Installation
This project is implemented using Python 3.8.3 and pip version 19.2.3 and uses Flask to
create a RESTful API and serve a simple user interface.

Create a local environment and install the requirements:

```
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Run the app

### Command line
The calculator can be run through the command line with either one of these two options:

1. Pass the expression as an argument through *--input* when running the file:

```python calculator.py --input '- 12 * 2 6'```

2. Run the file without passing any arguments and wait for the prompt. This way you can test many expressions
without rerunning the file: ```python calculator.py```


### REST API
Export the FLASK_APP environment variable and run the API locally.
```
export FLASK_APP=calculator_api.py
flask run
```

The API is now running on http://127.0.0.1:5000/, where the user can input an expression and view the result or any error messages.

## Testing
Run ```pytest``` to run all the tests written in **test_calculator.py**. The tests calculate all the examples provided in
https://github.com/Kheiron-Medical/swe_take_home_exercise, as well as corner cases.
