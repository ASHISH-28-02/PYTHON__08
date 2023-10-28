#cloning using python

# Python program to copy or clone a list
# Using the Slice Operator
def Cloning(li1):
	li_copy = li1[:]
	return li_copy


# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


# Python code to clone or copy a list
# Using the in-built function extend()


def Cloning(li1):
	li_copy = []
	li_copy.extend(li1)
	return li_copy


# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

# Python code to clone or copy a list 
# Using the List copy using =
def Cloning(li1): 
	li_copy = li1
	return li_copy 

# Driver Code 
li1 = [4, 8, 2, 10, 15, 18] 
li2 = Cloning(li1) 
print("Original List:", li1) 
print("After Cloning:", li2)
