import winsound 
def beepSound():
   winsound.Beep(1000, 700)


import pandas as pd
import mysql.connector as sql

conn=sql.connect(host='Localhost',user='root', passwd='Bhavna@123', database='foodstore')
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS STAFF (SID TEXT, NAME TEXT, AGE TEXT,PROFILE TEXT, MOBILE TEXT);")

if conn.is_connected():
   print('successfully connected')



   

def about():
   print(' You are welcome in FOODSTORE MANAGEMENT Project. It has 13 choice It has used 3 Tables named as stock, Staff and bill')

def showlist():
    print('Display all details of Food available')
    print()
    df=pd.read_sql("select * from stock", conn)
    print(df)




def sortFood():
    print('sorting Food names in Ascending order')
    print()
    df=pd.read_sql("select * from stock ",conn)
    df=df.sort_values('fname')
    print(df)



def addstock():
    c1=conn.cursor()
    print("Food already in Stock")
    print()
    df=pd.read_sql("select * from stock", conn)
    print(df)
    L=[]
    fcode=input("ENTER Food Code:")
    L.append(fcode)
    fname=input("ENTER Food Name:")
    L.append(fname)
    dateofexp=input("ENTER Date Of Expiry:")
    L.append(dateofexp)
    quan=input("ENTER Quantity of Food:")
    L.append(quan)
    price=input("ENTER Price :")
    L.append(price)
    stock=(L)
    sql="insert into stock(fcode, fname, dateofexp, quan, price) values(%s, %s, %s, %s, %s)" %(fcode, fname, dateofexp, quan, price)
    c1.execute(sql,stock)
    conn.commit()
    print('Record inserted')

def updatestock():

    print('Change price of Food')
    c1=conn.cursor()
    print("Old Prices")
    df=pd.read_sql("select * from stock", conn)
    print(df)
    c1.execute("update stock set  =price +30 where fcode='101'")
    print("Price increased ")
    print()
    #conn.commit()
    df=pd.read_sql("select * from stock", conn)
    print(df)


def deletestock():
    print('Before any changes in Stock')
    print()
    df=pd.read_sql("select * from stock", conn)
    print(df)
    print()
    mc=conn.cursor()
    mc.execute("'delete from stock where fcode='117'")
    print("Record Deleted")
    df=pd.read_sql("select * from stock", conn)
    print(df)

#conn.commit()

def custorder():

   print("Food Codes and Names and Price of each Food is show below :")
   print()
   df=pd.read_sql("select * from stock", conn)
   print(df)
   print()
   print()
   print()
   print()
   print()
   x=int(input("Enter Your Food Code Please->"))
   n=int(input(" HOW MUCH QUANTITY YOU WANT TO BUY? "))

   if(x==111):

      print()
      print("you have Bought ice cream")
      print ("Price is 150 Rs. Each Strip")
      s=150*n

   elif(x==112):

      print()
      print ("you have Bought  white bread")
      print() 
      print("Price is 120 Rs. Each Strip")
      s=120*n

   elif(x==113):

      print()

      print("YOU HAVE Bought condiments")

      print()

      print ("Price is 220 Rs. 500 ml Bottle")

      s=220*n

   elif(x==114):

      print()

      print ("you have Bought samosha") 
     
      print()

      print ("Price is 60 Rs. per piece") 
     
      s=60*n

   elif (x==115):

      print()

      print ("YOU HAVE Bought kachori")

      print() 
      
      print ("Price is 20 Rs. per piece")

      s=20*n

   elif (x==116):

      print()

      print ("YOU HAVE Bought matar kulcha")

      print() 
      
      print("Price is 90 Rs.")

   elif (x==117):

     print()
     print ("YOU HAVE Bought fruit  juice 50 mg")
     print() 
     print ("Price is 50 Rs. Each 50 mg ")
     s=50*n

   else:

     print ("Please Enter CORRECT Food Code") 
     print ("your Bill is Rs. ",s,"\n")


def billrecords():

     print("Display contact No. of Customers and food purchased and its quantity and price")
           
     print()
     
     df=pd.read_sql("select * from bill", conn)
   
     print(df)


def recordorder():

   print("List and Price of Food")

   print()

   df=pd.read_sql("select * from stock", conn)

   print(df)

   print()

   print('insert into bill Records new sale ')

   mc=conn.cursor()

   L=[]

   mno=input("ENTER Mobile No.:")

   L.append(mno)

   itemcode=input("ENTER ITEM CODE:")

   L.append(itemcode)

   itemname=input("ENTER ITEM Name:")

   L.append(itemname)

   q=input("ENTER QUANTITY.:")

   L.append(q)

   price=input("ENTER PRICE Per Piece:")

   L.append(price)

   billrec=(L)

   sql="insert into bill(mobile, fcode, fname, quan, price) values(%s, %s, %s, %s, %s)" %(mno, itemcode, itemname, q, price)

   mc.execute(sql, billrec)

   conn.commit()

   print('Record inserted')

   
   
