def compound_interest(P, R, n, t):
    A = P * (1 + R / (n * 100)) ** (n * t)
    return A

# Example usage
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Annual Interest Rate (%): "))
n = int(input("Enter Number of Times Interest is Compounded per Year: "))
t = float(input("Enter Time (Years): "))

A = compound_interest(P, R, n, t)
print(f"Total Amount after Compound Interest: {A:.2f}")