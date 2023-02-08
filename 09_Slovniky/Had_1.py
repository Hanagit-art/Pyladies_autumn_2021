"""Napiš funkci pohyb, která dostane seznam souřadnic a světovou stranu ("s", "j", "v" nebo "z") a přidá k seznamu poslední bod „posunutý“ v daném směru."""

#  menim pozici pismene X pomoci cyklu while
    
# print(len(snake))

snake = [(0, 0), (1, 0), (2, 0)]
fruit = [(2,3)]  
# snake = snake[-1]  # posledni prvek seznamu dvojic
# print(snake)

def motion(snake, dir): 
    
    e = [(snake[len(snake)-1][0], snake[len(snake)-1][1]+1)]
    s = [(snake[len(snake)-1][0]+1, snake[len(snake)-1][1])]
    w = [(snake[len(snake)-1][0], snake[len(snake)-1][1]-1)]
    n = [(snake[len(snake)-1][0]-1, snake[len(snake)-1][1])]
    
    if dir == "e":
        return e
    elif dir == "s":
        return s
    elif dir == "w":
        return w
    elif dir == "n":
        return n

def f(map):  
    dots = 10 * "."
    map = []
    for i in range(10):
        map.append(list(dots))
         
    for raw, col in snake:
        map[raw][col] = "X"
    for raw, col in fruit:
        map[raw][col] = "?"  
    return map


while True:
    dir = input("Set direction: ")
             
    if dir == "end":
        break
        
    dir = motion(snake, dir)         
    print(dir)
        
    snake = snake + dir
    
    print(snake)
    
    snake = snake[-3:]
    if dir in snake:
        print('You hit yourself!')
    elif dir in fruit:
         
    

    print(snake)
    
        
    local_map = f(map) 

    for list2 in local_map:
        for item in list2:
            print(item, end=' ')
                
        print()
