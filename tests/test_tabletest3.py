import unittest

import tabletest3


class TableTestCaseExample(tabletest3.TableTestCase):
    """An example table test case, with three test cases."""
    TEST_CASES = ['A', 'B', 'C']

    def tabletest(self, test_case):
        self.assertEqual(test_case.upper(), test_case)


class TableTest(unittest.TestCase):
    def test_example_instance_has_three_methods(self):
        self.assertTrue('test_table_0' in dir(TableTestCaseExample))
        self.assertTrue('test_table_1' in dir(TableTestCaseExample))
        self.assertTrue('test_table_2' in dir(TableTestCaseExample))


if __name__ == '__main__':
    unittest.main()
