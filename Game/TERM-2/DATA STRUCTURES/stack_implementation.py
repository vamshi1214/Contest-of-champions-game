def empty(stack):
    if stack==[]:
        return True
    else:
        return False
def push(stack,item):
    stack.append(item)
    top=len(stack)-1
def pop(stack):
    if empty(stack)==True:
        print('underflow')
    else:
        item=stack.pop()
        if len(stack)==0:
            top=None
        else:
            top=len(stack)-1
        return item
def peek(stack):
    if empty(stack):
        return "underflow"
    else:
        top=len(stack)-1
        return stack[top]
def display(stack):
    if empty(stack):
        print("stack is empty")
    else:
        top=len(stack)-1
        print(stack[top],"is top")
        for i in range (top-1,-1,-1):
            print(stack[i])
#main
stack=[]
top=None

while True:
    print("STACK OPERATIONS")
    print("1.PUSH")
    print("2.POP")
    print("3.PEEK")
    print("4.DISPLAY")
    print("5.EXIT")
    ch=int(input("enter no."))
    if ch==1:
        item=int(input('enter item'))
        push(stack,item)
    elif ch==2:
        item=pop(stack)
        if item=="underflow":
            print('underflow!stack is empty')
        else:
            print('pop is',item)
    elif ch==3:
        item=peek(stack)
        if item=='underflow':
            print('underflow stack is empty')
        else:
            print("top item is",item)
    elif ch==4:
        display(stack)
    elif ch==5:
        break
    else:
        print('invalidchoice')