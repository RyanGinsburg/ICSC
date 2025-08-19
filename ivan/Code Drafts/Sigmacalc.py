import math

input = [.2, .15, .12, .10, .08, .06, .05, .05, .04, .03, .02, .10]
sum = 0
for val in input:
    instance = (val * math.log(val, 2))
    print(instance)
    sum += instance
sum = -sum
print(sum)