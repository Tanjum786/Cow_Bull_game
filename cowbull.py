import random
def game(list1):
    name=input("enter your name ")
    guess=10
    i=0
    list3=[]
    list4=[]
    while i<=guess:
        number=int(input("enter any number"))
        position=int(input("enter position of number"))
        if number in list2 and list2.index(number)==position:
            list3.insert(position,number)
            print("**bull**",list3)
        if number in list2 and list2.index(number)!=position:
            list4.append(number)
            print("These are correct numbers you can reuse it",list4)    
            print("**cow**")
        i+=1
    if list2==list3:
        print(name,"congratulation you are won!!")
    else:
        print(name,"opps you lost")
list1=[0,1,2,3,4,5,6,7,8,9]        
list2=random.sample(list1,5) 
print(list2)       
game(list1) 