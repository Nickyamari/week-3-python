def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount= (price * discount_percent) /100 
        final_price = price - discount_amount
        return final_price
    else:
        return price


original_price = float(input("enter the original price: "))
discount_percentage = float(input("enter the discount percentage: "))
final_price =calculate_discount (original_price, discount_percentage)

if discount_percentage >= 20:
    print(f"The final price after applying the discount is ${final_price} ")
else:
    print(f"No discount applied. The original price is ${original_price}")

    

        

