# 1. Double

nums = [4, 8, 15, 16, 23, 42]

double_nums = [num * 2 for num in nums]

# 2. Squares

nums = range(11)

squares = [num ** 2 for num in nums]

# 3. Add ten

nums = [4, 8, 15, 16, 23, 42]

add_ten = [num + 10 for num in nums]

# 4. Divide by two

nums = [4, 8, 15, 16, 23, 42]

divide_by_two = [num / 2 for num in nums]

# 5. Parity

nums = [4, 8, 15, 16, 23, 42]

parity = [num % 2 for num in nums]

# 6. Add hello

names = ["Elaine", "George", "Jerry", "Cosmo"]

greetings = ["Hello, " + name for name in names]

# 7. First character

names = ["Elaine", "George", "Jerry", "Cosmo"]

first_character = [name[0] for name in names]

# 8. Size

names = ["Elaine", "George", "Jerry", "Cosmo"]

lengths = [len(name) for name in names]

# 9. Opposites

booleans = [True, False, True]

opposite = [not bln for bln in booleans]

# 10. Same string

names = ["Elaine", "George", "Jerry", "Cosmo"]

is_Jerry = [name == "Jerry" for name in names]

# 11. Greater than two

nums = [5, -10, 40, 20, 0]

greater_than_two = [num > 2 for num in nums]

# 12. nested_lists = [[4, 8], [15, 16], [23, 42]]

product = [num1 * num2 for (num1, num2) in nested_lists]

# 13. Greater than

nested_lists = [[4, 8], [16, 15], [23, 42]]

greater_than = [num1 > num2 for (num1, num2) in nested_lists]

# 14. First only

nested_lists = [[4, 8], [16, 15], [23, 42]]

first_only = [num[0] for num in nested_lists]

# 15. Add with zip

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

sums = [sum(ls) for ls in zip(a,b)]

# 16. Divide with zip

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

quotients = [num2/num1 for (num1,num2) in zip(a,b)]

# 17. Capitals

capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]

locations = [capital + ", " + country for (capital, country) in zip(capitals, countries)]

# 18. Ages

names = ["Jon", "Arya", "Ned"]
ages = [14, 9, 35]

users = ["Name: " + name + ", Age: " + str(age) for (name, age) in zip(names, ages)]

# 19. Greater than with zip

a = [30, 42, 10]
b = [15, 16, 17]

greater_than = [num1 > num2 for (num1, num2) in zip(a,b)]
