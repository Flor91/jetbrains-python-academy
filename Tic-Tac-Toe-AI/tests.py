from hstest.stage_test import *
from hstest.test_case import TestCase
from enum import Enum
from typing import List, Optional
from copy import deepcopy

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class FieldState(Enum):
    X = 'X'
    O = 'O'
    FREE = ' '


def get_state(symbol):
    if symbol == 'X':
        return FieldState.X
    elif symbol == 'O':
        return FieldState.O
    elif symbol == ' ' or symbol == '_':
        return FieldState.FREE
    else:
        return None


class TicTacToeField:

    def __init__(self, *, field: str = '', constructed=None):

        if constructed is not None:
            self.field = deepcopy(constructed)

        else:
            self.field: List[List[Optional[FieldState]]] = [
                [None for _ in range(3)] for _ in range(3)
            ]

            field = field.replace("\"", "")

            for row in range(3):
                for col in range(3):
                    index = (2 - row) * 3 + col
                    self.field[row][col] = get_state(field[index])

    def equal_to(self, other) -> bool:
        for i in range(3):
            for j in range(3):
                if self.field[i][j] != other.field[i][j]:
                    return False
        return True

    def has_next_as(self, other) -> bool:
        improved: bool = False
        for i in range(3):
            for j in range(3):
                if self.field[i][j] != other.field[i][j]:
                    if self.field[i][j] == FieldState.FREE and not improved:
                        improved = True
                    else:
                        return False
        return improved

    def differ_by_one(self, other) -> bool:
        have_single_difference = False
        for i in range(3):
            for j in range(3):
                if self.field[i][j] != other.field[i][j]:
                    if have_single_difference:
                        return False
                    have_single_difference = True
        return have_single_difference

    def is_close_to(self, other) -> bool:
        return (
            self.equal_to(other)
            or self.has_next_as(other)
            or other.has_next_as(self)
        )

    @staticmethod
    def parse(field_str: str):

        lines = field_str.splitlines()
        lines = [i.strip() for i in lines]
        lines = [i for i in lines if
                 i.startswith('|') and i.endswith('|')]

        for line in lines:
            if len(line) != 9:
                raise WrongAnswerException(
                    f"Line of Tic-Tac-Toe field should be 9 characters long\n"
                    f"found {len(line)} characters in \"{line}\"")
            for c in line:
                if c not in 'XO|_ ':
                    return None

        field: List[List[Optional[FieldState]]] = [
            [None for _ in range(3)] for _ in range(3)
        ]

        y: int = 2

        for line in lines:
            cols = line[2], line[4], line[6]
            x: int = 0
            for c in cols:
                state = get_state(c)
                if state is None:
                    return None
                field[y][x] = state
                x += 1
            y -= 1

        return TicTacToeField(constructed=field)

    @staticmethod
    def parse_all(output: str):
        fields = []

        lines = output.splitlines()
        lines = [i.strip() for i in lines]
        lines = [i for i in lines if len(i) > 0]

        candidate_field = ''
        inside_field = False
        for line in lines:
            if '----' in line and not inside_field:
                inside_field = True
                candidate_field = ''
            elif '----' in line and inside_field:
                field = TicTacToeField.parse(candidate_field)
                if field is not None:
                    fields += [field]
                inside_field = False

            if inside_field and line.startswith('|'):
                candidate_field += line + '\n'

        return fields


inputs = [
    "1 1", "1 2", "1 3",
    "2 1", "2 2", "2 3",
    "3 1", "3 2", "3 3"
]


def iterate_cells(initial: str) -> str:
    index: int = -1
    for i in range(len(inputs)):
        if initial == inputs[i]:
            index = i
            break

    if index == -1:
        return ''

    full_input: str = ''
    for i in range(index, index + 9):
        full_input += inputs[i % len(inputs)] + '\n'

    return full_input


class TicTacToeTest(StageTest):
    def generate(self) -> List[TestCase]:
        tests: List[TestCase] = []

        i: int = 0
        for input in inputs:
            full_move_input = iterate_cells(input)

            str_nums = input.split()
            x = int(str_nums[0])
            y = int(str_nums[1])

            if i % 2 == 1:
                full_move_input = f'4 {i}\n' + full_move_input

            full_game_input = ''
            for _ in range(9):
                full_game_input += full_move_input

            if i % 6 == 0:
                initial = "start user easy\n"
            elif i % 6 == 1:
                initial = "start easy user\n"
            elif i % 6 == 2:
                initial = "start user medium\n"
            elif i % 6 == 3:
                initial = "start medium user\n"
            elif i % 6 == 4:
                initial = "start user hard\n"
            else:
                initial = "start hard user\n"

            full_game_input = initial + full_game_input + "exit"

            tests += [TestCase(stdin=full_game_input)]

            i += 1

        tests += [
            TestCase(stdin="start easy easy\nexit"),
            TestCase(stdin="start medium medium\nexit"),
            TestCase(stdin="start hard hard\nexit"),

            TestCase(stdin="start medium easy\nexit"),
            TestCase(stdin="start easy medium\nexit"),

            TestCase(stdin="start medium hard\nexit"),
            TestCase(stdin="start hard medium\nexit"),

            TestCase(stdin="start easy hard\nexit"),
            TestCase(stdin="start hard easy\nexit"),

            TestCase(stdin=
                     "start user user\n" +
                     "1 1\n" +
                     "2 2\n" +
                     "1 2\n" +
                     "2 1\n" +
                     "1 3\n" +
                     "exit"),
        ]

        return tests

    def check(self, reply: str, attach: str) -> CheckResult:

        fields = TicTacToeField.parse_all(reply)

        if len(fields) == 0:
            return CheckResult.wrong(
                "No fields found"
            )

        for i in range(1, len(fields)):
            curr: TicTacToeField = fields[i - 1]
            next: TicTacToeField = fields[i]

            stayed = curr.equal_to(next)
            improved = curr.has_next_as(next)

            if not (stayed or improved):
                return CheckResult.wrong(
                    "For two fields following each " +
                    "other one is not a continuation " +
                    "of the other (they differ more than in two places)."
                )

        return CheckResult.correct()


if __name__ == '__main__':
    TicTacToeTest('tictactoe.tictactoe').run_tests()
