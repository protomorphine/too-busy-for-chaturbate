import itertools
import time

it = itertools.cycle(["."] * 3 + ["\b \b"] * 3)
cc = itertools.cycle("-/|\\")
# for x in range(30):
#    time.sleep(0.3)  # выполнение функции
#    print(next(it), end="", flush=True)
# print("Downloading ", end="")
# for c in range(30):
#    print(next(cc) + "\b", flush=True, end="")
#    time.sleep(0.1)
