# Yongdong Xi
def food_costs(groceries,costs): 
    for grocerie in groceries:
    # Separate the single list from the large lists
        for index,fruit in enumerate(grocerie):
        # Operate independently of the elements in the list
            grocerie[index] = fruit + ': $' + str(costs[0])
            # Add to the original list according to the order and required format
            del costs[0]
            # Delete used data
        groceries_mod = groceries
    return groceries_mod


def factorial(number):
    total = 1
    # Any positive integer number greater than zero is bigger or equal to 1
    num = 1
    # Any positive integer number greater than zero should be multiplied from 1
    if number == 0:
    # if number equals to 0
        total = 0
    else:
        while num <= number:
        # when number is a positive integer number, select a positive integer number smaller than it without repetition       
            total = num * total
            # multiply numbers less than or equal to the required factorial number one by one
            num += 1
            # find the next positive integer number
    return total

print(factorial(5))


def fib_nums(number):
    if number == 1:
        return [0]
    # Only the first number of fib is required
    if number == 2:
        return [0,1]
    # Only the first two numbers of fib are required
    fib = [0,1]
    while number > len(fib):
    # When you need to find fib lst greater than two
    # the loop will continue until the current list does not reach the specified length
        fib.append(fib[-1] + fib[-2])
        # Adds the last two numbers of the current sequence
    return fib 
