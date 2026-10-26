import pathlib as Path
import string
import random
import json

class ATM:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open('database','r') as fs:
                data = json.loads(fs.read())
        else:
            print("file doesnt exist.")
    except Exception as err:
        print(f"Exception occured: {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(ATM.data))  #data is dump into json file that is database

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k= 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def createAccount(self):
        info = {
            "name":input("enter your name:"),
            "age":int(input("enter your age:")),
            "pin":input("create your 4 digit pin:"),
            "accountNum": ATM.__accountgenerate(),
            "phoneNum":int(input("enter your phone number:")),
            "balance":0
        }
        if info["age"]<18 or len(str(info["pin"]))!=4:
            print("sorry your account cannot be created!")
        else:
            print("your account details are:\n")
            for i in info:
                print(f"{i}: {info[i]}")

            ATM.data.append(info)
            ATM.__update()
            print("account created successfully.")


    def updateDetails(self):
        accNum = input("enter your account number:")
        pin = int(input("enter your pin: "))

        userdata = [i for i in ATM.data if i["accountNum"==accNum and i["pin"]==pin]]

        if userdata==False:
            print("no details found!")
        else:
            print("age, account number and balance cannot be updated\n update the details below:")
            newdata={
                 "name": input("please tell new name or press enter : "),
                "phoneNum":input("please tell your new phone number or press enter to skip :"),
                "pin": input("enter new Pin or press enter to skip: ")
             }
            if newdata["name"]=="":
                newdata["name"]=userdata[0]["name"]
            if newdata["phoneNum"] == "":
                newdata["phoneNum"] = userdata[0]['phoneNum']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']

            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']
            
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]

            ATM.__update()
            print("details updated successfully")


    def withDrawMoney(self):
        accNum = input("enter your account number:")
        pin = int(input("enter your pin: "))
        
        userdata = [i for i in ATM.data if i["accountNum"]==accNum and i["pin"]==pin]
        
        if userdata==False:
            print("no details found!")
        else:
            amount = int(input("enter amount to withdraw:"))
            if amount<userdata[0]["balance"]:
                userdata[0]["balance"] -= amount
            else:
                print("you do not have sufficient balnce!")
            for i in userdata:
                print(f"your current balance is {userdata[0]["balance"]}")

            ATM.__update()

    def depositMoney(self):
        accnum = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in ATM.data if i['accountNum'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("soory no data found")
        
        else:
            amount = int(input("how much you want to depoit "))
            if amount  > 10000 or amount < 0:
                print("sorry the amount is too much you can deposit below 10000 and above 0")

            else:
                userdata[0]['balance'] += amount
                ATM.__update()
                print("Amount deposited successfully ")
        


user = ATM()
choice = int(input("Enter your choice: \n"))

if choice==1:
    user.updateDetails()
elif choice==2:
    user.withDrawMoney()
elif choice==3:
    user.depositMoney()
elif choice==4:
    user.createAccount()
else:
    print("....enter a valid choice....")
