def move(f, t):
    print(f"Move disc from {f} to {t}!")


def moveVia(f, v, t):
    move(f,v)
    move(v,t)

def hanoi(n, f, h, t):
    if n == 0:
        pass
    else:
        hanoi(n-1, f, t, h)
        move(f, t)
        hanoi(n-1, h, f, t)


hanoi(1, "A", "B", "C")


