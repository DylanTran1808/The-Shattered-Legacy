import numpy  as np

def function(x):
    P = 5 * ((1.02) ** x)
    return P

def derivative(x):
    dP = 5 * np.log(1.02) * ((1.02) ** x)
    return dP

def euler_method(x0, P0, h, num_steps):
    x_values = [x0]
    P_values = [P0]

    for _ in range(num_steps):
        x_n = x_values[-1]
        P_n = P_values[-1]
        dP_n = derivative(x_n)

        x_next = x_n + h
        P_next = P_n + h * dP_n

        x_values.append(x_next)
        P_values.append(P_next)

    return x_values, P_values

def backward_euler_method(x0, P0, h, num_steps):
    x_values = [x0]
    P_values = [P0]

    for _ in range(num_steps):
        x_n = x_values[-1]
        P_n = P_values[-1]
        dP_n = derivative(x_n)

        x_next = x_n - h
        P_next = P_n - h * dP_n

        x_values.append(x_next)
        P_values.append(P_next)

    return x_values, P_values

#usage

initial_x = 0
initial_P = 5.0
step_size = 0.5
num_steps = 10

x_values, P_values = euler_method(initial_x, initial_P, step_size, num_steps)
x_back , P_back  = backward_euler_method(initial_x, initial_P, step_size, num_steps)


# Print or visualize the results
# Backward Euler
# for xb, Pb in zip(x_back, P_back):
    # if round(xb,2) == -10.0: 
        # print(f"x: {xb}, P: {Pb}")

# Forward Euler
for x, P in zip(x_values, P_values):
    # if round(x,2) == 10.0 or round(x, 2) == 50.0 or round(x, 2) == 240.0:
        print(f"x: {x}, P: {P}")
    # elif round(x,2) == 0.0:
        print(f"x: {x}, P: {P}")