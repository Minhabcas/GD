
def gradient_descent(starting_point, learning_rate, num_iterations):
    x = starting_point
    for i in range(num_iterations):
        gradient = 2 * x + 6
        x = x - learning_rate * gradient
        f_x = x**2 + 6*x + 8
        print(f"Iteration {i+1}: x = {x}, f(x) = {f_x}")

gradient_descent(starting_point=-1, learning_rate=0.1, num_iterations=5)
