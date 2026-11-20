tickets_prices = {
    "under_13": "3$",
    "13_to_16": "5$",
    "17_to_50": "5$",
    "over_50": "only 1$",
}
snacks = ["popcorn", "soda", "choclate", "sinckers", "candy"]

customer_name = input("Hello...?, Whats your name?\n").strip().title()
print(f"Hello, {customer_name} Welcome in our cinema market !")

age = int(input(f"How old are you in numbers, {customer_name}?: ").strip())

if age <= 13:
    tier = "under_13"
elif age >= 13 and age <= 16:
    tier = "13_to_16"
elif age > 16 and age <= 50:
    tier = "17_to_50"
else:
    tier = "over_50"

print(f"Ticket price is just {tickets_prices[tier]} for you {customer_name}!")