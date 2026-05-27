# Python Test Readability Guidelines

## 1. Naming Conventions ##
- **Descriptive Names**: Test names should clearly state the scenario and expected outcome (e.g., `test_calculate_total_returns_zero_for_empty_input` instead of `test_total_1`).
- **Variables**: Use meaningful variable names. Avoid single-letter variables like `x` or `t` unless iterating in a short loop.
- **SUT (System Under Test)**: Naming the object being tested `sut` or `model` is acceptable if it improves clarity, but specific names are often better.

## 2. Structure (AAA Pattern) ##
- **Arrange**: Set up the initial state (objects, variables, database records).
- **Act**: Invoke the method or function under test.
- **Assert**: Verify the result.
- **Visual Separation**: Use blank lines to separate these three usage phases.

## 3. Assertions ##
- **One Concept per Test**: A test should verify one logical concept. Multiple assertions are fine if they check different aspects of the same result.
- **Appropriate Assertions**: Use specific assertions (e.g., `assert list is empty` via `assert not list`) rather than generic checks.
- **No Logic in Tests**: Avoid control structures (loops, if/else) in test code; tests should be linear.

## 4. Setup and Teardown ##
- **Use Fixtures**: Use `pytest.fixtures` for common setup code to reduce duplication.
- **Clean Scope**: Ensure tests do not rely on side effects from other tests.

## 5. Simplicity ##
- **Reduce Cognitive Load**: The test code should be obvious. If you have to read it twice to understand what it tests, it is too complex.
- **Helpers**: Extract complex setup data generation into helper functions, but keep the *logic* of the test visible in the test function.
