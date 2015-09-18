# TableTest3 [![Build Status](https://travis-ci.org/horia141/tabletest3.svg)](https://travis-ci.org/horia141/tabletest3) #

Unit testing module for table-like test, for Python 3.

For Python 2, check out [TableTest](https://github.com/horia141/tabletest).

Many unit tests, especially those for side-effect free functions, can be written like this:

```python
import unittest
class FooTest(unittest.TestCase):
  TEST_CASES = [ case_1, case_2, ... ]
  def test_all(self):
    for test_case in TEST_CASES:
      do something with test_case
```

If there are many test cases, they'll all appear as a single unit test in test runners. Furthermore,
the failure of one test will cause all others to fail. Finally, it might be hard to identify which
of the tests actually fail.

TableTest3 aims to solve this problem. Using it, we can rewrite the previous example as:

```python
import tabletest
class FooTest(tabletest3.TableTestCase):
  TEST_CASES = [ case_1, case_2, ... ]
  @tabletest3.tabletest(TEST_CASES)
  def test_all(self, test_case):
    do something with test_case
```

When the testrunner will run this class, it will now find one test for each test case. Each test
will basically invoke `tabletest` with a single test case.

The setup functions like this:
* You must define a `TEST_CASE` class variable which can be iterated as a sequence.
* You must define a single argumet test function which does the testing required for each
  test case.
* Each element of `TEST_CASE` generates a test function, called `test_all_{xx}`, for the previous
  example.
* Iteration order is not guaranteed and should not be depended on.
* All other `unittest.TestCase` behavior remains intact: `setUp` and `tearDown` methods, other test
  methods etc.
* More than one test can be annotated with tabletests per test case.
* However, the name must starst with `test_`, so it is picked up by the runner.

## Installation ##

Installation is straightforward, via `pip`:

```bash
pip install tabletest3
```

## Development ##

Working on this project is pretty much standard Python development. Perhaps the most novel aspect is the usage of the [Bazel][bazel] build system. At the moment, only a `py_library` and a `py_test` are defined as build rules. Nevertheless, tests are run through [Bazel][bazel] rather than through regular invocation. To run the tests use:

```bash
bazel test //:tabletest3_test
```

To push a new version of the package to PyPi use:

```bash
bazel run //:tabletest3_upload -- --user=[pypi user] --pass=[pypi password]
```

## References ##

See [Tabletests][tabletests] and [How Tabletest Works][how-tabletest-works] for a longer introduction as well as a deep dive into the library.

[tabletests]: https://horia141.github.com/jekyll/update/2015/08/31/tabletests.html
[how-tabletest-works]: https://horia141.github.com/jekyll/update/2015/09/08/how-tabletest-works.html
[bazel]: http://bazel.io