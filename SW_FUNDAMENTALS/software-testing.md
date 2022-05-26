#   Table of Contents

#   Software Testing - an Overview

Separated into two general categories
*   Functional Testing
*   Non-Functional Testing

##  Functional Testing
Whether sotware behaves as intended in a logical sense
*   Unit Testing examines low-level details
    *   Do components return expected results?
    *   Do we reject known-bad input?
    *   Input validation
*   Integration Testing examines high-level functionality
    *   Do components communicate properly
    *   Do database connections function as expected

##  Non-Functional Testing (NFTs)
Examines if software is fit for purpose, minimizes risk, and provides intended value

Examines
*   Usability
*   Performance
*   Security
*   Resilience
*   Compliance
    *   Regulations and standards

#   Unit Testing - Python Overview
Unit Testing - detailed functional testing of small, isolated pieces of code.

Unit test frameworks let you make assertions about testable conditions (return values, etc.)

In python, `assert` keyword is native, and can assert that one variable should equal one value.

Python Unit Testing Frameworks include:
*   `unittest`, a default framework that allows tests to be created by extended a default TestCase class
*   `PyTest`, a framework that can be added that allows devs to build tests by using functions, rather than class methods. Used by PyATS from Cisco.

It's best to test lower level functions and confirm their functionality before continuing to test higher-level functions that depend on them.

##  Simple unit testing with PyTest
PyTest automatically executes any scripts that start with `test_` or end with `_test.py` 

Within those scripts, any functions beginning with `test_` or `tests_` are automatically executed.


**Tests in these functions**
*   Use the `assert` keyword
*   Results are compiled and reported upon
*   Can be run using the `pytest` command on the python file that includes tests
*   Should be separated based on low-level functionality being tested

Pytest is straightforward to run, but does not give detailed results as to where the error may have occurred, especially in higher-order functions. 

##  Simple unit testing with unittest
Unittests is dependent on a class being instantiated and overridden to begin a testing suite

**Tests implemented in the class**
*   Use the `assertEqual` function
    *   One of MANY
*   Should be separated based on low-level functionality being tested

#   Test-Driven Development

Building small unit and integration tests allow us to know
*   If the software behaves as expected
*   If it's built-to-purpose

Before committing the code to a remote repo or to production.

Traditionally, tests were written to validate existing code

Test-Driven Development dictates that test code should derive development code

##  Test-Driven Development Process
1.   Create a new test (or add to existing)
2.   Run tests to see if any fail
    *   Expected failures are acceptable
3.   Write application code to pass the new test
4.   Run tests to see if any fail
5.   Refactor and improve application code

##  Why TDD?
*   Ensure that code is highly-testable
*   Clarify and constrain purpose of function
*   Forces developers to consistently think about requirements