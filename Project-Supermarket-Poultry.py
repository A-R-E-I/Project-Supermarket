import os.path
from os import path

def storage():
    global Quantities, Cart, cartItem, Cost
    Quantities = []
    Cart = []
    cartItem = []
    Cost = []
    Askinfo()
    
def Askinfo():
    global initialprice, askitem
    print("\nWhat product would you like to purchase?");
    print("\n");
    askitem = str(input(" pencils($0.30) \n composition notebooks($1.25) \n book bags($30) \n erasers($1) \n folders($1.50) \n Enter here:"));
    match(askitem):
        case("pencils"):
            initialprice = 0.30
            Calcprice();
        case("composition notebooks"):
            initialprice = 1.25
            Calcprice();
        case("book bags"):
            initialprice = 30
            Calcprice();
        case("erasers"):
            initialprice = 1
            Calcprice();
        case("folders"):
            initialprice = 1.50
            Calcprice();
        case(_):
            print("Please type “pencils”, “composition notebooks”,  “book bags”, “erasers”, or “folders”");
            Askinfo();
            
def Calcprice():
    global Askamount
    Askamount = str(input("How many do you want? (Enter number from 1-100)"));
    amountlen = len(Askamount);
    isletter = ord(Askamount[0:1:2])
    if(int(isletter) >= 48 and int(isletter) <= 57 and amountlen <= 3):
        match(float(Askamount) > 0 and float(Askamount) <= 100):
            case(True):
                Checknum();
            case(False):
                print("Please enter a whole number from 1-100");
                Calcprice();
    else:
        print("Please enter a whole number from 1-100");
        Calcprice();
    
    
def Checknum():
    modnum = float(Askamount) % 1
    if(modnum == 0):
        Quantities.append(Askamount);
        price = int(Askamount) * initialprice
        Addcart(price);
    else:
        print("Please enter a whole number from 1-100");
        Calcprice();
    
    
def Addcart(money):
    money = round(money,2)
    AddtoCart = str(input("The cost is $" + str(money) + " Add to cart?(Enter 1 for yes and 2 for no.)"));
    match(AddtoCart):
        case("1"):
            Cart.append(money);
            match(askitem):
                case("pencils"|"composition notebooks"|"erasers"|"book bags"|"folders"):
                    cartItem.append(askitem);
            Cost.append(money);
            Results();
        case("2"):
            money = 0
            print("Purchase canceled")
            Askinfo();
        case(_):
            print("please enter 1 or 2");
            Addcart(money);
                    
def Results():
    Whatelse = str(input("Anything else that you want to buy?(Enter 1 for yes and 2 for no.)"));
    match(Whatelse):
        case("1"):
            Askinfo();
                    
        case("2"):
            totalprice = 0
            for i in range(0,len(cartItem)):
                totalprice = totalprice + Cost[i]
                print("You purchased " + str(Quantities[i]) + " " + cartItem[i] + ", the cost is $" + str(Cart[i]));
            
            print("The total price is $" + str(totalprice));
                
        case(_):
            print("please enter 1 or 2");
            Results();
def main():
    storage();
  
if __name__=="__main__":
    main();
      
                 
