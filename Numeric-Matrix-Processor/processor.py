exit_flg = False
user_choice = None


def print_menu_get_option():
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    return int(input("Your choice: "))


def get_matrix_float(rows, cols):
    matrix_float = []
    for i in range(rows):
        row = input().split()
        matrix_float.append([])
        for j in range(cols):
            matrix_float[i].append(float(row[j]))
    return matrix_float


def add_matrices():
    matrix1_size = input("Enter size of first matrix: ").split()
    num1_rows, num1_cols = int(matrix1_size[0]), int(matrix1_size[1])
    print("Enter first matrix:")
    matrix1 = get_matrix_float(num1_rows, num1_cols)
    matrix2_size = input("Enter size of second matrix: ").split()
    print("Enter second matrix:")
    num2_rows, num2_cols = int(matrix2_size[0]), int(matrix2_size[1])
    matrix2 = get_matrix_float(num2_rows, num2_cols)
    if matrix1_size == matrix2_size:
        matrix_sum = []
        for i in range(num1_rows):
            matrix_sum.append([])
            for j in range(num1_cols):
                matrix_sum[i].append(matrix1[i][j] + matrix2[i][j])
        return matrix_sum
    else:
        print("Impossible!")
        return []


def multiply_by_constant():
    matrix_size = input("Enter size of matrix: ").split()
    num_rows, num_cols = int(matrix_size[0]), int(matrix_size[1])
    print("Enter matrix:")
    matrix__ = get_matrix_float(num_rows, num_cols)
    constant = float(input("Enter constant: "))
    matrix_multiply_const = []
    for i in range(num_rows):
        matrix_multiply_const.append([])
        for j in range(num_cols):
            matrix_multiply_const[i].append(matrix__[i][j] * constant)
    return matrix_multiply_const


def ele_ij(num_cols, i, j, matrix1, matrix2):
    sum_multiply = 0
    for k in range(num_cols):
        sum_multiply += matrix1[i][k] * matrix2[k][j]
    return sum_multiply


def multiply_matrices():
    matrix1_size = input("Enter size of first matrix: ").split()
    num1_rows, num1_cols = int(matrix1_size[0]), int(matrix1_size[1])
    print("Enter first matrix:")
    matrix1 = get_matrix_float(num1_rows, num1_cols)
    matrix2_size = input("Enter size of first matrix: ").split()
    num2_rows, num2_cols = int(matrix2_size[0]), int(matrix2_size[1])
    print("Enter second matrix:")
    matrix2 = get_matrix_float(num2_rows, num2_cols)
    if num1_cols == num2_rows:
        matrix_multiply = []
        for i in range(num1_rows):
            matrix_multiply.append([])
            for j in range(num2_cols):
                matrix_multiply[i].append(ele_ij(num1_cols, i, j, matrix1, matrix2))
        return matrix_multiply
    else:
        print("Impossible!")
        return []


def print_result(matrix_):
    print("The result is:")
    for row in matrix_:
        for ele in row:
            print(ele, end=" ")
        print()


def calculate_determinant(matrix, num_rows, num_cols):
    if num_rows == num_cols == 1:
        return matrix[0][0]
    elif num_rows == num_cols == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif num_rows > 2 and num_cols > 2:
        determ = 0
        for i in range(num_cols):
            minor = [[matrix[k][j] for j in range(num_cols) if j != i] for k in range(1, num_rows)]
            determ += matrix[0][i] * calculate_determinant(minor, num_rows - 1, num_cols - 1) * (-1) ** (2 + i)
        return determ


