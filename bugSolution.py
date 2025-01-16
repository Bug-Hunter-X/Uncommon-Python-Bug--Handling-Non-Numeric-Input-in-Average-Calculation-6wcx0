def calculate_average(numbers):
    if numbers is None or not numbers:
        return 0  # Handle None and empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle list with no numeric elements
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_mixed_list = [1, 2, 'a', 4, 5]
average_mixed = calculate_average(my_mixed_list)
print(f"The average of a mixed list is: {average_mixed}")

my_none_list = None
average_none = calculate_average(my_none_list)
print(f"The average of None is: {average_none}")
