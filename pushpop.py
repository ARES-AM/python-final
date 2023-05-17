# let arry of 5
stackarray=[]
global tos
tos=int(-1)
def push(x):
    global tos
    if tos==4:
        raise IndexError("stack overflow")

    tos+=1
    stackarray.insert(tos,x)
    print(stackarray)
    return stackarray
def pop():
    if tos==-1:
        raise IndexError("stack underflow")
    value=stackarray[tos]
    stackarray.pop(tos)
    # print(tos)
    return value
        
            

def choicepoporpush(choice):
    if choice==1:
        inputvalue=int(input("Enter the value you want to stack"))
        print(f"{choicepoporpush(inputvalue)} is stacked")
        
        # choicepoporpush(inputvalue)
        

    elif choice==0:
        print(f"{pop()} is poped")
        z=int(input("enter 1 to stack 0 to pop and 2 to quit"))
        choicepoporpush(z)
    elif choice==2:
        print(f"final stack is {stackarray}\nquitting")
    else:
        y=int(input("please enter 0 , 1 or 2  only"))
        choicepoporpush(y)
        
    
choice=int(input("enter 1 to push and 0 to pop"))

choicepoporpush(choice)
print(stackarray)


    