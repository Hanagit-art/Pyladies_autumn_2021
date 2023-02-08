
                
from turtle import forward, left, exitonclick

n = int(input('Zadej pocet uhlu: '))

for i in range(n):
    forward(200)
    left(180-180*(1-2/n))
    
exitonclick()







