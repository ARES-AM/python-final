import string as str
import random as r
import os


def randomPasswordGenerator(letter_count, digit_count, uppercase, sign_cnt):

    # random password generator
    #  use this for loop not to get error at first
    str1 = ''.join((r.choice(str.ascii_letters) for x in range(letter_count)))
    for i in range(digit_count):
        str1 += ''.join(r.choice(str.digits))

    for i in range(sign_cnt):
        str1 += ''.join(r.choice(str.punctuation))

    for i in range(uppercase):
        str1 += ''.join(r.choice(str.ascii_uppercase))

    str6 = list(str1)
    r.shuffle(str6)
    finalString = ''.join(str6)
    return finalString


def findWord(usrnm):
    with open("/home/ares_am/Documents/newtrypy/Password.txt", "r+") as file:
        es = []
        lines = file.readlines()
        for j in range(len(lines)):
            es = lines[j]

            linewiselist = es.split(" ")

            for i in range(len(linewiselist)):
                if linewiselist[i] == usrnm:
                    x = True
                    return True, j
                    if x == True:
                        break


def pwd(pwdd, usrnm):

    y = findWord(usrnm)

    if y != None:
        lineNO = findWord(usrnm)[1]
        with open("/home/ares_am/Documents/newtrypy/Password.txt", 'r+') as fp:
            es = []
            lines = fp.readlines()
            offset = 0
            for j in range(lineNO):
                es = lines[j]
                offset += len(es)

            fp.seek(offset+len(usrnm)+1)
            fp.write(pwdd)
    else:
        with open("/home/ares_am/Documents/newtrypy/Password.txt", "a") as ff:
            ff.write("\n"+usrnm + " "+pwdd)
# forloop
def usrchoice1(dorpwd,usnam):
    print(f"Generated password for{usnam}is :{dorpwd}")
    
    choice=input('''Enter
    Y to update or save password
    N to not change password
    T to regenerate password
    ''')
    c11=choice.upper()
    if c11=="Y":
        pwd(dorpwd, usr)
        print("Password has been updated")
    elif c11=="N":
        print("Terminated succssfully")
    
    elif c11=="T":
        pdd = randomPasswordGenerator(2, 4, 1, 4)
        os.system("clear")
        usrchoice1(pdd,usnam)
    else:
        os.system("clear")
        print("Enter y , n or t only")
        usrchoice(dorpwd,usnam)



def usrchoice(dorpwd,usnam):
    print(f"Generated password for{usnam}is :{dorpwd}")
    
    choice=input('''Enter
    Y to update or save password
    N to not change password
    T to regenerate password
    ''')
    c11=choice.upper()
    if c11=="Y":
        pwd(pwdddd, usr)
        print("Password has been updated")
    elif c11=="N":
        print("Terminated succssfully")
    
    elif c11=="T":
        pdd = randomPasswordGenerator(2, 4, 1, 4)
        os.system("clear")
        usrchoice1(pdd,usnam)
    else:
        os.system("clear")
        print("Enter y , n or t only")
        usrchoice(dorpwd,usnam)







usr = input("Enter the username: ")
pwdddd = randomPasswordGenerator(2, 4, 1, 4)
x = os.path.isfile('/home/ares_am/Documents/newtrypy/Password.txt')
if x == True:
    usrchoice(pwdddd,usr)
    

else:
    fp = open('/home/ares_am/Documents/newtrypy/Password.txt', 'x')
    usrchoice(pwdddd,usr)
    fp.close()
