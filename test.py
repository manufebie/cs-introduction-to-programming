# defined function "main"
def main():
    # calls function "select"
    select()
# defined function "select"
def select():
    # prompts user for integer input
    times = int(input("How many numbers do you want to enter? "))
    # creates an empty list
    results = []
    # does a loop as much times as the value of the inputted integer
    for i in range(0, times):
        # prompts user for an integer to be decided (ODD or EVEN)
        num = int(input("Enter Number: "))
        # declares number as ODD, when no remainder is produced when dividing the number by 2
        if (num % 2 != 0):
            # adds string "Bob" in the "results" list
            results.append("Bob")
        # declares number as EVEN, when a remainder is produced when dividing the number by 2
        elif (num % 2 == 0):
            # adds string "Alice" in the "results" list
            results.append("Alice")
    # prints the whole list
    print(results)
# calls function "main"
main()