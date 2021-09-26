import numpy as np


def calculate(nums):
    if len(nums) != 9:
        raise ValueError('List must contain nine numbers.')

    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }
    nums = np.array(nums).reshape(3, 3)
    calculations['mean'].append(list(np.mean(nums, axis=0)))
    calculations['mean'].append(list(np.mean(nums, axis=1)))
    calculations['mean'].append(np.mean(nums))
    calculations['variance'].append(list(np.var(nums, axis=0)))
    calculations['variance'].append(list(np.var(nums, axis=1)))
    calculations['variance'].append(np.var(nums))
    calculations['standard deviation'].append(list(np.std(nums, axis=0)))
    calculations['standard deviation'].append(list(np.std(nums, axis=1)))
    calculations['standard deviation'].append(np.std(nums))
    calculations['max'].append(list(np.max(nums, axis=0)))
    calculations['max'].append(list(np.max(nums, axis=1)))
    calculations['max'].append(np.max(nums))
    calculations['min'].append(list(np.min(nums, axis=0)))
    calculations['min'].append(list(np.min(nums, axis=1)))
    calculations['min'].append(np.min(nums))
    calculations['sum'].append(list(np.sum(nums, axis=0)))
    calculations['sum'].append(list(np.sum(nums, axis=1)))
    calculations['sum'].append(np.sum(nums))

    # 可以简化为
    # calculations = {'mean': [list(np.mean(nums, axis=0)), list(np.mean(nums, axis=1)), np.mean(nums)],
    #                 'variance': [list(np.var(nums, axis=0)), list(np.var(nums, axis=1)), np.var(nums)],
    #                 'standard deviation': [list(np.std(nums, axis=0)), list(np.std(nums, axis=1)), np.std(nums)],
    #                 'max': [list(np.max(nums, axis=0)), list(np.max(nums, axis=1)), np.max(nums)],
    #                 'min': [list(np.min(nums, axis=0)), list(np.min(nums, axis=1)), np.min(nums)],
    #                 'sum': [list(np.sum(nums, axis=0)), list(np.sum(nums, axis=1)), np.sum(nums)]}

    return calculations






