# Simple Currency Converter
def simple_converter():
    history = []
    while True:
        amount = input("Enter the amount you want to convert: ")
        from_currency = input("From currency (USD/EUR/CAD/INR/NPR): ").upper()
        to_currency = input("To currency (USD/EUR/CAD/INR/NPR): ").upper()
        try:
            amount = float(amount)
            if from_currency == "USD" and to_currency == "EUR":
                converted_amount = amount * 0.87  # Example conversion rate to EUR
                print(f"{amount} USD is equal to {converted_amount} EUR.")
                history.append(f"{amount} USD = {converted_amount} EUR")
        
            elif from_currency == "USD" and to_currency == "CAD":
                converted_amount = amount * 1.36  # Example conversion rate to CAD
                print(f"{amount} USD is equal to {converted_amount} CAD.")
                history.append(f"{amount} USD = {converted_amount} CAD")
            
            elif from_currency == "USD" and to_currency == "INR":
                converted_amount = amount * 82.50  # Example conversion rate to INR
                print(f"{amount} USD is equal to {converted_amount} INR.")
                history.append(f"{amount} USD = {converted_amount} INR")

            elif from_currency == "USD" and to_currency == "NPR":
                converted_amount = amount * 120.00  # Example conversion rate to NPR
                print(f"{amount} USD is equal to {converted_amount} NPR.")
                history.append(f"{amount} USD = {converted_amount} NPR")
                
            elif from_currency == "EUR" and to_currency == "USD":
                converted_amount = amount * 1.16  # Example conversion rate to USD
                print(f"{amount} EUR is equal to {converted_amount} USD.")
                history.append(f"{amount} EUR = {converted_amount} USD")
            
            elif from_currency == "EUR" and to_currency == "CAD":
                converted_amount = amount * 1.58  # Example conversion rate to CAD
                print(f"{amount} EUR is equal to {converted_amount} CAD.")
                history.append(f"{amount} EUR = {converted_amount} CAD")

            elif from_currency == "EUR" and to_currency == "INR":
                converted_amount = amount * 94.50  # Example conversion rate to INR
                print(f"{amount} EUR is equal to {converted_amount} INR.")
                history.append(f"{amount} EUR = {converted_amount} INR")

            elif from_currency == "EUR" and to_currency == "NPR":
                converted_amount = amount * 138.00  # Example conversion rate to NPR
                print(f"{amount} EUR is equal to {converted_amount} NPR.")
                history.append(f"{amount} EUR = {converted_amount} NPR")

            elif from_currency == "CAD" and to_currency == "EUR":
                converted_amount = amount * 0.63  # Example conversion rate to EUR
                print(f"{amount} CAD is equal to {converted_amount} EUR.")
                history.append(f"{amount} CAD = {converted_amount} EUR")

            elif from_currency == "CAD" and to_currency == "USD":
                converted_amount = amount * 0.74  # Example conversion rate to USD
                print(f"{amount} CAD is equal to {converted_amount} USD.")
                history.append(f"{amount} CAD = {converted_amount} USD")

            elif from_currency == "CAD" and to_currency == "INR":
                converted_amount = amount * 60.00  # Example conversion rate to INR
                print(f"{amount} CAD is equal to {converted_amount} INR.")
                history.append(f"{amount} CAD = {converted_amount} INR")

            elif from_currency == "CAD" and to_currency == "NPR":
                converted_amount = amount * 88.00  # Example conversion rate to NPR
                print(f"{amount} CAD is equal to {converted_amount} NPR.")
                history.append(f"{amount} CAD = {converted_amount} NPR")

            elif from_currency == "INR" and to_currency == "NPR":
                converted_amount = amount * 1.60  # Example conversion rate to NPR
                print(f"{amount} INR is equal to {converted_amount} NPR.")
                history.append(f"{amount} INR = {converted_amount} NPR")

            elif from_currency == "INR" and to_currency == "USD":
                converted_amount = amount * 0.012  # Example conversion rate to USD
                print(f"{amount} INR is equal to {converted_amount} USD.")
                history.append(f"{amount} INR = {converted_amount} USD")

            elif from_currency == "INR" and to_currency == "EUR":
                converted_amount = amount * 0.010  # Example conversion rate to EUR
                print(f"{amount} INR is equal to {converted_amount} EUR.")
                history.append(f"{amount} INR = {converted_amount} EUR")

            elif from_currency == "INR" and to_currency == "CAD":
                converted_amount = amount * 0.017  # Example conversion rate to CAD
                print(f"{amount} INR is equal to {converted_amount} CAD.")
                history.append(f"{amount} INR = {converted_amount} CAD")

            elif from_currency == "NPR" and to_currency == "USD":
                converted_amount = amount * 0.0083  # Example conversion rate to USD
                print(f"{amount} NPR is equal to {converted_amount} USD.")
                history.append(f"{amount} NPR = {converted_amount} USD")

            elif from_currency == "NPR" and to_currency == "INR":
                converted_amount = amount * 0.63  # Example conversion rate to INR
                print(f"{amount} NPR is equal to {converted_amount} INR.")
                history.append(f"{amount} NPR = {converted_amount} INR")

            elif from_currency == "NPR" and to_currency == "EUR":
                converted_amount = amount * 0.0072  # Example conversion rate to EUR
                print(f"{amount} NPR is equal to {converted_amount} EUR.")
                history.append(f"{amount} NPR = {converted_amount} EUR")

            elif from_currency == "NPR" and to_currency == "CAD":
                converted_amount = amount * 0.011  # Example conversion rate to CAD
                print(f"{amount} NPR is equal to {converted_amount} CAD.")
                history.append(f"{amount} NPR = {converted_amount} CAD")
            else:
                print("Unsupported currency pair. Please enter a valid currency pair (USD, EUR, CAD, INR, NPR).")
        except ValueError:
            print("Please enter a valid number for the amount.")
            continue
        if input("Do you want to perform another conversion? (y/n): ").lower() != 'y':
            print("\nConversion History:")
            print("-" * 20)
            for i, entry in enumerate(history, 1):
                print(f"{i}-> {entry}")
            print("-" * 20)
            break
            

    
