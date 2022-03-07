new_list = [2,3,6,9,13,53,57,27,31]
odd_list = list(filter(lambda x:(x % 2 != 0) , new_list))
print(odd_list)