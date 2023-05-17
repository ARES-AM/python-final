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
    # print(stackarray)
    # return stackarray
def pop():
    global tos
    if tos==-1:
        raise IndexError("stack underflow")
    value=stackarray[tos]
    stackarray.pop(tos)
    tos-=1
    # print(tos)
    return value
def peek():
    global tos
    if tos==-1:
        raise IndexError("stack underflow")
    value=stackarray[tos]
    
    # tos-=1
    # print(tos)
    return value


        
            

def choicepoporpush(choice):
    if choice==1:
        inputvalue=int(input("Enter the value you want to stack"))
        pushval=push(inputvalue)
        print(f"{inputvalue} is stacked")
        z=int(input("enter 1 to stack 0 to pop ,2 to quit,3 to peek,4 to check if stack is full,5 to check if stack is empty"))
        choicepoporpush(z)
        # choicepoporpush(inputvalue)
        

    elif choice==0:
        popedvalue=pop()
        print(f"{popedvalue} is poped")
        z=int(input("enter 1 to stack 0 to pop ,2 to quit,3 to peek,4 to check if stack is full,5 to check if stack is empty"))
        choicepoporpush(z)
    elif choice==2:
        print(f"final stack is {stackarray}\nquitting")
    elif choice==3:
        peekvalue=peek()
        print(f"{peekvalue} is in the top of stack")
        z=int(input("enter 1 to stack 0 to pop ,2 to quit,3 to peek,4 to check if stack is full,5 to check if stack is empty"))
        choicepoporpush(z)
    elif choice==4:
        print("stack is full") if tos==4 else print("stack is not full")
        z=int(input("enter 1 to stack 0 to pop ,2 to quit,3 to peek,4 to check if stack is full,5 to check if stack is empty"))
        choicepoporpush(z)
    elif choice==5:
        print("stack is empty") if tos==-1 else print("stack is not empty")
        z=int(input("enter 1 to stack 0 to pop ,2 to quit,3 to peek,4 to check if stack is full,5 to check if stack is empty"))
        choicepoporpush(z)
    else:
        y=int(input("please enter 0 , 1 or 2  only"))
        choicepoporpush(y)
        
    
choice=int(input("enter 1 to push and 0 to pop"))

choicepoporpush(choice)


    