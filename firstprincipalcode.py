'''
def computerupsspecification(model,voltage , frequency,batterytype,batterycapacity,batterybackup,rechargetime,weight):
    if isinstance(model,float) and isinstance(voltage,float) and isinstance(frequency,float) and isinstance(batterytype,str) and isinstance(batterycapacity,float) and isinstance(batterybackup,float) and isinstance(rechargetime,float) and isinstance(weight,float):
        print(model,voltage , frequency,batterytype,batterycapacity,batterybackup,rechargetime,weight)

    else:
        raise TypeError("data type is not correct")
    if voltage == "420v ac":
        print("420v ac")

    else:
        raise ValueError("data is not correct")
    
        return voltage

computerupsspecification("digital600","230v ac" ,"50hz","sealed maintenance free","12volt 7Ah","12 to 20 mints","5 to 6 hours","6.1 kg")    

'''
def Electricbillpaidvianetbanking(website, tnebusername,password,consumernumber,Billingstatus,modeofpayment ):
    if isinstance(website,float) and isinstance(tnebusername,str) and isinstance(password,int) and isinstance(consumernumber,int) and isinstance(Billingstatus,str) and isinstance(modeofpayment,str):
        if website == "www.tnebnet.org":
            print("website is corect")

    else:
        if website == "www.indian.com":
            
            raise ValueError("website is not correct")
        
        print("website is not correct")
        
    if tnebusername == "agilan":
        print("username is not correct")

    else:
        if tnebusername == "shaikbaba":
            print("username is correct")
            return 0
Electricbillpaidvianetbanking("www.tnebnet.org","agilan",1234567 ,23456123,"paid/unpaid","netbanking")


def function200(x):
    if isinstance(x,int):
        if x==100:
            print(x*200)
            return 0


function200(100)

def function3(x,y):
    return x+y
e = function3(1,2)
    
print(e)
function3(1,2)

def function4(x):
    print(x)
    return 3*x
f = function4(4)
print(f)
    
    
 
