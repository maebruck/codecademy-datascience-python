# Advanced Python Code Challenges: Functions

## 1. First Three Multiples

# Write your first_three_multiples function here
def first_three_multiples(num):
  for i in range(1,4):
    print(num*i)
  return num*3
# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

## 2. Tip

# Write your tip function here:
def tip(total, percentage):
  return total*percentage/100
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

## 3. Bond, James Bond

# Write your introduction function here:
def introduction(first_name, last_name):
  return (last_name + ", " + first_name + " " + last_name)
# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

## 4. Dog Years

# Write your dog_years function here:
def dog_years(name, age):
  return "%s, you are %i years old in dog years" % (name, age*7)
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

## 5. All Operations

# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
  arith1 = a+b
  arith2 = c-d
  arith3 = arith1*arith2
  print(arith1)
  print(arith2)
  print(arith3)
  return arith3 % a
# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
