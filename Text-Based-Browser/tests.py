from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

import sys
if sys.platform.startswith("win"):
    import _locale
    # pylint: disable=protected-access
    _locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class TextBasedBrowserTest(StageTest):
    def generate(self):
        return [
            TestCase(
                stdin="bloomberg.com\nexit",
                attach=('Bloomberg', 'New York Times')
            ),
            TestCase(
                stdin="nytimes.com\nexit",
                attach=('New York Times', 'Bloomberg')
            ),
        ]

    def check(self, reply, attach):
        """
        Every fake-page contains magic word. Bloomberg fake-page must contain
        'Bloomberg' and New York Times fake page must contain 'New York Times'

        These test cases check assertions above.
        """
        right_word, wrong_word = attach

        if wrong_word in reply:
            return CheckResult.wrong('It seems like you printed wrong variable')

        if right_word in reply:
            return CheckResult.correct()

        return CheckResult.wrong('You printed neither bloomberg_com nor nytimes_com')


TextBasedBrowserTest('browser.browser').run_tests()
