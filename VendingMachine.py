import sys

menu = (input("1.Water =  Rs 60, 2.Cola = Rs 85 , 3.Gatorade = Rs 125.Type the number only : "))
enteredNumber = int(menu)
item =""
price =0.0
if enteredNumber == 1:
    price = 60.0;
    print("Price is %f"%(price))
    item = "Water Bottle"
elif enteredNumber == 2:
    price = 85.0;
    print("Price is %f"%(price))
    item = "Cola"
elif enteredNumber == 3:
    price = 125.0;
    print("Price is %f" %(price))
    item = "Gatorade"


else :
    sys.exit()

varfive = int(input("Please enter number of five rupees notes :"))
varten = int(input("Please enter number of ten rupees notes :"))
var20 = int(input("Please enter number of twenty rupees notes :"))
var50 = int(input("Please enter number of fifty rupees notes :"))

total = 5 * varfive + 10 * varten + 20 * var20 + 50 * var50

print("Total value of notes entered in machine is = RS %d" %(total))
if total<price:
    extra = price - total
    input("please add = %d "%(extra))

if total>price:
    change = total - price
    print("The machine is returning the change = RS %d"%(change))

if total==price:
          print ("Here is your %s. "%(item))





print ("Thanks for using this vending machine.")
