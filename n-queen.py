# -*- coding: utf-8 -*-
'''
    for Even matrix :
        Append inverted mirror image of mat1

    for Odd matrix :
        Append inverted mirror image of mat1
        insert single row with middle element with Queen in the middle

    Mat1 is a 4D matrix with 2D array

                                                                        '''

n= int(raw_input("n x n Matrix : Tell 'n' "))

symbol = 1


# Blue-Print of checkboard

if not n%2:
    if n%4:
        x = n/2 -1
    else:
        x = n/2                                     # STARTING Index IS 'Zero'
else:
    if n%4:
        x = (n-1)/2
    else:
        x = (n+1)/2
       

no_space = []
queen =[]

n_dash = n/2
mat1 = [[0 for i in range(n)]for a in range(n_dash)]

import math
f = (n-x)/2
l = int(math.ceil((n_dash+x)/2.0))


for a in range(f,l):

    for b in range(x):
        no_space.append((a,f+b))


# Inserting Queens      

r_index = f-1           #  [r_index][c_index] == (y,x)
c_index = f


for a in range(n/2+1):

    if c_index>=n:
        c_index = c_index%(n-1) -1
        
    queen.append([r_index,c_index])
    mat1[r_index][c_index] = symbol
    
    r_index-=1
    c_index+=2

'''
print 'Queen',queen
print
print
print'Matrix',mat1
'''

# Inverting         # Virtual starting Index is 'One'

mat2 = [[0 for i in range(n)]for a in range(n_dash)]
king = []

for a in queen:
    r = a[0]
    c = a[1]

    mat2[-1*(r+1)][-1*(c+1)] = symbol
    king.append([-1*(r+1),-1*(c+1)])


# Appending
checkboard = mat1+mat2

if n%2:         # odd test
    l1 = [0 for i in range(n)]
    l1[n/2]= symbol 

    checkboard.insert(n/2,l1)

# Display
print'\n\n'

if n<17:

    for a in range(len(checkboard)):                    # use for small value as speed decreases!

        for b in range(len(checkboard[0])):

            print checkboard[a][b],' ',
        print
else:
    for a in checkboard:
        print a

