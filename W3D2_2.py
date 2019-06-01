'Tyler Thorpe'

Hours = float(input("Enter the number of hours: "))
rate = float(input("Enter the rate per hour: "))

def payroll(Hours, rate):
    OTrate = rate * 1.5
    OT = Hours - 40
    if OT > 0:
        OTpay = OT * OTrate
        RegPay = 40 * rate
        TotalP = RegPay + OTpay
    else:
        TotalP = Hours * rate
    print("Your Gross Pay is: %.2f" %TotalP)

payroll(Hours, rate)