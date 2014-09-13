# Which Challenges are suitable for which Test Framework?


| Challenge | unittest | nose | py.test |
|-----------|----------|------|---------|
| **1. Unit Tests** | | | |
| 1.1 Test a Python function | X | X | X |
| 1.2 Test proves if code is broken | | | |
| 1.3 Code proves if tests are broken | | | |
| 1.4 Running multiple tests | | | |
| 1.5 Test border cases | | | |
| | | | |
| **2. Integration Tests** | | | |
| 2.1 Mock Objects | | | |
| | | | |
| **3. Acceptance Tests** | | | |
| 3.1 Test a command-line application | | | |
| 3.2 Test another command-line application | | | |
| 3.3 User Acceptance | | | |
| | | | |
| **4. Test Data** | | | |
| 4.1 A module with test data | | | |
| 4.2 Preparing tests with fixtures | + | + | + |
| 4.3 Sets of example data | | | |
| 4.4 Write a test with sample data | | | |
| 4.5 Import test data in multiple test packages | + | + | + |
| | | | |
| **5. Test Suites** | | | |
| 5.1 Test selection | | | |
| 5.2 Test collection | | | |
| 5.3 Integrate a test suite in a Python package | | | |
| | | | |
| **6. Test Coverage** | | | |
| 6.1 Calculate Test Coverage | | | |
| 6.2 Identify uncovered lines | | | |
| 6.3 Increase test coverage | | | |
| | | | |
| **7. Testing New Features** | | | |
| 7.1 Add new feature: special characters | | | |
| 7.2 Add new feature: ignore case | | | |
| 7.3 Add new feature: word separators | | | | |
