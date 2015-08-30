import unittest

import tabletest3


class TableTestCaseExample(tabletest3.TableTestCase):
    """An example table test case, with three test cases."""
    TEST_CASES = ['A', 'B', 'C']

    SEEN = set()

    def tabletest(self, test_case):
        self.assertEqual(test_case.upper(), test_case)
        TableTestCaseExample.SEEN.add(test_case)


class TableTest(unittest.TestCase):
    def test_example_has_three_methods(self):
        self.assertTrue('test_table_0' in dir(TableTestCaseExample))
        self.assertTrue('test_table_1' in dir(TableTestCaseExample))
        self.assertTrue('test_table_2' in dir(TableTestCaseExample))

    def test_example_has_proper_metadata(self):
        example = TableTestCaseExample('test_table_0')
        example.run()
        self.assertEqual(example.SEEN, set(['A']))

        example = TableTestCaseExample('test_table_1')
        example.run()
        self.assertEqual(example.SEEN, set(['A', 'B']))

        example = TableTestCaseExample('test_table_2')
        example.run()
        self.assertEqual(example.SEEN, set(['A', 'B', 'C']))


if __name__ == '__main__':
    unittest.main()
