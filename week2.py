my_list = []
print(f"1. Empty list: {my_list}")

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"2. After appending elements: {my_list}")

my_list.insert(1, 15) 
print(f"3. After inserting 15 at second position: {my_list}")

my_list.extend([50, 60, 70])
print(f"4. After extending with [50, 60, 70]: {my_list}")

my_list.pop()  # Removes and returns the last element
print(f"5. After removing last element: {my_list}")

my_list.sort()
print(f"6. After sorting in ascending order: {my_list}")

index_of_30 = my_list.index(30)
print(f"7. Index of value 30: {index_of_30}")

print(f"\nFinal list: {my_list}")