userReply = input("Do you need to ship a package? (enter yes or no)")
if userReply == "yes" :
    print("we can help you ship that package")
else:
    print("please come back when you need to ship a package .thank you.")
    
    
userReply2 = input("Would you like to buy stamps,buy a envelope,or make a copy? (enter stamp,envelope or copy)")    
if userReply2 == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply2 == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply2 == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    
    
    
    
    

