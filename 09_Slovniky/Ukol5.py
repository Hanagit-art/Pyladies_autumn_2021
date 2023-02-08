

# print(len(coor))
# coor = coor[-1:] # posledni prvek druhe dvojice
coor = [(0, 0), (1, 0), (2, 0)]
while True:  

    dir = input("Set direction: ") 
    
    def motion(dir): 
        
        east = [(coor[len(coor)-1][0], coor[len(coor)-1][1]+1)]
        south = [(coor[len(coor)-1][0]+1, coor[len(coor)-1][1])]
        west = [(coor[len(coor)-1][0], coor[len(coor)-1][1]-1)]
        north = [(coor[len(coor)-1][0]-1, coor[len(coor)-1][1])]
        
        if dir == "east":
            return east
        elif dir == "south":
            return south
        elif dir == "west":
            return west
        elif dir == "north":
            return north
        
    dir = motion(dir)
    print(dir)
    # coor = coor + dir
                
    # print(coor)