#mini project using python

#function to add fruit to the stock
def fruitadd(fruit,f_stock):
        if fruit not in f_stock:
            f_quantity=int(input('Enter how many number of fruit stock is add:'))
            c_price=int(input('Enter cost price of the each friut:'))
            s_price=int(input('Enter selling price of the each friut:'))
            
            #Here add fruit details to the stock
            f_stock[fruit_name]={'quantity':f_quantity,'cost_price':c_price,'selling_price':s_price}
            return True               
        else:
            return False

#function to remove an fruit from the stock or cart.
def fruitremove(fruit,f_stock):
        if fruit in f_stock:
                fruit_removed=f_stock.pop(fruit)
                return True
        else:
                return False

#funtion to modify the fruit details from the stock
def modifyfruit(fruit,modify,f_stock):
        if fruit in f_stock:
                if modify=='quantity':
                        quantity=int(input('Enter quantity of fruit to modify:'))
                        f_stock[fruit]['quantity']=quantity
                        return True
                elif modify=='cost price':
                       c_price=int(input('Enter cost price of fruit to modify:'))
                       f_stock[fruit]['cost_price']=c_price
                       return True
                elif modify=='selling price':
                       s_price=int(input('Enter selling price of fruit to modify:'))
                       f_stock[fruit]['selling_price']=s_price
                       return True
                        
        else:
                return False
        
#funtion to add fruits to cart
def addcart(fruit,cart,f_stock):
        if fruit in f_stock:
                if fruit not in cart:
                        f_quantity=int(input('Enter how many fruits do you want to add to cart:'))
                        if f_quantity<=f_stock[fruit]['quantity']:
                                cart[fruit]={'quantity':f_quantity,'price':f_stock[fruit]['selling_price']*f_quantity}
                                return True
                        else:
                                return 2
                else:
                        return 3
                                       
                             
        else:
                return False
        
#function to add price of fruits in cart.
def sumofcart(cart):
        total=0
        for i in cart.keys():
                total=total+cart[i]['price']
        return total

f_stock={
         'apple':{'quantity':100,'cost_price':5,'selling_price':10},
         'oranges':{'quantity':150,'cost_price':5,'selling_price':10},
         'promagranet':{'quantity':170,'cost_price':15,'selling_price':20},
         'mango':{'quantity':130,'cost_price':5,'selling_price':10},
        }
