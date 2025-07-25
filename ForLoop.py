# In Python, I am making two variables: 
# class_room = [1,2]
# studentRoll = [1,2,3,4,5]

# Which means, there are 2 classrooms each having 5 students. 

# For each class's 3rd student, I want to show its index no/position (in the list).

class_room = [1,2]
studentRoll = [1,2,3,4,5]

for i in range(len(class_room)):
    for j in range(len(studentRoll)):
        if j == 2: 
            print(class_room[i])
            print(studentRoll[j])

            