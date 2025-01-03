l_list = [1, 2, 3, 4, 5, 6, 7, 5, 6]
print (l_list)

# list uzunligi topildi
lenght = len(l_list)
once_indx = l_list[0] # Birichi elementi topildi
center_indx = l_list[lenght // 2] # Markazdagi elemint topildi
end_indx = l_list[lenght - 1] # Oxirgi elementi topildi

print("Birinchi element = ", once_indx)
print("Markazdagi element = ", center_indx)
print ("Oxirgi element = ", end_indx)