x=1
def f():
    x=7
    y=x
    x=2
    return x+y
print(x)
print(f())
print(x)