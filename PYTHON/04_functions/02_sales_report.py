def fetch_sales(month):
    print(f"Sales fetched in month of {month}")

def filter_valid_orders(month):
    print(f"Valid Orders have extracted in the month of {month}")

def summarize_data(month):
    print(f"Data has summarized in the month of {month}")      

def generate_report(month):
    fetch_sales(month)
    filter_valid_orders(month)
    summarize_data(month)
    print(f"All set in the month {month}!!")      


month = input("Enter month name : ").lower()
generate_report(month)