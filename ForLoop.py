# In Python, I am making two variables: 
# class_room = [1,2]
# studentRoll = [1,2,3,4,5]

# Which means, there are 2 classrooms each having 5 students. 

# When the for loop gets Student No. 3 for each class, I want to print each to show:
# Class 1's Student No. 3 
# Class 2's Student No. 3 

class_room = [1,2]
studentRoll = [1,2,3,4,5]

for i in range(len(class_room)):
    for j in range(len(studentRoll)):
        if j == 2: 
            # print(class_room[i])
            # print(studentRoll[j])
            print("Class "+str(class_room[i])+"'s Student No." + str(studentRoll[j]))
            