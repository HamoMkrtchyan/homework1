# ----1----

x = int(input('1 - please enter a number'))
y = x // 2
if y == 0:
    print('    The number is even')
else:
    print('    The number is odd')

# ----2---

ch = input("2 - Enter a character: ")

if (ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I'
      or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u'):
    print("   ", ch, "is a Vowel")
else:
    print("   ", ch, "is a Consonant")

# ----3----

n = int(input("3 - Enter a number: "))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("    The nth Fibonacci number is:", fibonacci(n))


#----4----
num = int(input("4 - Enter a number: "))

sum = 0

while num > 0:
    sum += num % 10

    num //= 10

print("    The sum of the digits is:", sum)


#----5----
print('5 - ')
for i in range(5):
    if i == 0 or i == 4:
        print("* " * 5)
    else:
        print("*       *")
