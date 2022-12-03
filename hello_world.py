print("hello world");

input = open("input.csv", "r");
output = open("output.txt", "w");

nameForMaxAge = ""
maxAge = 0

for line in input.readlines()[1:]:
    [name,age] = line.split(',')
    age = int(age)
    if age > maxAge:
        maxAge = age
        nameForMaxAge = name

print(nameForMaxAge, maxAge)

output.write("{} is the oldest at {} years of age".format(nameForMaxAge, maxAge))

input.close();
output.close();