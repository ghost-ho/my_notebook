def idWithSet(element, Set):
    if element in Set:
        return element
    else:
        raise ValueError

# S = {1, 2, 3}
# print(idWithSet(1, S))
# print(idWithSet(2, S))
# print(idWithSet(3, S))
# print(idWithSet(4, S))

def DescartesProduct(Set1, Set2):
    Set = set()
    for i in Set1:
        for j in Set2:
            new_element = (i, j)
            Set.add(new_element)
    return Set

# X = {1, 2, 3}
# print(DescartesProduct(X, X))

# 交集
def myIntersection(Set1, Set2):
    intersection_set = set()
    for i in Set1:
        if i in Set2:
            intersection_set.add(i)
    return intersection_set


X = {1, 2, 3}
Y = myIntersection(X, X)
print(X)
print(Y)