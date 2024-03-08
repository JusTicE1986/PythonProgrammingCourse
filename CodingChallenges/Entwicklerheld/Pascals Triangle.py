from math import factorial
def get_pascals_triangle_row(row_number: int) -> list:
    # Implement me
    # 1. Anzahl der Reihen == Anzahl der Elemente in der Reihe
    # 2. for row in row_number:
    pascals_triangle = []
    for i in range(row_number+1):
        #for j in range(row_number - i+1):
            #print(end=" ")

        for j in range(i+1):
            pascals_triangle.append(factorial(i)//(factorial(j)*factorial(i-j)))

    if len(pascals_triangle) == 0:
        return [1]
    else:
        return pascals_triangle[-row_number-1:]

print(get_pascals_triangle_row(1))