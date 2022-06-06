def aproxNum(num, target, amount):
    if num > target:
        if num - amount < target:
            return target
        else:
            return num - amount
    else:
        if num + amount > target:
            return target
        else:
            return num + amount

def lerp(num, target, percentage):
    return (percentage * num) + ((1 - percentage) * target)