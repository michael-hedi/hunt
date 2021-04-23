def zeller(date,month,year):
    y1 = int(year[0:2])
    y2 = int(year[2:])
    cald_month=(13*month-1)//5
    sum_of = date + cald_month + y2 + y2//4 + y1//4
    c = y1*2
    law1 = sum_of - c
    law2 = law1%7
    if law2 == 0:
        print("Sunday")
    elif law2 == 1:
        print("Monday")
    elif law2 == 2:
        print("Tuesday")
    elif law2 == 3:
        print("wednesday")
    elif law2 == 4:
        print("Thuesday")
    elif law2 == 5:
        print("Friday")
    elif law2 == 6:
        print("Saturday")
    
    
    
    
    





    
    
    

