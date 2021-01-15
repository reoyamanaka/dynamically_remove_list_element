sample_list = [1, 2, 3, 4, "p", "r", "j", 0]

counter = len(sample_list) - 1

print(sample_list)

while counter > -1:
    del sample_list[counter]
    counter -= 1

print(sample_list)