def sumbillbycust():

   df=pd.read_sql("select * from bill", conn)

   print(df)

   print('total money spent on various Food By a Customer')

   m=float(input("mobile: "))

   print('Your Order')

   print()

   print()

   qry="select fname, quan, price from bill where mobile=%s; "%(m,)

   df=pd.read_sql(qry,conn)

   print(df)

   qry1="select quan*price as 'TOTAL COST of EACH ITEM' from bill where mobile=%s; "%(m,)

   df=pd.read_sql(qry1,conn)

   print(df)

   print()

   print()

   qry2="select sum(quan*price) as 'You have to pay' from bill where mobile=%s; "%(m,)

   df=pd.read_sql(qry2, conn)

   print(df)

def groupby(): 
   mc=conn.cursor()

   df=pd.read_sql("select * from bill",conn)

   print(df)

   print("Total quantity of each item sold along with its code and name")

   print()

   mc.execute("select sum(quan) from bill where mobile='989110081'")

   for x in mc:

    print(x)


def searchbymobile():

   df=pd.read_sql("select * from bill", conn)

   print(df)

   print()

   print("Enter your mobile no. to find details of your purchasing")

   m=float(input("mobile : "))

   qry="select mname, quan, price from bill where mobile=%s; "%(m,) 
   
   df=pd.read_sql(qry,conn)

   print(df)

    #for x in mc:

     #print(x)   

def insertstaff():

   c1=conn.cursor()
   df=pd.read_sql("select * from staff", conn) 
   print(df)
   print("Old Staff Detail")
   print()
   print('Enter New Staff Information')
   print()
   SID=int(input('Enter ID of Staff:'))
   NAME=input('Enter Staff Name:')
   AGE=int(input('Enter Age:'))
   PROFILE=input('Enter Work Profile: ')
   MOBILE=int(input('Enter Mobile number:'))

  
   # sql_insert=f"insert into staff values("""+"str(sid)+",'"+name+"", 

   #c1.execute(sql_insert)
   c1.execute("INSERT INTO STAFF (SID,NAME,AGE,PROFILE,MOBILE) VALUES (%s,%s, %s, %s, %s)", (SID,NAME,AGE,PROFILE,MOBILE))

   print('SUCCESSFULLY REGISTERED')

   conn.commit()


def updatestaff():

   print('Before any Changes in the Staff Mobile No.')

   df=pd.read_sql("select * from staff", conn)

   print(df)

   print()

   print()

   mc=conn.cursor()

   mc.execute("update staff set mobile ='1234567' where name='Bhavna'")

   #conn.commit()

   df=pd.read_sql("select * from staff", conn)
   print("New Mobile Number")
   print(df)

def choice():
   
   opt=int(input("enter your choice: "))

   if opt==1:
      winsound.Beep(1000, 700)
      about()

   elif opt==2:
      winsound.Beep(1000, 700)
      showlist()

   elif opt==3:
      # winsound.Beep(1000, 300)
      beepSound()
      sortFood()

   elif opt==4:
      beepSound()
      addstock()
   
   elif opt==5:
      beepSound()
      updatestock()
   
   elif opt==6:
      beepSound()
      deletestock()
   
   elif opt==7:
      beepSound()
      custorder()  
   
   elif opt==8:
      beepSound()
      recordorder()
   
   elif opt==9:
     sumbillbycust()
   
   elif opt==10: 
      groupby()

   elif opt==11: 
      searchbymobile()

   elif opt==12: 
      insertstaff()

   
   elif opt==13: 
      updatestaff()

   else: 
      print('invalid option')



def menu():

   print()

   print("*************************************************")

   print(" FOOD STORE MANAGEMENT ")

   print("*************************************************")

   print()

   print() 

   print("1. About the project ")

   print("2. Display List of all food available in the stock")

   print("3. Display ALL food in Alphabetical Order")

   print("4. Add new food Purchased in Stock Table") 

   print("5. Update price of food")

   print("6. Delete a food detail from Table stock if not Available")

   print("7. Accept Customer Order and show Bill") 

   print("8. Enter all Customers Orders and maintain Record ")

   print("9. Total Bill to be paid customerwise ")

   print("10. Total food Bought according to Mobile No. (Group By) ")

   print("11. Total food bought and Price of each according to Mobile ")

   print("12. Add new Staff Detail in Staff Table")

   print("13. Update Staff Mobile No. ")

   print("****************************************")      

# ch = int(input("Enter choice"))
menu() 
choice()


