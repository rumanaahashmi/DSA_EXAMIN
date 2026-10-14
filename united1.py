#1 QUESTION
a = [2, 4, 6]
b = a

b = b + [8]
a.append(10)

print(a)
print(b)

# answer - B 
# [2, 4, 6, 10]
# [2, 4, 6, 8]

#2 QUESTION 
from ast import Import
import code

import numpy as np

scores = np.array([10, 20, 30, 40, 50])

result = scores[
    (scores >= 20) & (scores < 50)
] 
#ANSWER -  Option B (30.0)

#Q3: C
#Q4: A
#Q5: D
#Q6: B
#Q7: A
#Q8: C
#Q9: B
#Q10: B 

# QUESTION 
students = {
    "Sara": [75, 85, 80],
    "Ali": [60, 70, 65],
    "John": [90, 95, 85]
}
def calculate_average(marks):
    return sum(marks) / len(marks)
for name, marks in students.items():
    average = calculate_average(marks)
    print(name, average)
for name, marks in students.items():
    average = calculate_average(marks)
    if average >= 80:
        print(name, average)
print(students.items())
print(calculate_average([])) 


#QUESTION  13 


import numpy as np

scores = np.array([35, 50, 65, 80, 95])

mean_score = scores.mean()

selected = scores[scores >= mean_score]

print(mean_score)
print(selected)
print(selected.size)


#
import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "HR", "IT"],
    "Salary": [50000, 40000, None, 45000, 40000]
})



