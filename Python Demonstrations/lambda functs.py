twice = lambda x:x*2
print(twice(10))

List = [1,5,4,6,8,11,3,12]

# Filter thru even numbers in list
new_list = list(filter(lambda x:(x%2 == 0), List))
print(new_list)

new_list = list(map(lambda x:x*2, List))
print(new_list)