print(type(1.1))


print ("'What will I do?' exclaimed Julia")

print (24.6, int(24.6))

print(type("Hello, World!"))
print(type(17))
print("Hello, World")

print(type(17))
print(type(3.2))
print(type("17"))
print(type("3.2"))

print(type("17"))
print(type("3.2"))

print(type("17"))
print(type("3.2"))


print(3.14, int(3.14))
print(3.9999, int(3.9999))       # This doesn't round to the closest int!
print(3.0, int(3.0))
print(-3.999, int(-3.999))        # Note that the result is closer to zero

print("2345", int("2345"))        # parse a string to produce an int
print(17, int(17))                # int even works on integers
          # tohle nejde print(int("23bottles")) 

print(float("123.45"))
print(type(float("123.45")))
print(str(17))
print(str(123.45))
print(type(str(123.45)))

message = "What's up, Doc?"
n = 17
pi = 3.14159

print(message)
print(n)
print(pi)



message = "What's up, Doc?"
n = 17
pi = 3.14159

print(type(message))
print(type(n))
print(type(pi))


y = 3.14
x = len("hello")
print(x)
print(y)

print(1 + 1)
print(len("hello"))


print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 ** 3)
print(3 ** 2)

minutes = 645
hours = minutes / 60
print(hours)

print(7 / 4)
print(7 // 4)

minutes = 645
hours = minutes // 60
print(hours)

print(6//4)
print(-6//4)

quotient = 7 // 3     # This is the integer division operator
print(quotient)
remainder = 7 % 3
print(remainder)

n = input("Please enter your name: ")
print("Hello", n)

str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)

print(2 ** 3 ** 2)     # the right-most ** operator gets done first!
print((2 ** 3) ** 2)   # use parentheses to force the order you want!

bruce = 5
print(bruce)
bruce = 7
print(bruce)

a = 5
b = a    # after executing this line, a and b are now equal
print(a, b)
a = 3    # after executing this line, a and b are no longer equal
print(a, b)

x = 6        # initialize x
print(x)
x = x + 1    # update x
print(x)