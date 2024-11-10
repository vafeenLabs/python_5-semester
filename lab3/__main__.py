import fp


#  Тестирование filter_t
a = [1, 6, 2, 6]


def is_4etnoe(x) -> bool:
    return x % 2 == 0


b = list(fp.filter_t(predicate=is_4etnoe, collection=a))
print(b)


# Тестирование map_gen 
def tostr(x: int) -> str:
    return str(x)


b = [1, 6, 2, 6]

c = fp.map_gen(function=tostr, collection=b)
print(list(c))

#Тестирование filter_lgen 
a = [1, 6, 2, 6]


def is_4etnoe(x) -> bool:
    return x % 2 == 0


b = fp.filter_lgen(predicate=is_4etnoe, collection=a)
print(b)