# Write an application to pre-sell a limited number of cinema tickets.
# Each buyer can buy up to 4 tickets. No more than 20 tickets can be sold total.
# Prompt the user for the desired number of tickets and then display the number of remaining tickets after their purchase.
# Repeat until all tickets have been sold. Then display the total number of buyers.
#
# Please use the following in your code:
#
# 1. two functions - your choice how you want to design this
# Total_Tickets_Sold
# Buyers
#
# 2. input
#
# 3. output
#
# 4. accumulator
#
# 5. if statement
#
# 6. loop
#
# You must also have a technical design document (refer to the Submitting Assignments Module).
#
# Submit both your .py file and .doc/.docx file in this assignment and these files must also be in your repository.
from symtable import Function

def total_tickets_sold():
    total_tickets = 0  # keeps track of all tickets sold
    total_buyers = 0 # Keeps track of the amount of buyers in the booth

    while True:
        try:
            tickets = int(input("How many tickets would you like? ")) # Gets a ticket input

            if tickets > 4:
                print("You can only have a maximum of 4 tickets.") # Makes sure only 4 tickets max will be purchased
            elif total_tickets + tickets > 20:
                print(f"Too many tickets have been sold. There are {20 - total_tickets} available.")
            else:
                total_tickets += tickets
                total_buyers += 1  # count the buyer

                if total_tickets == 20:
                    print("The total amount of tickets have been sold!")
                    break
                else:
                    print(f"You have purchased {tickets} tickets!")
                    print(f"Total tickets sold so far: {total_tickets}")
                    print(f"Total buyers so far: {total_buyers}")

        except ValueError:
            print("Please enter a valid number.")
    return total_buyers

def buyers(total_buyers):
    print(f"Total buyers: {total_buyers}")

buyers_count = total_tickets_sold()
buyers(buyers_count)
