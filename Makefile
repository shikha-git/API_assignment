 # Define a phony target for 'all' to ensure it's always run
    .PHONY: all clean test install

    # Default target
    all: test

    # Target to run tests
    test:
    	pytest

    # Target to install dependencies
    install:
    	pip install -r requirements.txt

    # Target to clean up generated files
    clean:
    	rm -rf __pycache__ .pytest_cache .coverage htmlcov/

    # Example of a target to run a specific Python script
    run_script:
    	pytest objects_api.py -k <test_name>