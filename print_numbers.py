def senir_op():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("Senir Op")
        elif i % 3 == 0:
            print("Senir")
        elif i % 5 == 0:
            print("Op")
        else:
            print(i)

senir_op()
