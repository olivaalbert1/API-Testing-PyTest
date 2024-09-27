# API-Testing-PyTest
RESTful API Testing with PyTest

How to start
create new env
```
python3 -m venv /path/to/folder
```

activate the environment
```
source /path/to/folder/bin/activate
```

install pytest
```
pip install pytest requests
```

Improvements
Error Handling: tests that deliberately trigger error scenarios (e.g., invalid input, missing resources) and ensure the  API responds with expected codes and messages.
Parameterization: Use PyTest’s parameterization feature to efficiently test multiple input variations within a single test function.