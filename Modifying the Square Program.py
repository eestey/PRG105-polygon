import turtle

bob = turtle.Turtle()
bob.shape("turtle")
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)


def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


square(bob)


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


square(bob, 50)


def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


polygon(bob, 9, 100)
turtle.done()
