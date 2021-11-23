import math


def print_duration(month):
    year = int(month / 12)
    remainingMonth = month - year * 12
    print("-> year:", year, ", month:", remainingMonth)


def print_money(money):
    rounded_money = math.floor(money * 10)/10.0
    print("%.1f" % rounded_money + "$")


def print_entry(loan_amount, int_rate, month):
    print("---------------------------------")
    print_duration(month)
    loan_amount_with_interest = float(
        loan_amount + (loan_amount / 100 * int_rate/12 * month))
    print("Total Payment:")
    print_money(loan_amount_with_interest)
    print("Monthly Payment:")
    print_money(loan_amount_with_interest / float(month))
    print("---------------------------------")


def print_full_report(loan_amount, int_rate, max_year, max_month, iteration_interval):
    total_month = max_year * 12 + max_month
    i = iteration_interval
    while i <= total_month:
        print_entry(loan_amount, int_rate, i)
        i += iteration_interval


print("....................................................")
print("*.*.*.*.*. Welcome To Interest Calculator .*.*.*.*.*")
print("....................................................\n")

name = input("Please enter your name: ")
# kredi tutarı ($ s cinsinden, ör. 1000.50)
loan_amount = float(input("Loan amount: "))
# yıllık faiz oranı (dalgalı yüzde olarak, ör. 1.5 veya 50 veya 150 veya ...)
annual_interest_rate = float(input("Interest rate (per year): "))
print("-> TIME LENGTH")
# maksimum yıl (tam sayı, ör. 0 veya 1 veya 2 veya ...)
max_year = int(input("\tLoan term in years: "))
# en fazla ay (tam sayı, ör. 0 veya 6 veya 18 veya ...)
max_month = int(input("\tLoan term in months: "))
# yineleme aralığı (ay cinsinden tam sayı)
iteration_interval = int(input("\tIteration in months: "))
print("....................................................\n")

print("Report for %s" % name)
print_full_report(loan_amount, annual_interest_rate,
                  max_year, max_month, iteration_interval)
