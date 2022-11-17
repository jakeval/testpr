def foo(x):
    return x + 10


def bar(y):
    return y + 25


def baz(z, w):
    return z * w


if __name__ == "__main__":
    print(baz(foo(1), bar(4)))
    print(foo(baz(bar(10), 3)))
