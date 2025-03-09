import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def plot_quadratic():
    x = sp.symbols('x')
    f = -1*x**2 + 6*x - 9
    
    a = f.coeff(x, 2)   # coefficient of the term with degree 2 (a in a*(x-h)^2 + k)
    b = f.coeff(x, 1)   # coefficient of the term with degree 1 (-b in a*(x-h)^2 + k)
    c = f.coeff(x, 0)   # constant term (c in a*(x-h)^2 + k)

    # vertex coordinates
    if a != 0:
        h_vertex = - b / (2 * a)
        k_vertex = f.subs(x, h_vertex)
    else:
        print("No solutions")

    print('Vertex:', (h_vertex, k_vertex))

    # x-intercepts
    x_intercepts = [sol.evalf() for sol in sp.solve(f, x) if sol.is_real]
    print('X-intercepts:', x_intercepts)

    # Generate some data points for the graph
    x_vals = np.linspace(-10, 10, 400)
    y_vals = [f.subs(x, val) for val in x_vals]

    # Calculate the nearest whole number coordinate to the vertex
    nearest_x = round(float(h_vertex))
    if nearest_x == float(h_vertex):
        nearest_x += 1  # Adjust to ensure it's not the vertex itself
    nearest_y = f.subs(x, nearest_x)
    print('Nearest whole number coordinate:', (nearest_x, nearest_y))

    # Plot the data
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(x_vals, y_vals)
    plt.scatter([float(h_vertex)], [float(k_vertex)], color='red')   # plot vertex point
    plt.scatter([nearest_x], [nearest_y], color='green')   # plot nearest whole number point

    # Annotate the vertex
    plt.text(float(h_vertex) + 0.5, float(k_vertex), f'({float(h_vertex):.2f}, {float(k_vertex):.2f})', color='red')

    # Annotate the nearest whole number point
    plt.text(nearest_x + 0.5, nearest_y, f'({nearest_x}, {nearest_y})', color='green')

    # Annotate the x-intercepts
    for x_int in x_intercepts:
        plt.scatter([float(x_int)], [0], color='blue')   # plot x-intercept points
        plt.text(float(x_int) + 0.5, 0.5, f'({float(x_int):.2f}, 0)', color='blue')

    # Set axis ticks to count by 1
    plt.xticks(np.arange(-10, 11, 1))
    plt.yticks(np.arange(-10, 11, 1))  # Adjust y-axis ticks to count by 1

    # Set y-axis limits to include some negative values
    plt.ylim(-10, 10)

    # Set the origin at (0,0)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

    # Create a table of the point coordinates
    plt.subplot(1, 2, 2)
    plt.axis('off')
    table_data = [
        ["Point", "X", "Y"],
        ["Vertex", f"{float(h_vertex):.2f}", f"{float(k_vertex):.2f}"],
        ["Closest Point", f"{nearest_x}", f"{nearest_y}"]
    ]
    for i, x_int in enumerate(x_intercepts):
        table_data.append([f"X-intercept {i+1}", f"{float(x_int):.2f}", "0.00"])
    table = plt.table(cellText=table_data, colLabels=None, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.5, 1.5)

    plt.show()

if __name__ == "__main__":
    plot_quadratic()