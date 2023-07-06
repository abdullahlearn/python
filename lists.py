introduction='''Welcome to the "List Generator"
               In this app, we'll generate a list ,
                 and you have to see it carefully 
                 then we'll generate that list again.
                 and you have to tell what is missing 
                 or what is added.
                would you like to play this game???
                 (y/n) :'''
print(introduction)
answer=input()
if answer == "y" or answer == "yes":
    print("ok let's do this .")
    import random
    wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter',
    'snake dandruff']
    names=['tex' , 'rex' , 'jen' , 'ace' , 'trtter' , 'gizmo']
    vehicles=['cuv' , 'suv' , 'sedan' , 'van']
    cars=['micro' , 'pickup' , 'supercar' , 'roadster' , 'hatchback' , 'coupe']
    list=(wizard_list,names,vehicles,cars)
    print(random.sample(list , 1))
    print('''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ''' )
    add1=wizard_list.append("wormburgers")
    sub1=vehicles.remove("sedan")
    add2=names.append("cookie")
    sub2=cars.remove("coupe")
    lists=(add1 , sub1 , add2 , sub2)
    list2=(wizard_list,names,vehicles,cars)
    print(random.sample(list2 , 1))
    print('''what is the difference between 
    the first and the second list:
    write your  answer with the help of 
    options given below:
    1-some thing added
    2-some thing deleted
    3-both lists are different
    4-no difference''')
    answer2=input()
    if answer2 == "4":
        print("your answer is incorrect")
    if answer2 == "3":
        print("your answer maybe correct")
    if answer2 == "2":
         print("your answer maybe correct")
    if answer2 == "1":
         print("your answer maybe correct")
    print("see you next time.")
else:
    print("ok , no problem")
    

