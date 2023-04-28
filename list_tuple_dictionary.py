#list values can be changed
myfruitlist = ["Apple" , "Banana" , " Cherry" ,"strawberry"]
print(myfruitlist)
print(type(myfruitlist))
print(myfruitlist[0])
print(myfruitlist[1])

myfruitlist[2] = "orange"
print(myfruitlist)

#the tuple is like a list, but it can't be changed.
# A data type that can't be changed after it's created is said to be immutable. 
# To define a tuple, you use parentheses()
mytuple = ( "apple " , "grapes" , "berries")
print(mytuple)
print(type(mytuple))

print(mytuple[2])

#dictinory 
#A dictionary is a list with named positions (keys)
myDictionary = {
    "sandu" : "mango",
    "pavan" : "orange",
    "tanusri" : "grapes"
}

print(type(myDictionary))
print(myDictionary["tanusri"])