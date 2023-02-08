"""Napiš funkci pohyb, která dostane seznam souřadnic a světovou stranu ("s", "j", "v" nebo "z") a přidá k seznamu poslední bod „posunutý“ v daném směru."""

#  menim pozici pismene X pomoci cyklu while
    
# print(len(coor))
# coor = coor[-1:] # posledni prvek seznamu dvojic

coor = [(0, 0), (1, 0), (2, 0)]  
def motion(dir): 
    
    e = [(coor[len(coor)-1][0], coor[len(coor)-1][1]+1)]
    s = [(coor[len(coor)-1][0]+1, coor[len(coor)-1][1])]
    w = [(coor[len(coor)-1][0], coor[len(coor)-1][1]-1)]
    n = [(coor[len(coor)-1][0]-1, coor[len(coor)-1][1])]
    
    if dir == "e":
        return e
    elif dir == "s":
        return s
    elif dir == "w":
        return w
    elif dir == "n":
        return n
            

def f(coor):  
    dots = 10 * "."
    map = []
    for i in range(10):
        map.append(list(dots))
         
    for raw, col in coor:
        map[raw][col] = "X"   
    return map


while True:
  
    dir = input("Set direction as e(east), w (west), n (north), s (south): ")
                
    if dir == "end":
            break
    try:       
        dir = motion(dir)
    
        # print(dir)
        
    except TypeError:
        print("Nerozumim, chyba!")
    except IndexError:
        print("Jsi mimo pole. Zadej jiny smer!")
        
    else:                    
        coor = coor + dir
        print(coor)
        coor = coor[-3:]
        # if dir in coor:
        #     raise 
        print(coor)
        
        local_map = f(coor) 

        for list2 in local_map:
            for item in list2:
                print(item, end=' ')
                        
            print()
