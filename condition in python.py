mark=10
if mark>100:
    print("invalid")

elif mark>=90:
    print("A+")

elif mark>=85 and mark<90:
    print("A")

elif mark>=80 and mark<85:
    print("B+")

elif mark>=75 and mark<80:
    print("B")

elif mark>=70 and mark<75:
    print("C+")

elif mark>=65 and mark<70:
    print("C")

elif mark>=60 and mark<65:
    print("D+")

elif mark>=50 and mark<60:
    print("D")

else:
    print("F")