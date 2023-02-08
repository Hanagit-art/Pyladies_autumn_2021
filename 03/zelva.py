
from turtle import penup, forward, pendown, right, left, exitonclick
from math import sqrt

for i in range(4):  
    forward(50)
    left(90)
 
left(45)
forward(sqrt(2*50**2))
for j in range(2):
        left(90)
        forward((sqrt(2*50**2))/2)
left(90)
forward(sqrt(2*50**2))   

exitonclick()







