import month
import law
d = int(input("Enter date:"))
mth = int(input("Enter month:"))
y = str(input("Enter year:"))
if mth == 3:
        mth = 1
elif mth == 4:
        mth = 2
elif mth == 5:
        mth = 3
elif mth == 6:
        mth = 4
elif mth == 7:
        mth = 5
elif mth == 8:
        mth = 6
elif mth == 9:
        mth = 7
elif mth == 1:
        mth = 8
elif mth == 11:
        mth = 9
elif mth == 12:
        mth = 10
elif mth == 1:
        mth = 11
elif mth == 2:
        mth = 12
law.zeller(d,mth,y)











