## Advanced Python Code Challenges: Control Flow

## 1. In Range

# Write your in_range function here:
def in_range(num, lower, upper):
  return num >= lower and num <= upper
# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

## 2. Same Name

# Write your same_name function here:
def same_name(your_name, my_name):
  #return your_name.casefold() == my_name.casefold() #codecademy expects (same_name("Alex", "alex") to be False)
  return your_name == my_name
# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

## 3. Always False

# Write your always_false function here:
def always_false(num):
  return num > num
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

## 4. Movie Review

# Write your movie_review function here:
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif 5 < rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

# 5. Max Number

# Write your max_num function here:
def max_num(num1, num2, num3):
  maxnum = max(num1, num2, num3)
  if sum([num1 == maxnum, num2 == maxnum, num3 == maxnum]) > 1:
    return "It's a tie!"
  else:
    return maxnum
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
#should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
