nums = input("enter numbers separated by space: ").split()

nums = [int(x) for x in nums]

print("Largest number: ", max(nums))