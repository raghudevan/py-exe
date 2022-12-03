
def max_age(input):
    nameForMaxAge = ""
    maxAge = 0
    for line in input.readlines()[1:]:
        [name,age] = line.split(',')
        age = int(age)
        if age > maxAge:
            maxAge = age
            nameForMaxAge = name

    return [nameForMaxAge, maxAge] 
