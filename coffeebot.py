'''create a Python chatbot that can help cut the wait time of a normal coffee run by taking customers’ orders in advance. '''

# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  print("Alright, that's a " + size + ", " + drink_type + "!")
  name = input("Can I get your name please? ")
  print("Thanks " + name + "! Your drink will be ready shortly.")

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")
  retsize=''
  if res == 'a' or res == 'A':
    retsize='Small'
    return retsize
  elif res == 'b' or res == 'B':
    retsize='Medium'
    return retsize
  elif res == 'c' or res == 'C':
    retsize='Large'
    return retsize
  else:
    #perform recursive selection
    print_message()
    return get_size()

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ")
  retdrinktype=''
  if res == 'a' or res == 'A':
    retdrinktype='Brewed Coffee'
    return retdrinktype
  elif res == 'b' or res == 'B':
    retdrinktype='Mocha'
    return retdrinktype
  elif res == 'c' or res == 'C':
    retdrinktype=order_latte()
    return retdrinktype
  else:
    #perform recursive selection
    print_message()
    return get_drink_type()

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ")
  retlattetype =''  
  if res == 'a' or res == 'A':
    retlattetype='Latte'
    return retlattetype
  elif res == 'b' or res == 'B':
    retlattetype='Non-fat Latte'
    return retlattetype
  elif res == 'c' or res == 'C':
    retlattetype='Soy Latte'
    return retlattetype
  else:
    #perform recursive selection
    print_message()
    return order_latte()

# Call coffee_bot()!
coffee_bot()
