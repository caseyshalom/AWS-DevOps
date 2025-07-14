The main purpose of unit testing is to ensure a unit of software performs as it is designed. Unit testing quickly identifies and isolates issues in individual units of application code.

Every commit made to each branch should initiate an automated test. The unit tests run on the compiled code. This ensures that as developers commit code to the repository, the changes don’t break the old code.

One measure of unit testing quality is code coverage. Code coverage is a measure of how much of the source code is tested.

File "calc_function.py" is the main module file (with function implementations), while "calc_test.py" contains the PyTest test cases for it.