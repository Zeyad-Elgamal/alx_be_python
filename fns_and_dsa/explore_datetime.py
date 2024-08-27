# Import necessary components from datetime module
from datetime import datetime, timedelta

# Function to display current date and time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

# Function to calculate a future date
def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    return formatted_future_date

# Main function to prompt user and display results
if __name__ == "__main__":
    display_current_datetime()
    
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = calculate_future_date(days_to_add)
    print(f"Future date: {future_date}")
