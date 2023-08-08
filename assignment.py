#write the coefficients of the equation in the form of a matrix in the text file "mat.txt"

import copy
#multiplying matrices
def multiply(elementary,mat):
    matrix_multiply=[]
    for i in elementary:
        row=[]
        c=0
        for y in range(cols):
            term=0
            j=0
            for x in mat:
                term+=i[j]*x[c]
                j+=1
            c+=1
            row.append(term)
        matrix_multiply.append(row)
    mat=matrix_multiply
    return mat
# creating a mXm identity matrix
def identity(r):
    element_mat=[]
    c=0
    for i in range(r):
        row=[]
        for j in range(r):
            if j==c:
                row.append(1)
            else:
                row.append(0)
        element_mat.append(row)
        c+=1
    return element_mat   
#to interchange rows        
def interchange(mat,r1,r2):
    changed=copy.deepcopy(identity_matrix)
    for i in range(len(changed)):
        if i==r1:
            changed[i]=identity_matrix[r2]
    changed[r2]=identity_matrix[r1]
    return multiply(changed,mat)
#to replace rows
def replace(mat,r1,r2,x):
    changed=copy.deepcopy(identity_matrix)
    changed[r1][r2]=x
    return multiply(changed,mat)
#to scale a row
def scale(mat,r1,x):
    changed=copy.deepcopy(identity_matrix)
    changed[r1][r1]=x
    return multiply(changed,mat) 
#to find the transpose of the matrix(parametric form)
def transpose(mat):
    c=0
    mat_transpose=[]
    while c<=cols-1:
        row=[]
        for i in range(rows):
            if mat[i][c]==0 or mat[i][c]==1:
                row.append(mat[i][c])
            else:
                row.append(-mat[i][c])
                
        mat_transpose.append(row)
        c+=1
    
    return mat_transpose  
    
#reading the input from the text file 
f=open('mat.txt','r')
inp=f.readlines()
rows=int(inp[0][:-1])
cols=int(inp[1][:-1])
mat=[]
for row in inp[2:]:
    entries=list(map(int,row[:-1].split()))
    mat.append(entries)

#creating an the augmented matrix for AX=0 
for row in mat:
    row.append(0)  
f.close()
identity_matrix=identity(rows)   
cols=cols+1
#creating echleon form of the matrix
c=0
r=0
pivots=[]
while c<=cols-1 and r<=rows-1:
    flag=True
    if mat[r][c]!=0:        
        pass    
    else:    
        flag=False  
        for i in range(r+1,rows):
            if mat[i][c]!=0:
                mat=interchange(mat,r,i)
                flag=True
                break
            else:
                flag=False

    if flag==True:    
        pivot=mat[r][c]
        pivot_index=r
        for i in range(r+1,rows):
            x=mat[i][c]/pivot
            mat=replace(mat,i,r,-x)
        pivots.append([r,c])
        c+=1
        r+=1
    else:
        c+=1
print('PIVOT POSITIONS')
print(pivots)
#to convert echleon to RREF
for x in pivots:
    r=x[0]
    c=x[1]
    entry=mat[r][c]
    if entry!=0:
        mat=scale(mat,r,1/entry)
for x in pivots:    
    r=x[0]
    c=x[1]
    if mat[r][c]!=0:        
        for j in range(r):
            if mat[j][c]!=0:
                y=mat[j][c]/mat[r][c]
                mat=replace(mat,j,r,-y)    
    
print('RREF OF THE MATRIX:')
for i in mat:
    for j in i:
        print(round(j,2),end=' ')
    print()


#finding free variables/parameters
y=[]
for i in pivots:
    y.append(i[1])
mat_transpose=transpose(mat)[:-1]
parameter=[]
for i in range(cols):
    if i not in y:
        parameter.append(i)
parameter=parameter[:-1]

# Parametric solution
if len(parameter)>0: 
    print('Non-trivial solution:')         
    
    for i in parameter:
        x=[0]*cols      
        x[i]=1  
        for j in range(len(mat_transpose[i])):
            if mat_transpose[i][j]!=float(0):
                x[pivots[j][1]]=round(mat_transpose[i][j],2)
        print(f'x{i}{x}')
else:
    print('Trivial solution')