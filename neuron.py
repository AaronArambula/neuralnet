import numpy as np

inputs = [0.5, 0.25, 0.75]
weights = [0.4, 0.6, 0.8]
bias = 0.1
output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
print(output)