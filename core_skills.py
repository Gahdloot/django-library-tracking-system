import random

rand_list = [random.randrange(1, 20) for _ in range(10)]

list_comprehension_below_10 = [x for x in range(10)]

list_comprehension_below_10 = list(filter(lambda x: x<10, range(10)))