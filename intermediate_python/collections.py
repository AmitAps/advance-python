#collections: Counter, namedtuple, OrderedDict, defaultdict, deque
# from collections import Counter
# a = "aaaabbbbbbccccdddddddddddddd"
# my_counter = Counter(a)
# # print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common())
# print(my_counter.most_common(1)[0][0])

# from collections import namedtuple
# Point = namedtuple('Point','x,y')
# pt = Point(1, -8)
# print(pt)
# print(pt.x, pt.y)

# from collections import OrderedDict
# ordered_dict = OrderedDict()
# ordered_dict['a'] = 1
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4
# print(ordered_dict)


# from collections import defaultdict
# d = defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# print(d)
# print(d['c'])

from collections import deque
d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)
