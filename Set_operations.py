# Set operations
"""Set is the collection of the unordered items.
    Each element in the set must be unique & immutable"""

nums = {7,8,2,10}
set2 = {15,2,78,1}

print(nums)
print(set2) #Ignore repeat values
print(type(set2))

null_set = set() # Empty set syntax

print(len(set2)) #Length of sets

print(min(set2))

print(max(set2))

print(sum(set2))

print(sorted(set2))

print(set2.union(nums))

print(set2.intersection(nums))

print(set2.difference(nums))

print(nums.difference(set2))

print(set2.symmetric_difference(nums))

print(set2.isdisjoint(nums))

print(set2.issubset(nums))

print(set2.issuperset(nums))