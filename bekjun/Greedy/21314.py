import math

n = [a for a in input()]

def min(n):
    minimum = ""
    previous = 0
    count = 0
    for a in range(len(n)):
        if a == len(n)-1 and n[a] == "M":
            count += 1
            minimum += str(int(math.pow(10,count-1)))
        elif n[a] == "M":
            count += 1
            previous = "M"
        elif n[a] == "K":
            if previous == "M":
                minimum += str(int(math.pow(10,count-1)))
                previous = "K"
                count = 0
            minimum += "5"   
    return minimum

def max(n):
    maximum = ""
    previous = ""
    count = 0
    for a in range(len(n)):
        if n[a] == "M":
            if a == len(n)-1:
                maximum += str(int(math.pow(10, count)))
            previous = "M"
            count += 1
        elif n[a] == "K":
            if previous == "":
                maximum += "5"
            elif previous == "M":
                maximum += str(5*int(math.pow(10,count)))
            elif previous == "K":
                maximum += "5"
            previous = "K"
            count = 0
    return maximum
            
print(int(max(n)))
print(int(min(n)))

