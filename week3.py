def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

def main():
    
        # Get input from user
        original_price = float(input("Enter the original price of the item: $"))
        discount_percentage = float(input("Enter the discount percentage: "))
        
        # Calculate the final price using our function
        final_price = calculate_discount(original_price, discount_percentage)
        
        # Check if discount was applied and print appropriate message
        if discount_percentage >= 20:
            print(f"\nDiscount applied! ({discount_percentage}%)")
            print(f"Original price: ${original_price:.2f}")
            print(f"Final price: ${final_price:.2f}")
            print(f"You saved: ${original_price - final_price:.2f}")
        else:
            print(f"\nNo discount applied (discount must be 20% or higher)")
            print(f"Price remains: ${final_price:.2f}")


# Run the program
main()