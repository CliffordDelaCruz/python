#med_insurance_cost.py
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

medical_records = list(zip(insurance_costs,names))

print(medical_records)

num_medical_records = len(medical_records)

print("There are {} medical records".format(num_medical_records))

first_medical_record = medical_records[0]

print("Here is the first medical record: {}".format(first_medical_record))

medical_records.sort()
print("Here are the medical records sorted by insurance cost: {}".format(medical_records))

cheapest_three = medical_records[:3]

print("Here are the three cheapest insurance costs in our medical records: {}".format(cheapest_three))

priciest_three = medical_records[-3:]

print("Here are the three most expensive insurance costs in our medical records: {}".format(priciest_three))

occurrences_paul = names.count("Paul")
print("There are {} individuals with the name Paul in our medical records.".format(occurrences_paul))


