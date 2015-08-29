"""Unit testing module for table-like test.

Many unit tests, especially those for side-effect free functions, can be written like this:

import unittest
class FooTest(unittest.TestCase):
  TEST_CASES = [ case_1, case_2, ... ]
  def test_all(self):
    for test_case in TEST_CASES:
      do something with test_case

If there are many test cases, they'll all appear as a single unit test in test runners. Furthermore,
the failure of one test will cause all others to fail. Finally, it might be hard to identify which
of the tests actually fail.

TableTest3 aims to solve this problem. Using it, we can rewrite the previous example as:

import tabletest3
class FooTest(tabletest3.TableTestCase):
  TEST_CASES = [ case_1, case_2, ... ]
  def tabletest(self, test_case):
    do something with test_case

When the testrunner will run this class, it will now find one test for each test case. Each test
will basically invoke tabletest with a single test case.

The setup functions like this:
* You must define a TEST_CASE class variable which can be iterated as a sequence.
* You must define a single argumet tabletest function which does the testing required for each
  test case.
* Each element of TEST_CASE generates a test function, called test_table_{xx}.
* Iteration order is not guaranteed and should not be depended on.
* All other unittest.TestCase behavior remains intact: setUp and tearDown methods, other test
  methods etc.
* Only a single TEST_CASES sequence and tabletest function can exist per case.
"""
import unittest

class TableTestMetaclass(type):
    """Metaclass used for generating test methods from each test case.

    Useful for when a testcase can't be inherited from TableTestCase.
    """
    def __new__(cls, name, bases, attrs):
        test_idx = 0
        for test_case in attrs['TEST_CASES']:
            attrs['test_table_{0}'.format(test_idx)] = lambda self: self.tabletest(test_case)
            test_idx += 1

        return type.__new__(cls, name, bases, attrs)


class TableTestCase(unittest.TestCase,metaclass=TableTestMetaclass):
    """Base class for table-like test cases."""

    TEST_CASES = []

    def tabletest(self, test_case):
        """Unittest applied to each test case."""
        raise NotImplementedError()
