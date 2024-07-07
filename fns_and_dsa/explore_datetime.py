from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time as a string
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the formatted current date and time
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Calculate the date after adding a specified number of days to the current date.
    """
    # Prompt the user to enter the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Get the current date and time
    current_date = datetime.now()
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    # Format the future date as a string
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Print the formatted future date
    print(f"Future date: {formatted_future_date}")

def main():
    """
    Main function to execute the script.
    """
    # Display the current date and time
    display_current_datetime()
    # Calculate and display the future date
    calculate_future_date()

if __name__ == "__main__":
    # Run the main function if the script is executed directly
    main()
