This project validates API: "https://api.restful-api.dev/objects".

To run the tests, please install Python 3.9 and then pytest ("pip install pytest").

Then run the make file to install venev and then activate it to run tests

make test

source venv/bin/activate


Use "pytest objects_api.py" to run all the tests in this file.

To run a particular test, use "pytest objects_api.py -k <test-name>

"pip install pytest-html" to generate the test report and then copy the report.html file path on the browser to view the results.

Use the command pytest objects_api.py --html=report.html to generate the report.

pytest.yml fil is created in github to run the pytest whenver there is a new code commit.
