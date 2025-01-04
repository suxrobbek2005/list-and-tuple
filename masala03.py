t_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)
print("Birinchi tuple:\n", t_tuple)

length = len(t_tuple)

thrid_index = t_tuple[0:length - 1:3]

print("O'zgartirilgan tuple:\n", thrid_index[::-1])

any_index = t_tuple.index(20)

print (f"Tuple ichidagi '20' ning indexi {any_index}")


