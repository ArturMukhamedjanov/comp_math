import input
import itertools

def permute_columns(A, cols, depth, n):
        if depth == n:
            # Создаем новую матрицу с переставленными столбцами
            new_matrix = [[row[i] for i in cols] for row in A]
            return new_matrix
        permutations = []
        for i in range(n):
            if i not in cols:
                # Вызываем рекурсивно для следующего столбца
                new_cols = cols + [i]
                permutations.extend(permute_columns(A, new_cols, depth + 1, n))
        return permutations

def check_matrix_diag(matrix, n):
    good = True
    strict = False
    for i in range(n):
        sum = 0
        for j in range(n):
            if(i != j):
                sum+=matrix[i][j]
        if sum > matrix[i][i]:
            good = False
            break
        if sum < matrix[i][i]:
            strict = True
    if(strict and good):
        return True
    return False

def decompose_matrix(matrix, n):
    A = []
    B = []
    for i in range(n):
        A.append(matrix[i][:n])
        B.append(matrix[i][n])
    return A,B

def sort_diagram(A, B, n):
    full_matrix = []
    for i in range(n):
        s = A[i]
        s.append(B[i])
        full_matrix.append(s)   
    if check_matrix_diag(full_matrix, n):
        return A, B
    permuntations = itertools.permutations(A)
    for matrix in permuntations:
        if check_matrix_diag(matrix, n):
            return decompose_matrix(matrix, n)
    print("Невозможно составить матрицу c диагональным преобладанием!!! Возможномть несходимость Слау")
    return A, B

def make_c_matrix(A, n):
    result_matrix = []
    for i in range(n):
        dummy = []
        for j in range(n):
            if(i == j):
                dummy.append(0)
            else:
                dummy.append( -A[i][j]/ A[i][i])
        result_matrix.append(dummy)
    return result_matrix

def make_d_matrix(A, B, n):
    result_matrix = []
    for i in range(n):
        result_matrix.append(B[i]/A[i][i])
    return result_matrix

def sort_diag_arr(a, b) :
    n = len(a)
    for i in range(n):
        ind, a[i:] = zip(*sorted(enumerate(a[i:]),
                             key=lambda x: -x[1][i]))
        b[i:] = [b[i+j] for j in ind]
    
    return a, b

def iterational_method(C, D,result_matrix, accuracy, n, iteration_counter, A, B):
    new_answers = []
    max_deviation = 0
    for i in range(n):
        temp = 0
        for j in range(len(C)):
            if(i == j):
                temp += D[j]
            else:
                temp += C[i][j] * result_matrix[iteration_counter][j]
        new_answers.append(temp)
        if(max_deviation < abs(result_matrix[iteration_counter][i] - temp)):
            max_deviation = abs(result_matrix[iteration_counter][i] - temp)
    #new_answers.append(max_deviation)
    max_deviation = max(count_residual(new_answers, A,B))
    new_answers.append(max(count_residual(new_answers, A,B)))
    print(new_answers)
    result_matrix.append(new_answers)
    if(max_deviation < accuracy):
        return result_matrix
    else:
        if(iteration_counter == 100):
            print("Количсетво итераций достигло максимума (100).")
            return result_matrix
        return iterational_method(C,D, result_matrix, accuracy, n, iteration_counter + 1, A, B)

def count_residual(answer_matrix, A, B):
    residual_arr = []
    for i in range(n):
        calc_ans = 0
        for j in range(n):
            calc_ans += A[i][j] * answer_matrix[j]
        residual_arr.append(abs(calc_ans - B[i]))
    return residual_arr
    

n = input.enter_demension()
accuracy = input.enter_accuracy()
A,B = input.enter_matrix(n)
#A, B = sort_diagram(A, B, n)
temp_A,temp_B = sort_diag_arr(A, B)
if(check_matrix_diag(temp_A, n)):
    A,B = temp_A, temp_B
else:
    print("Невозможно составить матрицу c диагональным преобладанием!!! Возможномть несходимость Слау")
print(A, B)
C = make_c_matrix(A, n)
D = make_d_matrix(A, B, n)
temp_d = []
for i in range(n):
    temp_d.append(100)
temp_d.append(None)
result_matrix = []
result_matrix.append(temp_d)
result_matrix = iterational_method(C,D, result_matrix, accuracy, n, 0, A, B)
print(len(result_matrix))
answer_matrix = result_matrix[len(result_matrix)- 1][:len(result_matrix[0]) - 1]
print(answer_matrix)
residual_arr = count_residual(answer_matrix, A,B)
print(residual_arr)