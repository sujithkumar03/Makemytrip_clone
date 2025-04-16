def flight():
    global amount
    print('''WELCOME TO FLIGHT BOOKING SECTION !!!!''')
    d = int(input("Enter Your Type of Journey : 1. International   2. Domestic "))
    print("Enter your Source and Destination places : ")
    fro = input("Source : ")
    to = input("Destination : ")
    date = input("Enter the date of journey (dd/mm/yyyy) : ").strip(".")
    if fro != to:
        print("Available flights : 1. Indigo  , 2. Air India  , 3. spicejet")
        f = int(input("Enter your flight number : "))
        if f == 1:
            print("Availabe Timings : 1. 10 AM , 2. 13 PM , 3. 18 PM ")
            t = int(input("Enter your timing slot : "))
            if t == 1:
                print("Your Flight from ", fro, "to", to, "on", date, "and time of 10AM")
                n = int(input("Enter the number of tickets : "))
                amount = 8000*n
                payment()
            elif t == 2:
                print("Your Flight from ",fro,"to",to,"on",date,"and time of 13PM")
                n = int(input("Enter the number of tickets : "))
                amount = 8000*n
                payment()
            elif t == 3:
                print("Your Flight from ",fro,"to",to,"on",date,"and time of 18PM ")
                n = int(input("Enter the number of tickets : "))
                amount=8000*n
                payment()

        if f==2:
            print("Availabe Timings : 1. 10 AM , 2. 13 PM , 3. 18 PM ")
            t = int(input("Enter your timing slot : "))
            if t == 1 :
                print("Your Flight from ",fro,"to",to,"on",date,"and time of 10AM")
                n = int(input("Enter the number of tickets : "))
                amount = 8000*n
                payment()
            elif t == 2 :
                print("Your Flight from ",fro,"to",to,"on",date,"and time of 13PM")
                n = int(input("Enter the number of tickets : "))
                amount = 8000*n
                payment()
            elif t == 3 :
                print("Your Flight from ",fro,"to",to,"on",date,"and time of 18PM")
                n = int(input("Enter the number of tickets : "))
                amount = 8000*n
                payment()

        if f==3:
            print("Availabe Timings : 1. 10 AM , 2. 13 PM , 3. 18 PM ")
            t = int(input("Enter your timing slot : "))
            if t == 1 :
                print("Your Flight from ",fro,"to",to,"on",date,"and time of 10AM")
                n = int(input("Enter the number of tickets : "))
                amount = 8000*n
                payment()
            elif t == 2 :
                print("Your Flight from ",fro,"to",to,"on",date,"and time of 13PM")
                n = int(input("Enter the number of tickets : "))
                amount = 8000*n
                payment()
            elif t == 3 :
                print("Your Flight from ",fro,"to",to,"on",date,"and time of 18PM")
                n = int(input("Enter the number of tickets : "))
                amount = 8000*n
                payment()
    else:
        print("NO SUCH JOURNEY !!!!")





def payment():
    print("Total amount : ",amount)
    print('''
                 Banks :           
                 1.SBI
                 2.IOB
                 3.Axis''')
    bank = int(input("Enter the bank : "))
    if bank == 1:
        pay = input("Enter your password : ")
        if pay == password:
            print("-----------------------------------------")
            print("Payment Proccesing ----------->>>>>>>>>>>")
            print("-----------------------------------------")
            print("Payment Successful !!!")
            print("-----------------------------------------")
            print("YOUR BOOKING HAS BEEN CONFIRMED")
        else:
            print("Invalid Password")
    if bank == 2:
        pay = input("Enter your password : ")
        if pay == password:
            print("-----------------------------------------")
            print("Payment Proccesing ----------->>>>>>>>>>>")
            print("-----------------------------------------")
            print("Payment Successful !!!")
            print("-----------------------------------------")
            print("YOUR BOOKING HAS BEEN CONFIRMED")
        else:
            print("Invalid Password")
    if bank == 3:
        pay = input("Enter your password : ")
        if pay == password:
            print("-----------------------------------------")
            print("Payment Proccesing ----------->>>>>>>>>>>")
            print("-----------------------------------------")
            print("Payment Successful !!!")
            print("-----------------------------------------")
            print("YOUR BOOKING HAS BEEN CONFIRMED")
        else:
            print("Invalid Password")