def get_conversion_rate(from_currency):
    conversion_rates = {
            "USD": {"EUR": 0.87, "CAD": 1.36, "INR": 82.50, "NPR": 120.00},
            "EUR": {"USD": 1.16, "CAD": 1.58, "INR": 94.50, "NPR": 138.00},
            "CAD": {"USD": 0.74, "EUR": 0.63, "INR": 60.00, "NPR": 88.00},
            "INR": {"USD": 0.012, "EUR": 0.010, "CAD": 0.017, "NPR": 1.60},
            "NPR": {"USD": 0.0083, "EUR": 0.0072, "CAD": 0.011, "INR": 0.63}
        }
    return conversion_rates.get(from_currency, {})

def show_currency_conversion():
    amount = input("Enter the amount you want to convert: ")
    select_currency = input("Enter the currency you want to convert from (USD/EUR/CAD/INR/NPR): ").upper()
    currency = get_conversion_rate(select_currency)
    for rate in currency:
        print(f"{amount} {select_currency} is equal to {amount * currency[rate]} {rate}.")

if __name__ == "__main__":
    simple_converter()
    # show_currency_conversion()    
    
# def main():
#     # 1. Initialize an empty list to store the history
#     conversion_history = []
    
#     while True:
#         try:
#             km = input("\nEnter kilometers to convert to miles (or 'q' to quit): ")
            
#             if km.lower() == 'q':
#                 break
                
#             km_float = float(km)
#             miles = km_float * 0.621371
#             result = f"{km_float} km = {miles:.2f} miles"
            
#             # 2. Append the result to the history list
#             conversion_history.append(result)
#             print(result)
            
#         except ValueError:
#             print("Please enter a valid number.")

#     # 3. Display the history at the end of the program
#     print("\n" + "="*30)
#     print("SESSION CONVERSION HISTORY")
#     print("="*30)
#     if not conversion_history:
#         print("No conversions made.")
#     else:
#         for i, entry in enumerate(conversion_history, 1):
#             print(f"{i}. {entry}")
#     print("="*30)

# if __name__ == "__main__":
#     main()