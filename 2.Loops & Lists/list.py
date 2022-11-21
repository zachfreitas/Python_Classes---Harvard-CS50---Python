


x =["Shit", "Poop", "Crap"]
y = [3,4,5]

d = dict(zip(x,y))

print(d)

u = [3,4,2]


def add_(x,y):
    return x+y


t = list(map(add_, y, u))

print(t)