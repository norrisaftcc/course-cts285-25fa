def datamon_calculator():
    print("Welcome to DataMon: Arithmetic Trainer")
    print("Enter expressions with single-digit numbers (e.g., 3 + 4). Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter expression: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye from DataMon!")
            break

        try:
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError("Invalid format. Use: digit operator digit")

            a, op, b = parts
            if not (a.isdigit() and b.isdigit()):
                raise ValueError("Only single-digit numbers are allowed.")

            a, b = int(a), int(b)

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            else:
                raise ValueError("Unsupported operator. Use +, -, or *.")

            print(f"Result: {a} {op} {b} = {result}\n")

        except Exception as e:
            print(f"Error: {e}\n")

# Run the calculator
if __name__ == "__main__":
    datamon_calculator()
