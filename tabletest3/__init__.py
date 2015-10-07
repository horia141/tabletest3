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
  @tabletest3.tabletest(TEST_CASES)
  def test_all(self, test_case):
    do something with test_case

When the testrunner will run this class, it will now find one test for each test case. Each test
will basically invoke tabletest with a single test case.

The setup functions like this:
* You must define a TEST_CASE class variable which can be iterated as a sequence.
* You must define a single argument test function which does the testing required for each
  test case.
* Each element of TEST_CASE generates a test function, called test_all_{xx}, for the previous
  example.
* Iteration order is not guaranteed and should not be depended on.
* All other unittest.TestCase behavior remains intact: setUp and tearDown methods, other test
  methods etc.
* More than one test can be annotated with tabletests per test case.
* However, the name must starst with "test_", so it is picked up by the runner.
"""
import unittest

class TableTestMetaclass(type):
    """Metaclass used for generating test methods from each test case.

    Useful for when a testcase can't be inherited from TableTestCase.
    """
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        for name, attr in attrs.items():
            if hasattr(attr, '__call__') and hasattr(attr, '_is_tabletest'):
                test_idx = 0
                for test_case in attr._test_cases:
                    test_name = '{0}_{1}'.format(name, test_idx)
                    if test_name in new_attrs:
                        raise Exception('Name "{0}" is already used'.format(test_name))
                    new_attrs[test_name] = \
                        lambda self, attr=attr, test_case=test_case: attr(self, test_case)
                    test_idx += 1
            else:
                new_attrs[name] = attr

        return type.__new__(cls, name, bases, new_attrs)


class TableTestCase(unittest.TestCase,metaclass=TableTestMetaclass):
    """Base class for table-like test cases."""
    __metaclass__ = TableTestMetaclass


class tabletest(object):
    """Annotation for marking test methods as table tests."""
    def __init__(self, test_cases):
        self._test_cases = iter(test_cases)

    def __call__(self, tester_fn):
        tester_fn._is_tabletest = True
        tester_fn._test_cases = self._test_cases
        return tester_fn