class Matrix:
    def __init__(self, matrix_dim):
        self.matrix_size = matrix_dim.split()
        self.num_rows, self.num_cols = int(self.matrix_size[0]), int(self.matrix_size[1])
        self.matrix = None
        self.matrix_transpose_main = None
        self.matrix_transpose_side = None
        self.matrix_transpose_vertical = None
        self.matrix_transpose_horizontal = None
        self.cofactor_mat = None

    def construct_matrix(self):
        self.matrix = []
        print("Enter matrix:")
        for i in range(self.num_rows):
            row = input().split()
            self.matrix.append([])
            for j in range(self.num_cols):
                self.matrix[i].append(float(row[j]))

    def transpose_main(self):
        self.matrix_transpose_main = []
        for i in range(self.num_cols):
            self.matrix_transpose_main.append([])
            for j in range(self.num_rows):
                self.matrix_transpose_main[i].append(self.matrix[j][i])
        # return  self.matrix_transpose_main

    def transpose_side(self):
        self.matrix_transpose_side = []
        for i in range(self.num_cols):
            self.matrix_transpose_side.append([])
            for j in range(self.num_rows):
                self.matrix_transpose_side[i].append(self.matrix[-1 - j][-1 - i])

    def transpose_vertical(self):
        self.matrix_transpose_vertical = []
        for i in range(self.num_rows):
            self.matrix_transpose_vertical.append([])
            for j in range(self.num_cols):
                self.matrix_transpose_vertical[i].append(self.matrix[i][self.num_cols - 1 - j])

    def transpose_horizontal(self):
        self.matrix_transpose_horizontal = []
        for i in range(self.num_rows):
            self.matrix_transpose_horizontal.append([])
            for j in range(self.num_cols):
                self.matrix_transpose_horizontal[i].append(self.matrix[self.num_rows - 1 - i][j])

    def cofactor_matrix(self):
        self.cofactor_mat = []
        for i in range(self.num_rows):
            self.cofactor_mat.append([])
            for j in range(self.num_cols):
                mat_re = [[self.matrix[p][q] for q in range(self.num_cols) if q != j] for p in range(self.num_rows) if
                          p != i]
                self.cofactor_mat[i].append((-1) ** (2 + i + j) * calculate_determinant(mat_re, self.num_rows - 1,
                                                                                    self.num_cols - 1))


while not exit_flg:
    user_choice = print_menu_get_option()
    if user_choice == 1:
        result = add_matrices()
        print_result(result)
    elif user_choice == 2:
        result = multiply_by_constant()
        print_result(result)
    elif user_choice == 3:
        result = multiply_matrices()
        print_result(result)
    elif user_choice == 0:
        exit_flg = True
    elif user_choice == 4:
        print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4.Horizontal line")
        transpose_option = int(input("Your choice: "))
        if transpose_option == 1:
            matrix_to = Matrix(input("Enter matrix size: "))
            matrix_to.construct_matrix()
            matrix_to.transpose_main()
            print_result(matrix_to.matrix_transpose_main)
        elif transpose_option == 2:
            matrix_to = Matrix(input("Enter matrix size: "))
            matrix_to.construct_matrix()
            matrix_to.transpose_side()
            print_result(matrix_to.matrix_transpose_side)
        elif transpose_option == 3:
            matrix_to = Matrix(input("Enter matrix size: "))
            matrix_to.construct_matrix()
            matrix_to.transpose_vertical()
            print_result(matrix_to.matrix_transpose_vertical)
        elif transpose_option == 4:
            matrix_to = Matrix(input("Enter matrix size: "))
            matrix_to.construct_matrix()
            matrix_to.transpose_horizontal()
            print_result(matrix_to.matrix_transpose_horizontal)
        else:
            print("Impossible")
            pass
    elif user_choice == 5:
        matrix_to = Matrix(input("Enter matrix size: "))
        matrix_to.construct_matrix()
        if matrix_to.num_rows != matrix_to.num_cols:
            print("Impossible!")
        else:
            determinant = calculate_determinant(matrix_to.matrix, matrix_to.num_rows, matrix_to.num_cols)
            if determinant % 1 == 0:
                int(determinant)
            print("The result is:\n{}".format(determinant))
    elif user_choice == 6:
        matrix_dim = input("Enter matrix size: ")
        matrix_to = Matrix(matrix_dim)
        matrix_to.construct_matrix()
        if matrix_to.num_rows != matrix_to.num_cols:
            print("Impossible!")
        else:
            if matrix_to.num_rows < 2 and matrix_to.matrix[0][0] != 0:
                print("The result is:")
                print(round(1 / matrix_to.matrix[0][0], 2))
            else:
                if calculate_determinant(matrix_to.matrix, matrix_to.num_rows, matrix_to.num_cols) == 0:
                    print("This matrix doesn't have an inverse")
                else:
                    matrix_to.cofactor_matrix()
                    cofactor_mat = matrix_to.cofactor_mat
                    det_main = calculate_determinant(matrix_to.matrix, matrix_to.num_rows, matrix_to.num_cols)
                    mat_inverse = []
                    for i in range(len(cofactor_mat)):
                        mat_inverse.append([])
                        for j in range(len(cofactor_mat[0])):
                            mat_inverse[i].append(round(cofactor_mat[j][i] / det_main, 4))
                    print_result(mat_inverse)