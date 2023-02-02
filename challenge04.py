# Reverse a number with explanation

n = int(input("Number to be reversed: "))
print("Number entered: %d" % n)
reversed = 0
while(n != 0):
    reversed = reversed * 10 + n % 10
    n = int(n / 10)
print("Reversed number: %d" % reversed )