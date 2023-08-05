# Write a Python function called max_num()to find the maximum of three numbers
def max_num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Write a Python function called rev_string() to reverse a string
def rev_string(input_string):
    return input_string[::-1]

# Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound

if num_within(num, lower_limit, upper_limit):
    print(f"{num} is within the range [{lower_limit}, {upper_limit}].")
else:
    print(f"{num} is outside the range [{lower_limit}, {upper_limit}].")

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle
def pascal(n):
    if n <= 0:
        return
    
    def next_row(row):
        return [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]

    row = [1]
    for _ in range(n):
        print(row)
        row = next_row(row)