import unittest

import tabletest3


class TableTestCaseExample(tabletest3.TableTestCase):
    """An example table test case, with three test cases."""
    TEST_CASES = ['A', 'B', 'C']

    SEEN = set()

    @tabletest3.tabletest(TEST_CASES)
    def test_basic(self, test_case):
        self.assertEqual(test_case.upper(), test_case)
        TableTestCaseExample.SEEN.add(test_case)


class TableTestCaseExampleTwoTables(tabletest3.TableTestCase):
    """An example table test case, with two table tests."""
    TEST_CASES_1 = ['A', 'B', 'C']
    SEEN_1 = set()

    @tabletest3.tabletest(TEST_CASES_1)
    def test_first(self, test_case):
        self.assertEqual(test_case.upper(), test_case)
        TableTestCaseExampleTwoTables.SEEN_1.add(test_case)

    TEST_CASES_2 = ['1', '2', '3', '4']
    SEEN_2 = set()

    @tabletest3.tabletest(TEST_CASES_2)
    def test_second(self, test_case):
        TableTestCaseExampleTwoTables.SEEN_2.add(int(test_case))


class TableTestCaseExampleExtra(tabletest3.TableTestCase):
    """An example table test case, with setUp and tearDown methods."""

    SEEN = set()

    def setUp(self):
        TableTestCaseExampleExtra.SEEN.add(-1)

    def tearDown(self):
        TableTestCaseExampleExtra.SEEN.add(-2)

    @tabletest3.tabletest([1, 2, 3])
    def test_basic(self, test_case):
        TableTestCaseExampleExtra.SEEN.add(test_case)


class TableTest(unittest.TestCase):
    def test_example_has_three_methods(self):
        self.assertTrue('test_basic_0' in dir(TableTestCaseExample))
        self.assertTrue('test_basic_1' in dir(TableTestCaseExample))
        self.assertTrue('test_basic_2' in dir(TableTestCaseExample))

    def test_example_has_proper_metadata(self):
        example = TableTestCaseExample('test_basic_0')
        example.run()
        self.assertEqual(example.SEEN, set(['A']))

        example = TableTestCaseExample('test_basic_1')
        example.run()
        self.assertEqual(example.SEEN, set(['A', 'B']))

        example = TableTestCaseExample('test_basic_2')
        example.run()
        self.assertEqual(example.SEEN, set(['A', 'B', 'C']))

    def test_example_two_tables_has_seven_methods(self):
        self.assertTrue('test_first_0' in dir(TableTestCaseExampleTwoTables))
        self.assertTrue('test_first_1' in dir(TableTestCaseExampleTwoTables))
        self.assertTrue('test_first_2' in dir(TableTestCaseExampleTwoTables))
        self.assertTrue('test_second_0' in dir(TableTestCaseExampleTwoTables))
        self.assertTrue('test_second_1' in dir(TableTestCaseExampleTwoTables))
        self.assertTrue('test_second_2' in dir(TableTestCaseExampleTwoTables))
        self.assertTrue('test_second_3' in dir(TableTestCaseExampleTwoTables))

    def test_example_two_tables_has_proper_metadata(self):
        example = TableTestCaseExampleTwoTables('test_first_0')
        example.run()
        self.assertEqual(example.SEEN_1, set(['A']))

        example = TableTestCaseExampleTwoTables('test_first_1')
        example.run()
        self.assertEqual(example.SEEN_1, set(['A', 'B']))

        example = TableTestCaseExampleTwoTables('test_first_2')
        example.run()
        self.assertEqual(example.SEEN_1, set(['A', 'B', 'C']))

        example = TableTestCaseExampleTwoTables('test_second_0')
        example.run()
        self.assertEqual(example.SEEN_2, set([1]))

        example = TableTestCaseExampleTwoTables('test_second_1')
        example.run()
        self.assertEqual(example.SEEN_2, set([1, 2]))

        example = TableTestCaseExampleTwoTables('test_second_2')
        example.run()
        self.assertEqual(example.SEEN_2, set([1, 2, 3]))

        example = TableTestCaseExampleTwoTables('test_second_3')
        example.run()
        self.assertEqual(example.SEEN_2, set([1, 2, 3, 4]))

    def test_setup_teardown(self):
        example = TableTestCaseExampleExtra('test_basic_0')
        example.run()
        self.assertEqual(example.SEEN, set([-1, -2, 1]))


if __name__ == '__main__':
    unittest.main()
