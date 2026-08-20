
a, b = 0, 0 
# i = 0

while (a < 10):

    i = 0

    while (b < 50):
        b += i 
        i += 1

        print("b is: ", b)
        print("i is: ", i)

        if (i == 5):
            break 

    print("b iteration is finished")

    a += i
    print("a is: ", a, "\n")

print("a iteration is finished")