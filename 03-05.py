# Tuple yaratildi 
t_tuple = (1, 3, 4, 5, 6, 7 ,8, 9, 10)
print (type(t_tuple))
print (t_tuple) 

# Yaratilgan tuple listga o'zgartirlidi 
l_list = list(t_tuple)
l_list[2] = 34 # List qiymati o'zgartirildi

print ("O'zgartirligan qiymat: ")
print (type(l_list))
print (l_list)
