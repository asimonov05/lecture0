def reverse():
    a = int(input())
    if a != 0:
        reverse()
        print(a, end=" ")
    else:
        return

reverse()