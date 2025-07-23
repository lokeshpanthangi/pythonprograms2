def matrix_multiply(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            sum = 0
            for k in range(len(mat2)):
                sum += mat1[i][k] * mat2[k][j]
            row.append(sum)
        result.append(row)
    return result




print("Enter Vectors")
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s=0

c=[]

for i in range(len(a)):
    s = s + a[i] * b[i]
    n = a[i] + b[i]
    c.append(n)
print(c)
print(s)
if s > 0 :
    print("Orthogonal = False")
else:
    print("Orthogonal = True")


#Matrix Multiplication

row = int(input("No of rows:"))
col = int(input("No of cols:"))

mat1=[]
mat2=[]
for i in range(2):
    print("Enter data for Matrix",i+1)
    for i in range(row):
        k = list(map(int,input().split()))
        if i == 0 :
            mat1.append(k)
        else:
            mat2.append(k)

result = matrix_multiply(mat1,mat2)
print(result)

