# Exercise 1: Calculate Area of a Triangle

def calculate_area_triangle(base, height):
    return ((base * height) / 2)



print('Exercise 1:', calculate_area_triangle(10, 5))


# Exercise 2: Calculate Simple Interest

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


print('Exercise 2:', simple_interest(1000, 5, 2))


# Exercise 3: Apply a Discount


def apply_discount(price, discount):
    discount_amount =  price * (discount/100)
    return price - discount_amount

print('Exercise 3:', apply_discount(100, 25))


# Exercise 4: Convert Temperature

def convert_temperature(temp, unit):
    celsius = unit == "C"
    fahrenheit = unit == "F"

    if celsius:
        return ( (temp * 9/5)+32) 
    elif fahrenheit:
        return ((temp -32)* 5/9)
    else:
        return "Invalid unit"

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


# Exercise 5: Sum to N


def sum_to(n):
    total = 0
    for num in range(1, n+1 ):
        total += num
    return total
print('Exercise 5:', sum_to(10))

# Exercise 6: Find the Largest Number

def largest(a,b,c):
    if a>=b and a >= c:
        return a
    elif b>=a and b >= c:
        return b
    else:
        return c

print('Exercise 6:', largest(1, 2, 3))

# # Exercise 7: Calculate a Tip


def calculate_tip(bill , tip_percentage):
    tip_amount = bill * (tip_percentage /100)
    return tip_amount
print('Exercise 7:', calculate_tip(50, 20))


# # Exercise 8: Calculate Product of Numbers

 
def product(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

print('Exercise 8:', product(2, 5, 5))


# # Exercise 9: Basic Calculator

def basic_calculator(num1, num2, operation):
    operations= {       
    "add": num1 + num2,
    "subtract": num1 - num2,
    "divide": num1 / num2,
    "multiply": num1 * num2
}    
    if operation in operations:
        return operations[operation]
    else:
        return "Invalid operation"

print('Exercise 9:', basic_calculator(10, 5, "subtract"))

