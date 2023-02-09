
#! functions
def user_login():
    tries = 0
    while tries < 3:
        username = input("Account name: ")
        passcode = input("Account pin: ")

        if(username == default_user["user"] and passcode == default_user["pin"]):
            print("welcome back",username)
            check_balance()
            break
            
        else:
            print("unsuccessful login")
            tries = tries + 1
            print("you have",3-tries,"tries left")

def check_balance():
    print(default_user["bal"])
    print("Your balance is KES", default_user["bal"]["KES"])
    print(default_user["bal"]["USD"])
    print(default_user["bal"]["GCD"])

def deposit():
    pass

def addition(first_digit,second_digit):
    # return first_digit + second_digit
    print(first_digit + second_digit)

############################################################

default_user = {
    "user":"test",
    "pin":"0000",
    "bal":{
        "KES":120,
        "USD":1,
        "GCD":12
    },
    "branch":[
        {"country1":"kenya",
        "country2":"ghana",
        "country3":"nigeria",},
        {"class1":"silver",
        "class2":"gold",
        "class3":"platinum",}
        ]
}

print(default_user["user"])
print(default_user["pin"])
print(default_user["branch"])
print(default_user["branch"][0]["country2"])


# user_login()

example = [
    {
    "veggies":["veg1","veg2"],
    },
    {
        "fruits":["frui1","frui2"],
    }
    ]
# check_balance()
# print(addition(50,100))
# addition(45,67)


# print(username)

# if(username == default_user["user"]):
#     print("welcome back ",username)
# elif(passcode == default_user["pin"]):
#     print("successful ",passcode)

        # exit()
        # break

# print(default_user["bal"])
# print("Your balance is KES", default_user["bal"]["KES"])
# print(default_user["bal"]["USD"])
# print(default_user["bal"]["GCD"])



# #! start validation
# # if(username == default_user["user"] and passcode == default_user["pin"]):
# #     print("welcome home: accountx")
# # else:
# #     print("unsuccessful login")
# #     exit()
