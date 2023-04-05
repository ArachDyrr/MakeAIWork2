import random

def initial_random_weights(I_n):
    """generate random weights totaling to 1"""

    I_n = [sum(I_n, [])]

    # Generate n random values
    initial_weights = [random.random() for i in range(len(I_n[0]))]

    # Calculate the sum of the random values
    weight_sum = sum(initial_weights)

    # Divide each random value by the sum to normalize them
    random_weights = [item/weight_sum for item in initial_weights]

    return random_weights

circle = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]

print((circle))
print(type(circle))
print()
print ()
random_weights = initial_random_weights(circle)
print(random_weights)
print (len(random_weights))
print(sum(random_weights))