while True:
        print('*'*10,'FRUIT SHOP','*'*10)
        print('1.ShopKeeper View')
        print('2.Customer view')
        print('3.Exit')
        choice=int(input('Please enter an option to view:'))
        print()
        if  choice==1:
                username='fruit_shop'
                password='owner@123'
                user=input('username:')
                passw=input('password:')
                if username==user and password==passw:
                        
                        f_stock={
                                   'apple':{'quantity':100,'cost_price':5,'selling_price':10},
                                   'oranges':{'quantity':150,'cost_price':5,'selling_price':10},
                                   'promagranet':{'quantity':170,'cost_price':15,'selling_price':20},
                                   'mango':{'quantity':130,'cost_price':5,'selling_price':10},
                                   }
                        
                        print('WELCOME TO THE STORE')
                        while True:
                                print()
                                print('1.Add Items')
                                print('2.Remove Items')
                                print('3.Modify Existing Items')
                                print('4.View Stock')
                                print('5.Exit')
                                ch=int(input('Please Enter Your Option:'))
                                print()
                                if ch==1:
                                   while True:
                                       fruit_name=input('Enter a fruit name to add to stock:')
                                       result=fruitadd(fruit_name,f_stock)
                                       if result==True:
                                           print(fruit_name,'details added successfully')
                                           print()
                                           add_other=input('Do you want to add other fruit(yes/no):')
                                           if add_other=='no':
                                               break        
                                       else:
                                           print(fruit_name,'already in stock')
                                   print()
                                elif ch==2:
                                        while True:
                                                fruit_name=input('Enter a fruit name to remove from stock:')
                                                if fruitremove(fruit_name,f_stock)==True:
                                                        print(fruit_name,'details removed from the stock successfully')
                                                        print()
                                                        add_other=input('Do you want to remove other fruit(yes/no):')
                                                        if add_other=='no':
                                                                break
                                                else:
                                                        print(fruit_name,'not found in the stock')
                                                        add_other=input('Do you want to remove other fruit(yes/no):')
                                                        if add_other=='no':
                                                                break
                                        print()               
                                elif ch==3:
                                        while True:
                                                fruit_name=input('which fruit details do you want to modify:')
                                                modify=input('what do you want to modify from the stock(quantity/cost price/selling price):')
                                                if modifyfruit(fruit_name,modify,f_stock)==True:
                                                        print(fruit_name,'details modified successfully')
                                                        print()
                                                        add_other=input('Do you want to modify other fruit(yes/no):')
                                                        if add_other=='no':
                                                                break
                                                else:
                                                       print(fruit_name,'not found in the stock or entered option is wrong')
                                        print()
                                elif ch==4:
                                        print('*'*10,'Fruit Stock and Prices','*'*10)
                                        for k,v in f_stock.items():
                                                print('_'*44)
                                                for x,y in v.items():
                                                        print(k,'->',x,':',y,)
                                        print()
                                        
                                elif ch==5:
                                        print('THANK YOU FOR INSPECTING THE DETAILS OF THE STOCK')
                                        print('HAVE A GOOD DAY')
                                        print()
                                        break
                else:
                        print('Username And Password Is Not Correct,Try Again')
                        print()
                                
        if choice==2:
                cart={}
                print('*'*20,'WELCOME TO THE FRUIT STORE','*'*20)
                print()
                print('*'*10,'AVAILABLE FRUIT DETAILS','*'*10)
                for k,v in f_stock.items():
                        print()
                        print('Fruit Name:','*'*3,k,'*'*3)
                        print('-'*(20+len(k)))
                        print('Available quantity:',v['quantity'])
                        print('price:',v['selling_price'])
                while True:
                        print()
                        print('CHOOSE ONE OPTION TO SHOPPING')
                        print('-'*29)
                        print('1.Add fruit to cart')
                        print('2.Remove fruit from cart')
                        print('3.Modify quantity of fruit from cart')
                        print('4.View Cart or buy fruits')
                        print('5.Exit')
                        print()
                        ch=int(input('Enter your choice:'))
                        if ch==1:
                                while True:
                                        fruit=input('which fruit do you want to buy:')
                                        result=addcart(fruit,cart,f_stock)
                                        if result==True:
                                                print(fruit,'added to the cart successfully')
                                        elif result==2:
                                                print('your entered quantity is not available in the store')
                                        elif result==3:
                                                print(fruit,'already in the cart')
                                        else:
                                                print(fruit,'is not available in the store')
                                        add_other=input('Do you want to add other fruits(yes/no):')
                                        if add_other=='no'or not add_other=='yes':
                                                break
                        
                        if ch==2:
                                while True:
                                        fruit=input('Enter a fruit name to remove from cart:')
                                        if fruitremove(fruit,cart)==True:
                                                print(fruit,'removed from cart successfully')
                                                print()
                                                add_other=input('Do you want to remove other fruit(yes/no):')
                                                if add_other=='no' or not add_other=='yes':
                                                        break
                                        else:
                                                print(fruit,'not found in the cart')
                                                add_other=input('Do you want to remove other fruit(yes/no):')
                                                if add_other=='no' or not add_other=='yes':
                                                        break

                        if ch==3:
                                while True:
                                        fruit=input('Which fruit details do you want to modify:')
                                        if fruit in cart:
                                                quantity=int(input('Enter quantity of fruits to modify:'))
                                                if quantity<=f_stock[fruit]['quantity']:
                                                        cart[fruit]['quantity']=quantity
                                                        cart[fruit]['price']=quantity*f_stock[fruit]['selling_price']
                                                        print(fruit,'details modified in the cart successfully')
                                                else:
                                                        print('your entered quantity is not available in the store')
                                        else:
                                                print(fruit,'not found in the cart')
                                                print()
                                        other=input('Do you want to modify other fruits in cart(yes/no)')
                                        if other=='no' or not other=='yes':
                                                break
                                 

                        if ch==4:
                                print('*'*10,'CART','*'*10)
                                for k,v in cart.items():
                                        print('FRUIT NAME:','*'*3,k,'*'*3)
                                        for x,y in v.items():
                                                print(x,':','->',y)
                                total_amount=sumofcart(cart)
                                print('*'*5,'TOTAL AMOUNT IS:','Rs:',total_amount,'*'*5)
                                print()
                                buy=input('Do you want buy these items(yes/no):')
                                if buy=='yes':
                                        print()
                                        print('YOUR SHOPPING IS DONE,ITEMS ARE PACKED')
                                        print('THANK YOU FOR SHOPPING')
                                        print('VISIT AGAIN')
                                        print()
                        if ch==5:
                                print()
                                break
        if choice==3:
                print()
                print('THANK YOU FOR VISITING')
                print()
                break













                                                
