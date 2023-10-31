''' In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

1. Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
2. Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
3. Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping. '''

weight = 41.5
cost = 0
# Ground Shipping
if weight <= 2:
  cost += (weight * 1.50) + 20.00
  print("Cost: $"+ str(cost))
elif weight > 2 and weight <= 6:
  cost += (weight * 3.00) + 20.00
  print("Cost: $"+ str(cost))
elif weight > 6 and weight <= 10:
  cost += (weight * 4.00) + 20.00
  print("Cost: $"+ str(cost)) 
elif weight > 10:
  cost += (weight * 4.75) + 20.00
  print("Cost: $"+ str(cost))
else:
  print("Error!")

# Premium Shipping
premium_shipping = 125.00
print("Ground shipping premium: $" + str(premium_shipping))

# Drone Shipping
drone_cost = 0
if weight <= 2:
  drone_cost += (weight * 4.50)
  print("Drone Cost: $"+ str(drone_cost))
elif weight > 2 and weight <= 6:
  drone_cost += (weight * 9.00)
  print("Drone Cost: $"+ str(drone_cost))
elif weight > 6 and weight <= 10:
  drone_cost += (weight * 12.00)
  print("Drone Cost: $"+ str(drone_cost)) 
elif weight > 10:
  drone_cost += (weight * 14.25)
  print("Drone Cost: $"+ str(drone_cost))
else:
  print("Error!")