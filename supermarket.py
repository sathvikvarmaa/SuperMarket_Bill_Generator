from datetime import datetime
name = input("Enter Your Name ")
# Products List
goods = """
    1.Sugar    30/Kg
    2.Rice     75/Kg
    3.Dal      40/Kg
    4.Peanut   30/Kg
    5.Jagguar  40/Kg
    6.Ravva    45/Kg
"""
#declarations
amount=0
ilist=[]
qlist=[]
plist=[]
price_list=[]
total_price=0
finalamount=0

goods_list = {"sugar":30,"rice":75,"dal":40,"peanut":30,"jagguar":40,"ravva":45 }
option = int(input("Enter Option 1 to show List "))
if option ==1:
    print(goods)
for i  in range(len(goods_list)):
    inp=int(input("If you want to buy press 1 or 2 for exit: "))
    if inp==2:
        break
    if inp==1:
        buy = input("Enter Products ")
        quant = int(input("Enter Quantity "))
        if buy in goods_list.keys():
            amount = quant*(goods_list[buy]) 
            price_list.append((buy,quant,goods_list,amount))
            total_price+=amount
            ilist.append(buy)
            qlist.append(quant)
            plist.append(amount)
            gst=(total_price*5)/100
            finalamount=gst+total_price
        else:
            print("Sorry your entered item is not available")
    else:
            print("You enterd wrong number")

    inp=input("Can i bill the items yes or no ")
    if inp=='yes':
         pass
         if finalamount!=0:
            print(25*"=","Kirana Store",25*"=")
            print(25* " ","Vizianagaram")
            print("name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("Sno",8*" ",'Items',8*" ",'Quantity',2*" ",'price')
            
            for i in range(len(price_list)):
                print(i,10*' ',ilist[i],10*' ',qlist[i],10*' ',plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',total_price)
            print("gst amount",50*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'FinalAmount:','Rs',finalamount)
            print(75*"-")
            print(25*" ",'Thanks For Visting')


          
    