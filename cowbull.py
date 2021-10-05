import random
def game(list1):
    print(list2)
    name=input("enter your name ")
    print(name,"welcome to cow bull game")
    guess=10
    i=0
    list3=[]
    list4=[]
    while i<guess:
        number=int(input("enter any number"))
        position=int(input("enter position of number"))
        if number in list2 and list2.index(number)==position:
            list3.insert(position,number)
            print("**bull**",list3)
        if number in list2 and list2.index(number)!=position:
            list4.append(number)
            print("These are correct numbers you can reuse it",list4)    
            print("**cow**") 
        if list2==list3:
            break      
        i+=1
    if list2==list3:
        print(name,"congratulation you are won!!")
    else:
        print(name,"opps you lost")
    user=input("would you want to continue game if yes type y or no then type n")
    while True:
        if user=="y":
            game(list1)
        else:
            print("quit")
            break
list1=[0,1,2,3,4,5,6,7,8,9]        
list2=random.sample(list1,5)        
game(list1)
# while True:
#     user=input("would you want to continue game if yes type y or no then type n")
#     if user=="y":
#         game(list1)
#     else:
#         print("quit")    
#         break