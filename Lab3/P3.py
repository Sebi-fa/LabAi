def normalize_data(data):
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

data = [10, 20, 30, 40, 50]
normalized_data = normalize_data(data)
print(normalized_data)


import random
random_data = [random.randint(1, 100) for _ in range(5)]
print(random_data)
print(normalize_data(random_data))