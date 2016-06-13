# Matrix Algebra
import numpy as np



a = np.matrix([[1,2,3], [2,7,4]])
b = np.matrix([[1,-1], [0,1]])
c = np.matrix([[5,-1], [9,1], [6,0]])
d = np.matrix([[3,-2,-1], [1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.matrix([[1], [8], [0], [5]])
alpha = 6



#1.1
a.shape
#(2, 3)

#1.2
b.shape
#(2, 2)

#1.3
c.shape
#(3, 2)
#1.4
d.shape
#(2, 3)

#1.5
u.shape
#(4,)



#1.6
w.shape
#(4, 1)

#2.1
u+v
#array([ 9,  7, -4,  9])

#2.2
u-v
#array([ 3, -3, -2,  1])

#2.3
alpha*u
#array([ 36,  12, -18,  30])

#2.4
u*v
#array([18, 10,  3, 20])

#2.5
sum([i**2 for i in u])**.5
#array([ 6,  2, -3,  5])

#3.1
a+c
#error


#3.2
a-c.transpose()
#matrix([[-4, -7, -3],
#        [ 3,  6,  4]])

#3.3
c.transpose() + (3*d)
#matrix([[14,  3,  3],
#        [ 2,  7,  9]])

#3.4
b*a
#matrix([[-1, -5, -1],
#       2,  7,  4]])

#3.5
b*a.transpose()
#error


#3.6
b*c
#error


#3.7
c*b
#matrix([[ 5, -6],
#        [ 9, -8],
#        [ 6, -6]])


#3.8
b**4
#matrix([[ 1, -4],
#        [ 0,  1]])
#3.9
a*a.transpose()
#matrix([[14, 28],
#        [28, 69]])

#3.10
d.transpose()*d
#matrix([[10, -4,  0],
#        [-4,  8,  8],
#        [ 0,  8, 10]])
