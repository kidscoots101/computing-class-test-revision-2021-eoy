matrixA = [[1, 4, 3],
           [2, 5, 9]]
matrixB = [[1, 3, 3, 7],
           [2, 4, 6, 8],
           [2, 0, 2, 1]]
result = []

if len(matrixA[0]) == len(matrixB): # changed condition
    print("Matrix A and Matrix B can be multiplied together.") # changed the string literal

    row = len(matrixA) # 2
    col = len(matrixB[0]) # 3
    
    temprow = [0] * col # [0,0]
    for i in range(row):
        result.append([0] * col)

    for _ in range(row):
        list(temprow).append(result)
    
    for i in range(row):
        for j in range(col):
            for k in range(len(matrixB)):
                result[i][j] += matrixA[i][k] * matrixB[k][j]

    print(result)
    
else:  # Change to else from elif
    print("Matrix A and Matrix B cannot be multiplied together.")
