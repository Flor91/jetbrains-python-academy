from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
import re

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class CreditCalcTest(StageTest):
    def generate(self):
        return [
            TestCase(
                args=[
                    '--type=annuity',
                    '--payment=8722',
                    '--periods=120',
                    '--interest=5.6',
                ],
                attach=('principal', 800018, 246622),
            ),
            TestCase(
                args=[
                    '--type=annuity',
                    '--payment=6898',
                    '--periods=240',
                    '--interest=3.4',
                ],
                attach=('principal', 1199997, 455523),
            ),

            TestCase(
                args=[
                    '--type=annuity',
                    '--principal=1000000',
                    '--periods=8',
                    '--interest=9.8',
                ],
                attach=('payment', 129638, 37104),
            ),

            TestCase(
                args=[
                    '--type=annuity',
                    '--principal=1000000',
                    '--periods=60',
                    '--interest=10',
                ],
                attach=('payment', 274880, 21248),
            ),

            TestCase(
                args=[
                    '--type=annuity',
                    '--principal=500000',
                    '--payment=23000',
                    '--interest=7.8',
                ],
                attach=('periods', 52000, 24),
            ),

            TestCase(
                args=[
                    '--type=diff',
                    '--principal=1000000',
                    '--periods=10',
                    '--interest=10',
                ],
                attach=[
                    108334,
                    107500,
                    106667,
                    105834,
                    105000,
                    104167,
                    103334,
                    102500,
                    101667,
                    100834,
                    45837,
                ],
            ),

            TestCase(
                args=[
                    '--type=diff',
                    '--principal=500000',
                    '--periods=8',
                    '--interest=7.8',
                ],
                attach=[
                    65750,
                    65344,
                    64938,
                    64532,
                    64125,
                    63719,
                    63313,
                    62907,
                    14628,
                ],
            ),

            TestCase(
                args=[
                    '--type=annuity',
                    '--principal=1000000',
                    '--payment=104000',
                ],
                attach='Incorrect',
            ),

            TestCase(
                args=[
                    '--type=diff',
                    '--principal=-1000000',
                    '--payment=104000',
                    '--periods=8',
                ],
                attach='Incorrect',
            ),

        ]

    def check(self, reply, attach):
        if attach == 'Incorrect':
            if attach.lower() in reply.lower():
                return CheckResult.correct()

            return CheckResult.wrong(
                'Parameters are incorrect. '
                'Just output "Incorrect parameters"'
            )

        numbers = re.findall(r'[-+]?(\d*\.\d+|\d+)', reply)
        if len(numbers) == 0:
            return CheckResult.wrong(
                'No numbers in the answer',
            )

        if isinstance(attach, tuple):
            if attach[0] == 'periods':
                years = int(attach[2] / 12)
                months = str(int(attach[2] % 12))
                for i in numbers:
                    if abs(attach[1] - float(i)) < 2:
                        if str(months) in numbers or str(years) in numbers:
                            return CheckResult.correct()

                if years == 0:
                    output = (
                        'Looks like your periods '
                        'calculations aren\'t working properly. '
                        'Correct months and overpayment are '
                        '[ {0}, {1} ]'
                        ', but you output: {2}'
                    )
                    return CheckResult.wrong(
                        output.format(attach[2], attach[1], numbers),
                    )
                else:
                    if months != '0':
                        output = (
                            'Looks like your periods '
                            'calculations aren\'t working properly. '
                            'Correct years, months and overpayment are '
                            '[ {0}, {1}, {2} ]'
                            ', but you output: {3}'
                        )
                        return CheckResult.wrong(
                            output.format(years, months, attach[1], numbers),
                        )
                    else:
                        output = (
                            'Looks like your periods '
                            'calculations aren\'t working properly. '
                            'Correct years and overpayment are '
                            '[ {0}, {1} ]'
                            ', but you output: {2}'
                        )
                        return CheckResult.wrong(
                            output.format(years, attach[1], numbers),
                        )
            for i in numbers:
                if not abs(attach[1] - float(i)) < 2:
                    if not abs(attach[2] - float(i)) < 2:
                        if attach[0] == 'payment':
                            output = (
                                'Looks like your annuity payments '
                                'calculations aren\'t working properly. '
                                'Correct annuity payment and overpayment are '
                                '[ {0}, {1} ]'
                                ', but you output: {2}'
                            )
                        else:
                            output = (
                                'Looks like your credit principal '
                                'calculations aren\'t working properly. '
                                'Correct credit principal and overpayment are '
                                '[ {0}, {1} ]'
                                ', but you output: {2}'
                            )
                        return CheckResult.wrong(
                            output.format(attach[2], attach[1], numbers),
                        )

            return CheckResult.correct()

        if isinstance(attach, list):
            if (len(numbers) + 1) / 2 < len(attach):
                user_numbers = numbers[1::2]
                if numbers[-1] not in user_numbers:
                    user_numbers.append(numbers[-1])
                return CheckResult.wrong(
                    'Not enough values for diff payment in the answer '
                    'must be {0} with overpayment {1}, but you output: {2}'
                    .format(attach[:-1], attach[-1], user_numbers)
                )

            for figure in attach:
                flag = False
                for number in numbers:
                    if abs(float(number) - figure) < 2:
                        flag = True
                        break
                if flag is False:
                    user_numbers = numbers[1::2]
                    if numbers[-1] not in user_numbers:
                        user_numbers.append(numbers[-1])
                    return CheckResult.wrong(
                        'Incorrect result '
                        'must be {0} with overpayment {1}, but you output: {2}'
                        .format(attach[:-1], attach[-1], user_numbers)
                    )

        return CheckResult.correct()


if __name__ == '__main__':
    CreditCalcTest('creditcalc.creditcalc').run_tests()
