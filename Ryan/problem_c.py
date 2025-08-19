import math

probability = [0.20, 0.15, 0.12, 0.10, 0.08, 0.06, 0.05, 0.05, 0.04, 0.03, 0.02, 0.10]

entropy = -sum(p * math.log2(p) for p in probability)
print(f'entropy: {entropy}')

fano = [[0.20,3],[0.15, 3], [0.12, 3], [0.10, 4], [0.08, 4], [0.06, 4], [0.05, 3], [0.05, 4], [0.04, 4], [0.03, 4], [0.02, 4], [0.10, 4]]
weighted_average_code_length = sum(probability * length for probability, length in fano)
print(f'weighted_average_code_length: {weighted_average_code_length}')

average_code_length = sum(length for _, length in fano) / len(fano)
print(f'average_code_length: {average_code_length}')

weighted_difference = weighted_average_code_length - entropy
print(f'weighted_difference: {weighted_difference}')

difference = average_code_length - entropy
print(f'dfference: {difference}')