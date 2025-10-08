def addition(x, y):
    print(x + y)


addition(13, 14)
addition(25, 24)

def determine_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 89:
        return "B"
    elif 70 <= score < 89:
        return "C"
    elif 60 <= score < 79:
        return "E"
    elif 0 <= score < 69:
        return "F"
    else:
        return "Invalid score"

def simple_calculator(value1, value2, operation):
     if operation == "add":
        return value1 + value2
    elif operation == "subtract":
        return value1 - value2
    elif operation == "multiply":
        return value1 * value2
    elif operation == "divide":
        return value1 / value2
    else:
        return "Error: Division by zero"
    else:
        return "Invalid operation"  


            
