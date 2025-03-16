def annuity_plan(PMT, R, n, t):
    A = PMT * (((1 + R / (n * 100)) ** (n * t) - 1) / (R / (n * 100)))
    return A

# Example usage
PMT = float(input("Enter Monthly Payment Amount: "))
R = float(input("Enter Annual Interest Rate (%): "))
n = int(input("Enter Number of Times Interest is Compounded per Year: "))
t = float(input("Enter Time (Years): "))

A = annuity_plan(PMT, R, n, t)
print(f"Total Amount from Annuity Plan: {A:.2f}")