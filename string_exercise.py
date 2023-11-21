def username_generator(first_name, last_name):
  user_name = first_name[:3] + last_name[:4]
  # password_generator(user_name)
  return user_name

def password_generator(user_name):
  password=user_name[-1] + user_name[:len(user_name)-1]
  print("initial: {}".format(password))
  for ctr in range(len(user_name)):
    password[ctr] = user_name[ctr-1]
  return password

print(username_generator("Clifford","DelaCruz"))
print(password_generator("CliDela"))