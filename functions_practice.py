# *! To check: python3 functions_practice.py 

# Activity (Python Local Setup and Function Practice)

def hello():
    print("Hello, I'm Tron from inside the function!")

hello() # Call the hello function to execute it


def pack(a, b, c): 
    return [a, b, c]

result = pack('apple', 'banana', 'orange')
print(result) # Accepts three arguments and returns the arguments as a list 


def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print("My lunchbox is empty!") # This is an if statement that checks if the list is empty 
    else:
        print("First I ate a", lunch_items[0])
        for item in lunch_items[1:]: # This is a for loop that iterates through the list and prints out each item
            print("Next I ate", item)

lunch_items = ['Meatball Sandwich', 'Baklava', 'Salmon Roll', 'Rice']
eat_lunch(lunch_items) # This function accepts a list of any length and prints out a series of strings based on the list items 
