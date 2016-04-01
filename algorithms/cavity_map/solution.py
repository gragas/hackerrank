# Read in the data
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

# Solve the problem
for i in range(n):
    for j in range(n):
        if i > 0 and i < n-1 and j > 0 and j < n-1:
            adjacents = (data[i-1][j], data[i][j-1], data[i][j+1], data[i+1][j])
            if all([value < data[i][j] for value in adjacents]):
                print("X", end="")
            else:
                print(data[i][j], end="")
        else:
            print(data[i][j], end="")
    print()
