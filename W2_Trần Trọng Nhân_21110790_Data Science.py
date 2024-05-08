#Trần Trọng Nhân - 21110790
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def visualize(augmented_matrix,title):
    n = len(augmented_matrix)

    #gaussian elimination
    for i in range(n):
        max_el = abs(augmented_matrix[i][i])
        max_row = i
        for k in range(i+1, n):
            if abs(augmented_matrix[k][i]) > max_el:
                max_el = abs(augmented_matrix[k][i])
                max_row = k

    
        augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]

        
        for k in range(i+1, n):
            c = -augmented_matrix[k][i]/augmented_matrix[i][i]
            for j in range(i, n+1):
                if i == j:
                    augmented_matrix[k][j] = 0
                else:
                    augmented_matrix[k][j] += c * augmented_matrix[i][j]


    solution = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        solution[i] = augmented_matrix[i][n]/augmented_matrix[i][i]
        for k in range(i-1, -1, -1):
            augmented_matrix[k][n] -= augmented_matrix[k][i] * solution[i]

    print(f"The solution is {solution}")



    #Plot
    def eq(x, y, coeffs):
        return (coeffs[0]*x + coeffs[1]*y - coeffs[3])/(-coeffs[2]+1e-1000)

    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)

    X, Y = np.meshgrid(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    colors = ['b', 'r', 'g', 'y']

    # Plot the surfaces
    for i in range(len(augmented_matrix)):
        Z = eq(X, Y, augmented_matrix[i])
        ax.plot_surface(X, Y, Z, color=colors[i], alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)

    plt.show()


def main():
    augmented_matrix = [[2, 1, -2, 8], [3, 2, -4, 15], [5, 4, -1, 1]]
    visualize(augmented_matrix,title="3 equations")

    print("\n================================")

    augmented_matrix = [[2, 2, -1, 1,4], [4, 3, -1, 2, 6], [8, 5, -3, 4,12],[3,3,-2,2,6]]
    visualize(augmented_matrix,title="4 equations")

main()