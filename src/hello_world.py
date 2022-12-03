from age import max_age

import math
import time

print("hello world!")

input = open("input.csv", "r")
output = open("output.txt", "w")

[nameForMaxAge, maxAge] = max_age(input)
print(nameForMaxAge, maxAge)

output.write("{} is the oldest at {} years of age | floor {}; script run at {}".format(nameForMaxAge, maxAge, math.floor(maxAge), time.time()))

input.close()
output.close()