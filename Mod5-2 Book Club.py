# CSU Global Book Club Points Program

print('Welcome to CSU Global Bookstore Book Club!\n')

# Ask how many books they purchased
books_bought = int(input("Enter the number of books purchased this month: "))
points = 0

# Determine points based on number of books
if books_bought < 2:
    points = 0
elif books_bought < 4:
    points = 5
elif books_bought < 6:
    points = 15
elif books_bought < 8:
    points = 30
else:
    points = 60

# Display the point total
print(f"\n{books_bought} books purchased this month earns you {points} points.")

