def flatten(iterable):
    value = []
    while iterable:
        first = iterable.pop(0)
        if isinstance(first, int):
            value.append(first)
        elif isinstance(first, list):
            iterable = first + iterable
    return value

    value = []
    stack = [iter(iterable)]

    while stack:
        for item in stack[-1]:
            print(item)
            if isinstance(item, list):
                stack.append(iter(item))
                break
            elif item is not None:
                value.append(item)
        else:
            stack.pop()
    return value



a = flatten([[[[100,2]]],2])
print(a)