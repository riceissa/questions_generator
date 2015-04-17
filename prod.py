import itertools

def prod(A, B):
    A = set(A)
    B = set(B)
    B = B.difference(A)
    result = []
    for i in itertools.product(A, B):
        if len(i) == len(set(i)):
            result.append(i)
    return result

def mprod(*args):
    pass

A = ["a", "b", "c"]
B = ["e", "b", "f", "a"]

print(prod(A, B))
