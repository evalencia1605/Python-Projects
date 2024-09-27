mylist = ["banana", "apple", "cherry"]
print(mylist)

if "apple" in mylist:
    print("yes")
else:
    print("not in my list")

mylist.append("lemon") #for appending at the end of the list

print(mylist)

mylist.insert(1, "watermelon") #for inserting an item in and index position
print(mylist)

print(len(mylist))

reverse_list = mylist.reverse() #reversing a list
print(mylist)


