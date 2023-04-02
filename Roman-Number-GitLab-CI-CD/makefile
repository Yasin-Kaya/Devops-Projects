.PHONY: test

test:
    # Test GET request to the homepage
    curl -X GET -I http://localhost:80
    # Test invalid input to the form
    curl -X POST -d "number=invalid" -I http://localhost:80
    # Test valid input to the form
    curl -X POST -d "number=2021" -I http://localhost:80