def train():
    global amount
    print('''WELCOME TO TRAIN BOOKING SECTION !!!!''')
    print("Enter your Source and Destination places : ")
    fro = input("Source : ")
    to = input("Destination : ")
    date = input("Enter the date of journey (dd/mm/yyyy) : ").strip(".")
    if fro != to:
        print("Available trains : 1. Howrah Exp   , 2. Chennai Exp  , 3. Vaigai Exp")
        f = int(input("Enter your train number : "))
        if f == 1:
            print("Availabe Timings : 1. 10 AM , 2. 13 PM , 3. 18 PM ")
            t = int(input("Enter your timing slot : "))
            if t == 1:
                print("Your trains from ", fro, "to", to, "on", date, "and time of 10AM")
                print("Types of coach :   1 .sleeper    2. AC II tier    3. AC III tier")
                co = int(input("Enter Your Choice : "))
                if co == 1:
                    n = int(input("Enter the number of tickets : "))
                    amount = 1500 * n
                    payment()
                elif co == 2:
                    n = int(input("Enter the number of tickets : "))
                    amount = 3500 * n
                    payment()
                elif co == 3:
                    n = int(input("Enter the number of tickets : "))
                    amount = 2500 * n
                    payment()
            elif t == 2:
                print("Your trains from ", fro, "to", to, "on", date, "and time of 13PM")
                print("Types of coach :   1 .sleeper    2. AC II tier    3. AC III tier")
                co = int(input("Enter Your Choice : "))
                if co == 1:
                    n = int(input("Enter the number of tickets : "))
                    amount = 1500 * n
                    payment()
                elif co == 2:
                    n = int(input("Enter the number of tickets : "))
                    amount = 3500 * n
                    payment()
                elif co == 3:
                    n = int(input("Enter the number of tickets : "))
                    amount = 2500 * n
                    payment()
            elif t == 3:
                print("Your trains from ", fro, "to", to, "on", date, "and time of 18PM ")
                print("Types of coach :   1 .sleeper    2. AC II tier    3. AC III tier")
                co = int(input("Enter Your Choice : "))
                if co == 1:
                    n = int(input("Enter the number of tickets : "))
                    amount = 1500 * n
                    payment()
                elif co == 2:
                    n = int(input("Enter the number of tickets : "))
                    amount = 3500 * n
                    payment()
                elif co == 3:
                    n = int(input("Enter the number of tickets : "))
                    amount = 2500 * n
                    payment()

        if f == 2:
            print("Availabe Timings : 1. 10 AM , 2. 13 PM , 3. 18 PM ")
            t = int(input("Enter your timing slot : "))
            if t == 1:
                print("Your trains from ", fro, "to", to, "on", date, "and time of 10AM")
                print("Types of coach :   1 .sleeper    2. AC II tier    3. AC III tier")
                co = int(input("Enter Your Choice : "))
                if  co == 1:
                    n = int(input("Enter the number of tickets : "))
                    amount = 1500 * n
                    payment()
                elif  co == 2:
                    n = int(input("Enter the number of tickets : "))
                    amount = 3500 * n
                    payment()
                elif  co == 3:
                    n = int(input("Enter the number of tickets : "))
                    amount = 2500 * n
                    payment()
            elif t == 2:
                print("Your trains from ", fro, "to", to, "on", date, "and time of 13PM")
                print("Types of coach :   1 .sleeper    2. AC II tier    3. AC III tier")
                co = int(input("Enter Your Choice : "))
                if co == 1:
                    n = int(input("Enter the number of tickets : "))
                    amount = 1500 * n
                    payment()
                elif co == 2:
                    n = int(input("Enter the number of tickets : "))
                    amount = 3500 * n
                    payment()
                elif co == 3:
                    n = int(input("Enter the number of tickets : "))
                    amount = 2500 * n
                    payment()
            elif t == 3:
                print("Your trains from ", fro, "to", to, "on", date, "and time of 18PM")
                print("Types of coach :   1 .sleeper    2. AC II tier    3. AC III tier")
                co = int(input("Enter Your Choice : "))
                if co == 1:
                    n = int(input("Enter the number of tickets : "))
                    amount = 1500 * n
                    payment()
                elif co == 2:
                    n = int(input("Enter the number of tickets : "))
                    amount = 3500 * n
                    payment()
                elif co == 3:
                    n = int(input("Enter the number of tickets : "))
                    amount = 2500 * n
                    payment()

        if f == 3:
            print("Availabe Timings : 1. 10 AM , 2. 13 PM , 3. 18 PM ")
            t = int(input("Enter your timing slot : "))
            if t == 1:
                print("Your trains from ", fro, "to", to, "on", date, "and time of 10AM")
                print("Types of coach :   1 .sleeper    2. AC II tier    3. AC III tier")
                co = int(input("Enter Your Choice : "))
                if co == 1:
                    n = int(input("Enter the number of tickets : "))
                    amount = 1500 * n
                    payment()
                elif co == 2:
                    n = int(input("Enter the number of tickets : "))
                    amount = 3500 * n
                    payment()
                elif co == 3:
                    n = int(input("Enter the number of tickets : "))
                    amount = 2500 * n
                    payment()
            elif t == 2:
                print("Your trains from ", fro, "to", to, "on", date, "and time of 13PM")
                print("Types of coach :   1 .sleeper    2. AC II tier    3. AC III tier")
                co = int(input("Enter Your Choice : "))
                if co == 1:
                    n = int(input("Enter the number of tickets : "))
                    amount = 1500 * n
                    payment()
                elif co == 2:
                    n = int(input("Enter the number of tickets : "))
                    amount = 3500 * n
                    payment()
                elif co == 3:
                    n = int(input("Enter the number of tickets : "))
                    amount = 2500 * n
                    payment()
            elif t == 3:
                print("Your trains from ", fro, "to", to, "on", date, "and time of 18PM")
                print("Types of coach :   1 .sleeper    2. AC II tier    3. AC III tier")
                co = int(input("Enter Your Choice : "))
                if co == 1:
                    n = int(input("Enter the number of tickets : "))
                    amount = 1500 * n
                    payment()
                elif co == 2:
                    n = int(input("Enter the number of tickets : "))
                    amount = 3500 * n
                    payment()
                elif co == 3:
                    n = int(input("Enter the number of tickets : "))
                    amount = 2500 * n
                    payment()
    else:
        print("***************NO SUCH JOURNEY****************")



