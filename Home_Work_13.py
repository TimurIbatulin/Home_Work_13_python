# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
# Напишите к ним классы исключения с выводом подробной информации. 
# Поднимайте исключения внутри основного кода. 
# Например нельзя создавать прямоугольник со сторонами отрицательной длины

def sum_matrix(matrix_1: list, matrix_2: list):
    answer_matrix = []
    insait_string = []
    try:
        for i in range (len(matrix_2)):
            for i_2 in range(len(matrix_2[i])):
                insait_string.append(matrix_1[i][i_2] + matrix_2[i][i_2])
        answer_matrix.append(insait_string)
        insait_string = []
    except IndexError  as e:
        print(f'Ошибка {e}, Вероятно разный размер матриц. При сложении матрицы должны быть одного размера')     
    return answer_matrix

def mul_matrix(matrix_1: list, matrix_2: list):
    temporarily_list = []
    ans_list = []
    temp = 0
    temp_1 = 0
    
    try:
        for i in range(len(matrix_1)):
            count = 0
            for _ in range(len(matrix_1)):
                for k in range(len(matrix_1[0])):
                    temp = matrix_1[i][k] * matrix_2[k][count]
                    temp_1 += temp
                temporarily_list.append(temp_1)
                count += 1
                temp_1 = 0
                temp = 0
            ans_list.append(temporarily_list)
            temporarily_list = []
        return ans_list
    except IndexError as e:
        print(f'Ошибка {e}, Вероятно разный размер матриц. При умножении количество строк одной матрицы должно соответствовать количеству столбцов другой')




class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix
    
    def __eq__(self, other):
        return self == other
    
    def __add__(self, other):
        return Matrix(sum_matrix(self.matrix, other.matrix))
    
    def __mul__(self, other):
        return Matrix(mul_matrix(self.matrix, other.matrix))
    
    def __repr__(self):
        return f'{self.matrix}'


if __name__ == '__main__':
    z_1 = [[2, 1], [-3, 0], [4, -1]]
    z_2 = [[5, -1, 6],[-3, 0, 3]]
    z_3 = [[2, 1], [-3, 0], [4, -1]]

    m_1 = Matrix(z_1)
    m_2 = Matrix(z_2)
    m_5 = Matrix(z_3)
    
    m_3 = m_1 + m_5
    m_33 = m_1 + m_2

    m_4 = m_1 * m_2
    print(f'{m_3 = } ')
    print(f'{m_33 = } ')
    print(f'{m_4 = } ')
