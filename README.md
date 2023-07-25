# Coding Interview

Repository for interview


## Requirements

Have following tools installed:

- Docker
- Python 3.11

## Setup Steps

1. Build docker image
2. Run container from built image publishing port 8080
3. Create a python virtual environment
4. Install python dependencies from requirements.txt


## Accessing CloudBeaver

1. http://localhost:9000
2. Click next one welcome screen
3. Add a password - password
4. Click next
5. Click Finish
6. Log in with 
    username: cbadmin 
    password: password
7. Add new connection manager 
8. Select postgresql driver
9. Configure driver values
    host: host.docker.internal
    database: payroll
    username: postgres
    password: password
10. Click Save credentials
11. Click Create

## Challenge

1. Run test using pytest
2. Fix failing tests for assigned test file under the tests directory
3. Identify additional tests that can be written for the application under test
    - Use the documentation and acceptance criteria outlined in the test file

*Note: The applications under tests have a few issues built in. Try and identify then with your tests and potentially look to fix it.
