#medical_insurance.py
# Add your code here
# Create an empty dictionary called medical_costs
medical_costs = {}

# Add key value pairs
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

# one line update of dictionary
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

print(medical_costs)

#update Vinay's medical cost to 3325.0
medical_costs["Vinay"] = 3325.0
print(medical_costs)

# Get average medical cost
# Get total cost
total_cost = 0
for cost in medical_costs.values():
    total_cost += cost
print(total_cost)
# proceed to calculate the average
average_cost = total_cost / len(medical_costs)
print(f"Average Insurance Cost: {average_cost}")

# List Comprehension to Dictionary
names = ["Marina","Vinay","Connie","Isaac","Valentina"]
ages = [27,24,43,35,52]

# zip the two lists
zipped_ages = zip(names,ages)

# create names to ages dictionary
names_to_ages = {key: value for key, value in zipped_ages}
print(names_to_ages)

# Get Marina's age
marina_age = names_to_ages.get("Marina",None)
print(f"Marina's age is {marina_age}")

# Use dictionary to create a medical database
medical_records = {}

# Input the medical records
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

print(medical_records)

# Display Connie's insurance cost
print(f"Connie's insurance is " + str(medical_records["Connie"]["Insurance_cost"]) + " dollars.")

# remove Vinay from the list
medical_records.pop("Vinay")

# display medical records
for name, record in medical_records.items():
    print(name + " is a " + str(record["Age"]) + \
          " year old " + record["Sex"] + " " + record["Smoker"] \
         + " with a BMI of " + str(record["BMI"]) + \
         " and insurance cost of " + str(record["Insurance_cost"]))
  