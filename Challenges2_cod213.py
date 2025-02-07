##### First exercice #######

fruit = ["banana" , "apple ", "orange ", "grapes", "prach", "plum" ]

fruit.append("watermelon")
fruit.pop(2)

sorted_fruit = sorted (fruit)

print (sorted_fruit)

##### Second exercice ######

client = {"name" : "imad", "age": 30 , "city": "Sidi_aissa"}

client ["id"] = 100

client.update({"name": "omda"})

print (client)

##### Third exercice ######

set1 = {1,2,3,4,5,6,7,8,9}

set2 = {8,44,20,4,3}

intersect_set = set1.intersection(set2)

union_set = set1.union(set2)

print (intersect_set)

print (union_set)

##### Forth exercice ######


def find_number ( list , number):

    for i in range (0,len(list)):
        if list[i] == number :
            print (f"the Number '{number}' with index '{i}' has been found")
            break
    else : 
        print ("the Number couldn't be found")
        
        
list1 = [22 , 45 , 36.6 , 4 ,99 ,125 , 4125 , 78]

find_number(list1 , 36.6)
