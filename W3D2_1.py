'Tyler Thorpe'

Hours = int(input("Enter the number of hours: "))
RPH = int(input("Enter the rate per hour: "))

OTrate = RPH * 1.5
OT = Hours - 40

if OT > 0:
    OTpay = OT * OTrate
    RegPay = 40 * RPH
    Total = RegPay + OTpay
    print(Total)
else:
    RegPay = Hours * RPH
    print(RegPay)