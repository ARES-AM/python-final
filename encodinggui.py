import random as r
import string as s
def revefxn(msg):
    return msg[::-1]
class encoding:
    cyp=input("Enter your message")
    # step 1 swap lower to upper and vice versa 
    cyp1=cyp.swapcase()
    # change msg to list and reverse
    cyplist1=cyp1.split(' ')
    cyplist1.reverse()
    cpylist2=[]
    for i, element in enumerate(cyplist1):
    # add 7 letters word in index 1,3,5....
        randomword=''.join(r.choice(s.ascii_uppercase + s.ascii_lowercase) for i in range(7))  
        cpylist2.append(revefxn(element))
        cpylist2.append(randomword)
   
    cpylist2.reverse()              
    cyp2=' '.join(cpylist2)   
    print(cyp2)   

    
    
a=encoding()


