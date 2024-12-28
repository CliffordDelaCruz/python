import requests
import datetime

# API Base URL (Use a valid API key)
API_URL = "https://open.er-api.com/v6/latest/"

def fetch_exchange_rates(base_currency):
    """Fetch exchange rates for the given base currency."""
    try:
        response = requests.get(f"{API_URL}{base_currency}")
        response.raise_for_status()
        data = response.json()
        if data["result"] == "success":
            return data["rates"]
        else:
            print("Error fetching exchange rates. Please try again.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def convert_currency(amount, rate):
    """Convert currency based on rate."""
    return round(amount * rate, 2)

def save_results(results):
    """Save conversion results to a file."""
    filename = "currency_conversion_results.txt"
    with open(filename, "a") as file:
        file.write("\n".join(results) + "\n")
    print(f"Results saved to {filename}.")

def main():
    print("Welcome to the Currency Exchange Rate Tracker!")
    base_currency = input("Enter the base currency (e.g., USD): ").upper()

    rates = fetch_exchange_rates(base_currency)
    if not rates:
        return

    print("\nAvailable currencies:", ", ".join(list(rates.keys())[:10]), "...")
    target_currencies = input("Enter target currencies (comma-separated, e.g., EUR, GBP): ").upper().split(",")

    amount = float(input(f"Enter the amount in {base_currency}: "))
    results = [f"Base currency: {base_currency}"]
    results.append(f"Amount: {amount} {base_currency}")

    print("\nConversion Results:")
    for target in target_currencies:
        target = target.strip()
        if target in rates:
            converted_amount = convert_currency(amount, rates[target])
            result = f"{amount} {base_currency} = {converted_amount} {target}"
            print(result)
            results.append(result)
        else:
            print(f"Currency {target} is not available.")

    # Save the results
    results.append(f"Timestamp: {datetime.datetime.now()}")
    save_results(results)

if __name__ == "__main__":
    main()