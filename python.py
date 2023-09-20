import random

horni_limit = 100

y=random.randint(0,horni_limit)
print (f"Myslím si číslo mezi 0 a {horni_limit}.")
print('Zkus ho uhodnout.')

x = y+1

while x!=y:

    try:
        x= int(input())
    except ValueError:
        print("Tohle není číslo! Zkus to znovu.")
        continue
    if x<y:
        print("moje číslo je větší")

    if x>y:
        print("moje číslo je menší")
        
        
    if x==y:
        print("správně!")

