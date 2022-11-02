# Ayah Saleh
def encode(passString):  # encode method to shift each digit in passcode up by 3 numbers
    newStr = ""  # new variable to store new password
    val = None
    for i in range(len(passString)):  # for loop to go through each individual elem in str to shift to int + 3
        val = int(passString[i]) + 3  # adds 3 to each num in the str
        if val > 9:  # if val goes above 9 the num should reset
            if val == 10:
                val = 0
            elif val == 11:
                val = 1
            elif val == 12:
                val = 2
        newStr += str(val)  # casts int back to str in order to concatenate to new str variable
    return newStr


def decode(passString):  # decode method to shift each encoded passcode back to original passcode
    newStr = ""  # new var to store new pass word
    val = None
    for i in range(len(passString)): # for loop to go through each individual elem in str to shift back to original
        val = int(passString[i]) - 3  # subtracts 3 from each num in the str
        if val < 0: # if val goes below 0 the num should reset
            if val == -3:
                val = 7
            elif val == -2:
                val = 8
            elif val == -1:
                val = 9
        newStr += str(val) # casts int back to str in order to concatenate to new str variable
    return newStr


loop = True  # boolean that perpetuates the while
encoded = ""  # defines encoded var that will store str
password =""  # defines password var that will store str
while loop:
    print("Menu")  # prints menu headliner
    print("-"*13)
    print("1. Encode\n2. Decode\n3. Quit\n")  # prints menu options
    opt = int(input("Please enter an option: "))  # input statement for user option
    if opt == 1:  # option to allow user to enter pass and then stores the new encoded pass in a var
        password = input("Please enter your password to encode: ")
        encoded = encode(password)
        print("Your password has been encoded and stored!\n")
    elif opt == 2: # option to decode a users encoded password back to the initial password
        decoded = decode(encoded)
        print(f"The encoded password is {encoded} and the original password is {decoded}.\n")
    elif opt == 3:  # terminates loop and hence the program
        loop = False
        break
