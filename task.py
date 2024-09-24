def task_1(numbers, N): # Numbers is a list of integer values, times is how many times to operatate (int)

    for _ in range(N):
        for i in range(len(numbers)):
            if numbers[i] % 2 == 0:
            # Remove 2
                numbers[i] -= 2
            else:
            # Add 2
                numbers[i] += 2
    return numbers

def task_2(N): # N is any integer value
    msg = "The most"
    if N % 1 == 0:
        msg += " brilliant"
    if N % 2 == 0:
        msg += " exciting"
    if N % 3 == 0:
        msg += " fantastic"
    if N % 4 == 0:
        msg += " virtuous"
    if N % 5 == 0:
        msg += " heart-warming"
    if N % 6 == 0:
        msg += " tear-jerking"
    if N % 7 == 0:
        msg += " beautiful"
    if N % 8 == 0:
        msg += " exhilarating"
    if N % 9 == 0:
        msg += " emotional"
    if N % 10 == 0:
        msg += " inspiring"
    msg += f" number is {N}!"
    return msg

def task_3(calc): # Calc is a string

    parts = calc.split()
    
    number1 = int(parts[0])
    number2 = int(parts[2])

    operator = parts[1]
    
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '//':
        if number2 == 0:
            result = -1
        else:
            result = number1 // number2
    
    return result

print(task_1([3, 4, 9], 3))