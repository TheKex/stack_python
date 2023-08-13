import unittest
from stack import check_brackets


class TestBrackets(unittest.TestCase):
    def test_check_brackets(self):
        test_cases = [
            ('(((([{}]))))', True),
            ('(((([}{]))))', False),
            ('[([])((([[[]]])))]{()}', True),
            ('{{[()]}}', True),
            ('}{}', False),
            ('{{[(])]}}', False),
            ('[[{())}]', False)
        ]
        for test in test_cases:
            with self.subTest(f'brackets - "{test[0]}"'):
                self.assertEqual(check_brackets(test[0]), test[1])

