# Len's Slice
# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices =[2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
ctr = 0
pizza_and_prices = []
while ctr < 7:
  pizza_and_prices.append([prices[ctr], toppings[ctr]])
  ctr += 1
print(pizza_and_prices)
# sort - ascending
pizza_and_prices.sort()
print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
# use pop to remove the priciest pizza off the list. last of the list so no need to indicate index
pizza_and_prices.pop()
print(pizza_and_prices)
# insert element in list - indicate the correct index to insert
pizza_and_prices.insert(4,[2.5, "peppers"])
print(pizza_and_prices)
three_cheapest = pizza_and_prices[:5]
print(three_cheapest)