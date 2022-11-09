print("Loan Calculator\n\nPrincipal amount=1000$\n for a period of 10 years\n at 5% interest rate")
principal =1000
rate =0.05

for _ in range(10):
  principal=principal+(principal*rate)
  print("Year",_+1,round(principal,2))