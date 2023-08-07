def countdown(num):
    if num == 0:
        print("caboom")
    else:
        print(num)
        countdown(num -1)
countdown(5)

print("--------------------------")

def countdown2(num):
    for number in range(-num,0):
         print(-number)

    print("!boom¡")
        
countdown2(20)


print("----------------------------")


def infinite_recursion(word):
    print(word)
    infinite_recursion(word)
infinite_recursion("comelona")