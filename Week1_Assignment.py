# For_Lower_Triangle
def lower_triangle(n):
    for i in range(n):
        for j in range(n-i-1):
            print("",end="")
        for j in range(i+1):
            print("*",end=" ")
        print()
# For_Upper_Triangle
def upper_triangle(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()
# For_Pyramid_Triangle
def pyramid_triangle(n):
    for i in range(n):
        for j in range(n-i-1):
            print("",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
print("Lower Triangle Pattern:")
lower_triangle(7)
print("\n")
print("Upper Triangle Pattern:")
upper_triangle(7)
print("\n")
print("Pyramid Pattern:")
pyramid_triangle(7)
            