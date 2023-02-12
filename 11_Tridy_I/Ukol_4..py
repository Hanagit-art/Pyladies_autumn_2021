test_str = "Cyware is US based MNC and works in IOT technology"
 
# splitting string
# list_str = test_str.split()
# print(list_str)

rd = "0062021234"
year = rd[0:2]
month = rd[2:4]
day = rd[4:6]
sex = rd[3]


def process_rd(rd, year, month, day, sex):
    """year"""
    if int(rd[0:2]) >= 54:
        year = "19"+rd[0:2]
    else:
        year = "20"+rd[0:2]
    
    """month"""
    if int(rd[2]) == 5 or int(rd[2]) == 0:
        month = int(rd[3])
    elif int(rd[2]) == 1:
        month = int(rd[2:4])
    else: 
        month = int(rd[3])+10
    
    """day"""
    if int(rd[4]) == 0:
        day = rd[5] 
    else:
        day = rd[4:6]
        
    """sex"""
    if int(rd[2]) > 1:
        sex = "female"
    else:
        sex = "male"
                
    return year, month, day, sex

print(process_rd(rd, year, month, day, sex))