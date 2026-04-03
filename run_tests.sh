#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Execute the test suite using Firefox in headless mode
pytest --webdriver Firefox --headless test_app.py

# Return exit code 0 if all tests passed, or 1 if something went wrong
if [ $? -eq 0 ]; then
    echo "Tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi
