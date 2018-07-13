import random

from copy import deepcopy

class Matrix:
    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.matrix=[]
        self.nrows=nrows
        self.ncols=ncols
        for _ in range(nrows):
            tmp=[]
            for _ in range(ncols):
                tmp.append(random.randint(0,9))
            self.matrix.append(tmp)

    def add(self,m):
        """return a new Matrix object after summation"""
        if Arows==Brows and Acols==Bcols:
            tmp=deepcopy(self)
            for i in range(tmp.nrows):
                for j in range(tmp.ncols):
                    tmp.matrix[i][j]=tmp.matrix[i][j]+m.matrix[i][j]
            return tmp
        else:
            return None

    def sub(self, m):
        """return a new Matrix object after substraction"""
        if Arows==Brows and Acols==Bcols:
            tmp=deepcopy(self)
            for i in range(tmp.nrows):
                for j in range(tmp.ncols):
                    tmp.matrix[i][j]=tmp.matrix[i][j]-m.matrix[i][j]
            return tmp
        else:
            return None

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        if Acols==Brows:
            mul=Matrix(Arows,Bcols)
            for i in range(self.nrows):
                for j in range(m.ncols):
                    tmp=0
                    for k in range(self.ncols):
                        tmp=tmp+self.matrix[i][k]*m.matrix[k][j]
                    mul.matrix[i][j]=tmp
            return mul
        else:
            return None

    def transpose(self):
        """return a new Matrix object after transpose"""
        if Acols==Brows:
            tmp=deepcopy(self)
            for i in range(self.nrows):
                for j in range(self.ncols):
                    tmp.matrix[i][j]=self.matrix[j][i]
            return tmp
        else:
            return None

    def display(self):
        """Display the content in the matrix"""
        for i in range(self.nrows):
            print(*self.matrix[i])
        print('')

Arows=int(input("Enter A matrix's rows:"))
Acols=int(input("Enter A matrix's cols:"))
A=Matrix(Arows,Acols)
print("Matrix A",'(',Arows,',',Acols,')')
A.display()

Brows=int(input("Enter B matrix's rows:"))
Bcols=int(input("Enter B matrix's cols:"))
B=Matrix(Brows,Bcols)
print("Matrix B",'(',Brows,',',Bcols,')')
B.display()

print('='*10,"A+B",'='*10)
Sum=A.add(B)
if Sum:
    Sum.display()
else:
    print("Matrixs' size should be in the same size")

print('='*10,"A-B",'='*10)
Sub=A.sub(B)
if Sub:
    Sub.display()
else:
    print("Matrixs' size should be in the same size")

print('='*10,"A*B",'='*10)
Mul=A.mul(B)
if Mul:
    Mul.display()
else:
    print("The number of cols in A must  equal to the number of rows in B")

print('='*10,"the transpose of A*B",'='*10)
if Mul:
    Trans=Mul.transpose()
    Trans.display()
else:
    print("The number of cols in A must  equal to the number of rows in B")
