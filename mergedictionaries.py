items1 = input("enter key-value pairs for first dictionary: ").split()

items2 = input("enter key-value pairs for second dictionary: ").split()

dict1 = {items1[i]: items1[i+1] for i in range(0,len(items1),2)}

dict2 = {items2[i]: items2[i+1] for i in range(0,len(items2),2)}

merged = dict1.copy()

merged.update(dict2)

print("Merged dictionary: ", merged)