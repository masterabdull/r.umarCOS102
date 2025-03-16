def simple_interest(P, R, T):
    A = P * (1 + (R / 100) * T)
    return A

# Example usage
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Annual Interest Rate (%): "))
T = float(input("Enter Time (Years): "))

A = simple_interest(P, R, T)
print(f"Total Amount after Simple Interest: {A:.2f}")

