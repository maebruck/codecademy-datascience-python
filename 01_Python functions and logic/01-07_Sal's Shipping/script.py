def rate(weight):
  if weight <= 2:
    return 1.5
  elif 2 < weight <= 6:
    return 3
  elif 6 < weight <= 10:
    return 4
  else:
    return 4.75
def ground_cost(weight):
  flat = 20
  return rate(weight) * weight + flat

ground_premium_cost = 125

def drone_cost(weight):
  flat = 0
  premium = 3
  return rate(weight) * premium * weight + flat

def cheapest_shipping(weight):
  min_shipping = min(ground_cost(weight), ground_premium_cost, drone_cost(weight))
  if min_shipping == ground_cost(weight):
    print("The cheapest method is ground shipping at $", min_shipping)
  elif min_shipping == ground_premium_cost:
    print("The cheapest method is Premium ground shipping at $", min_shipping)
  elif min_shipping == drone_cost(weight):
    print("The cheapest methos is drone shipping at $", min_shipping)

cheapest_shipping(4.8)
cheapest_shipping(41.5)
