a,b,c=map(int,input().split())
if (a==b==c):
    print("Equilateral triangle")
elif (a!=b!=c):
    print("Scalene triangle")
else:
    print("Isosceles triangle")