def hotel():
    global amount
    print("WELCOME TO HOTEL BOOKING SECTION !!!")
    state = input("Enter the State : ")
    city=input("Enter the city : ")
    dat = input("Enter the date (dd/mm/yyyy) : ").strip(".")
    print(''' 
    1. Taj 
    2. The Park
    3. Colombia''')
    h = int(input("Enter your Choice : "))
    if h == 1:
        n = int(input("Enter the total number of rooms : "))
        amount=6000*n
        payment()
    elif h == 2:
        n = int(input("Enter the total number of rooms : "))
        amount=6000*n
        payment()
    elif h == 3:
        n = int(input("Enter the total number of rooms : "))
        amount=6000*n
        payment()


password = '123'
global n
print("WELCOME TO MAKE MY TRIP !!!!!")
print("-----------------------------------------")
print("We Make Your Trips Enjoyable !!!!")
print("-----------------------------------------")
print(''' We Provide :
          1. Hotel Room Booking (Type Hotel)
          2. Flight Ticket Booking (Type flight)
          3. Train Ticket Booking (type train)
                                                ''')
print("-----------------------------------------")
a = input("Enter your preference : ")
if a == 'hotel':
    hotel()
elif a == 'flight':
    flight()
elif a == 'train':
    train()
else:
    print("*****No Such Services are Provided*****")