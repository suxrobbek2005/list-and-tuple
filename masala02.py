word = "Learning Python is fun!"



for i in word:
    print(i, end=" ")

t_tuple = tuple(i)
print (type(t_tuple))

length = len(t_tuple)

end_indx = word.index("fun")

print(f"Tuple ichidagi eng oxirgi so'zning indexi {end_indx}")