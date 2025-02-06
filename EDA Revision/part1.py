import numpy as np

def calculate(list):
    if len(digits) != 9:
        raise ValueError("List must contain nine numbers.")
    list = np.array(digits).reshape(3, 3)

    mean = [(np.mean(list[:, 0]), np.mean(list[:, 1]), np.mean(list[:, 2])),
            (np.mean(list[0]), np.mean(list[1]), np.mean(list[2]) ),
             np.mean(list)]

    var = [(np.var(list[:, 0]), np.var(list[:, 1]), np.var(list[:, 2])),
            (np.var(list[0]), np.var(list[1]), np.var(list[2]) ),
             np.var(list)]

    std = [(np.std(list[:, 0]), np.std(list[:, 1]), np.std(list[:, 2])),
           (np.std(list[0]), np.std(list[1]), np.std(list[2]) ),
            np.std(list)]

    max = [(np.max(list[:, 0]), np.max(list[:, 1]), np.max(list[:, 2])),
           (np.max(list[0]), np.max(list[1]), np.max(list[2]) ),
            np.max(list)]

    min = [(np.min(list[:, 0]), np.min(list[:, 1]), np.min(list[:, 2])),
           (np.min(list[0]), np.min(list[1]), np.min(list[2]) ),
            np.min(list)]

    sum = [(np.sum(list[:, 0]), np.sum(list[:, 1]), np.sum(list[:, 2])),
           (np.sum(list[0]), np.sum(list[1]), np.sum(list[2]) ),
            np.sum(list)]

    calculations = {
        'mean': [mean[0], mean[1], mean[2]],
        'var': [var[0], var[1], var[2]],
        'std': [std[0], std[1], std[2]],
        'max': [max[0], max[1], max[2]],
        'min': [min[0], min[1], min[2]],
        'sum': [sum[0], sum[1], sum[2]]
    }
    return calculations

# digits = list(map(int, input().split()))  # For a custom input
digits = [0, 1, 2, 3, 4, 5, 6, 7]  # Fixed input
print(calculate(digits))

