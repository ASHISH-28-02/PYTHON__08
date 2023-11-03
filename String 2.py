#program to replace all occurence in a string


#Python has inbuilt function replace to replace all occurrences of substring.
input_string = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"
input_string = input_string.replace(s1, s2)
print(input_string)


#code for replacing all occurrences of substring s1 with new string s2

test_str="geeksforgeeks"
s1="geeks"
s2="abcd"

#string split by substring
s=test_str.split(s1)
new_str=""

for i in s:
	if(i==""):
		new_str+=s2
	else:
		new_str+=i

#printing the replaced string
print(new_str)


