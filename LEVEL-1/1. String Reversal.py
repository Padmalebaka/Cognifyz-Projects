a = input()
reversed_a = ""
length = len(a)

for i in range(length):
    reversed_a = reversed_a + a[(length-1) - i]

print(reversed_a)