# Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.
#if num not present return -1

# Hint: Linear Searching will require searching a list for a given number.

sample_list = [10,23,45,70,11,15]
sample_target = 77

def find_num(num_list, target):
    for i in range(len(num_list)):
        if num_list[i] != target:
            continue
        elif num_list[i] == target:
            return f'Target number [{target}] found at index: {i}'
        else:
             return f'Target number [{target}] was not found'

print(find_num(sample_list, sample_target))

