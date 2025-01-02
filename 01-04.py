# O'zgaruchilar yaratildi 

number1 = 2
number2 = 6
number3 = 4
number4 = 9
to_save = 0

print (number1)
print (number2)
print (number3)
print (number4)

print ("Almashtirilgan qiymat:\n")
if number1 < number2 :
    to_save = number1
    number1 = number2
    number2 = to_save

if number3 < number4:
    to_save = number3
    number3 = number4
    number4 = to_save
  
print (number1)
print (number2)
print (number3)
print (number4)


