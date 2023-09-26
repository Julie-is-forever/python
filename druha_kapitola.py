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




#cviceni

#1
print(5 ** 2)
print(9 * 5)
print(15 / 12)
print(12 / 15)
print(15 // 12)
print(12 // 15)
print(5 % 2)
print(9 % 5)
print(15 % 12)
print(12 % 15)
print(6 % 6)
print(0 % 7)

#2
print (2 + (3 - 1) * 10 / 5 * (2 + 3))

#3
str_hours = input("Please enter the time in hours")
total_hours = int(str_hours)
str_time = input("Please enter the time difference in hours")
total_time = int(str_time)
hours = total_hours + total_time
time = hours // 24
clock =  hours % 24
print ("Hodiny budou ukazovat", clock)


#4
str_day = input("Please enter the day number")
total_day = int(str_day)
str_time = input("Please enter the lenght of your stay")
total_time = int(str_time)
stay = total_day + total_time
time = stay // 7
home =  stay % 7
print ("Vratite se ", home, "den v tydnu")


#5
a = "All"
b = "work"
c = "and"
d = "no"
e = "play"
f = "makes"
g = "Jack"
h = "a"
ch = "dull"
i = "boy"
print (a,b,c,d,e,f,g,h,ch,i)

#6
print (6 * (1 - 2))

#7

str_t = input("Please enter the number of years")
total_t = int(str_t)
P= 10000
n = 12
r = 0.08
compound =  P* (1+r/n) ** (n * total_t) 
print ("The compound will be ", compound)

#8

str_r = input("Please enter the radius")
total_r = int(str_r)
pi= 3.14
A =  pi* total_r**2
print ("The areas of your circle is ", A)

#9
str_w = input("Please enter the width of your rectangle")
total_w = int(str_w)
str_h = input("Please enter the height of your rectangle")
total_h = int(str_h)
A =  total_h* total_w
print ("The area of your rectangle is ", A)

#10

str_g = input("Please enter the number of gallons used")
total_g = int(str_g)
str_m = input("Please enter the number of miles travelled")
total_m = int(str_m)
MPG =  total_m / total_g
print ("The MPG of your car is ", MPG, "miles per gallon")


#11

str_c = input("Please enter the temperature in celsius")
total_c = int(str_c)
f =  total_c * 9 / 5 + 32
print ("The temperature in fahrenheit is ", f)


#12

str_f = input("Please enter the temperature in fahrenheit")
total_f = int(str_f)
c =  (total_f - 32)* 5 / 9
print ("The temperature in celsius is ", c)
