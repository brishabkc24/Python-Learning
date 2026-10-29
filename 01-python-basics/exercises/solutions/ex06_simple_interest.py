"""Calculate simple interest and print the interest and total with separators."""

principal = float(input("Principal: "))
rate = float(input("Rate (% per year): "))
years = float(input("Years: "))

interest = principal * rate * years / 100
total = principal + interest

print(f"Interest: {interest:,.2f}")
print(f"Total: {total:,.2f}")
