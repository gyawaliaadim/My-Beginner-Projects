import random
from turtle import *
a=random.randint(0,180)
b=random.randint(0,180)
color('red', 'yellow')
begin_fill()
while True:
    forward(a)
    left(b)
    if abs(pos()) < 1:
        break
end_fill()
done()