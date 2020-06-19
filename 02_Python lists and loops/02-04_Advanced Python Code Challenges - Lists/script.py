## Advanced Python Code Challenges: Lists

## 1. Every Three Numbers

#Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))

## 2. Remove Middle

#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end + 1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

## 3. More Frequent Item

#Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) < lst.count(item2):
    return item2
  else:
    return item1
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

## 4. Double Index

#Write your function here
def double_index(lst, index):
  if index in range(len(lst)):
    lst[index] *= 2
    return lst
  else:
    return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

print(double_index([3, 8, -10, 12], 5))

## 5. Middle Item

#Write your function here
def middle_element(lst):
  length = len(lst)
  if length % 2 == 1:
    return lst[int(length / 2 - 0.5)]
  else:
    return sum(lst[int(length / 2 - 1):int(length / 2 + 1)]) / 2

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5, 75]))

print(middle_element([5, 2, -10, -4, 4, 5]))
