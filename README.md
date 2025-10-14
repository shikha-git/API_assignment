This project validates API: "https://api.restful-api.dev/objects".

SETUP:

1. To run the tests locally in pycharm editor or terminal, please install Python 3.9 and then pytest ("pip install pytest").

2. Then run the make file to install venev and then activate it to run tests

    2.a make test

    2.b source venv/bin/activate

3. use "pytest" to run all the files starting with prefix test_ in the given directory.

4. Use "pytest objects_api.py" to run all the tests in this file.

5. To run a particular test, use "pytest test_objects_api.py -k <test-name>

6. "pip install pytest-html" to generate the test report and then copy the report.html file path on the browser to view the results.

7. Use the command pytest objects_api.py --html=report.html to generate the report.

8. pytest.yml file is created in github to run the pytest whenever there is a new code commit.

9. After the workflow completes (CI/CD), navigate to the "Actions" tab in the GitHub repository, select the specific workflow run, and locate the "Artifacts" section. 
Download the pytest-html-report artifact, which will contain  report.html file.
Unzip the downloaded artifact and open the report.html file in your local web browser.
