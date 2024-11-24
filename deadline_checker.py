from datetime import datetime

# Step 1: Ask the user for the deadline date and time
deadline_input = input("Enter the deadline (e.g., 2024-11-15 17:00): ")

# Step 2: Convert the input string to a datetime object
deadline = datetime.strptime(deadline_input, "%Y-%m-%d %H:%M")

# Step 3: Get the current date and time
now = datetime.now()

# Step 4: Compare the current time to the deadline and display the result
if now > deadline:
    print("The deadline has passed! 😢")
elif now.date() == deadline.date():
    print("The deadline is today! 🕒 Don't miss it!")
else:
    time_remaining = deadline - now
    days_remaining = time_remaining.days
    print(f"The deadline is in {days_remaining} day(s). Keep working! 🚀")