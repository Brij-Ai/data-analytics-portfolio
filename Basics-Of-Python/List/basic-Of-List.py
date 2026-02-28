nums = [1, 5, 3, 4]

print(nums[0])
print('-----')
for i in nums:
    print(i);

nums[1] = "brij"; # Mutable 
for i in nums:
    print(i);

i = 10
print(id(i))
