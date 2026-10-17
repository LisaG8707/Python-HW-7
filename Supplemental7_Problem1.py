def simpleDiv(dividend, divisor):
    count = 0

    while dividend >= divisor:
        dividend = dividend - divisor
        count = count + 1

    return count

def main():
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))

    if dividend < 0 or divisor <= 0:
        print("Invalid input.")
    else:
        result = simpleDiv(dividend, divisor)
        print("The result is:", result)

main()
