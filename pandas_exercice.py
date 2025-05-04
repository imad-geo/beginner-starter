import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###_____reading the data____#####

student = pd.read_csv("C:/Users/i-korichi/Desktop/students.csv")



###_____Analyse the data____#####
# average_score = student["score"].mean() #to get the average 

# hight_score = student["score"].max()# to get the highest score

# youngest = student["age"].min()# to get the youngest age

# total_student = len(student)# to get the number of rows

# print(total_student )

###_____Manipulation the data____##### 

# add new row

# new_student = {"name":"lghith",
                # "age":70,
                # "score":93}

# student = pd.concat([student,pd.DataFrame([new_student])], ignore_index=True)

# student.to_csv("C:/Users/i-korichi/Desktop/students.csv", index=True)

# sort the data based on scores

# sorted_student = student.sort_values("score" , ascending= False)

# sorted_student = student[student["score"] > 80]

# print (sorted_student)

# add Visualisation chart

# bar_student = student["score"].value_counts().plot.barh()# i did this in google collab

# histo = student['age'].plot.hist()#i did this in google collab

# print(histo)


