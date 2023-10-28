#python program to multiply two matrices

# Matrix multiplication using nested for loop  
# Initialize the value of the a and b matrix    
a = [[1,2,3],  
        [4,5,6],  
        [7,8,9]]  
b = [[0,0,1],  
       [0,1,0],  
       [1,0,0]]  
res = [[0,0,0],  
         [0,0,0],  
         [0,0,0]]  
for i in range(len(a)):  
   for j in range(len(b[0])):  
       for k in range(len(b)):  
           res[i][j] += a[i][k] * b[k][j]  
for r in res:  
   print(r)  
