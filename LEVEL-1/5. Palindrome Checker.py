a = input()
reversed_a = ""     #initialization with empty string
length = len(a)     #length of the string

#for loop
for i in range(length):       #condition upto length of the string
    reversed_a = reversed_a + a[(length-1)-i]

if a == reversed_a:
    print("Palindrome")       #result if palindrome
else:
    print("Not a palindrome") #result if not a palindrome