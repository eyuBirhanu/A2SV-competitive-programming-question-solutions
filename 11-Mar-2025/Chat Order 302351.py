# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

from collections import OrderedDict

len_ = int(input())
chat = OrderedDict()
for _ in range(len_):
    name = input()
    if name not in chat:
        chat[name] = 0
        chat.move_to_end(name, last=False)
    else:
        chat.move_to_end(name, last=False)

for name , val in chat.items():
    print(name)