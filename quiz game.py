print("Welcome to my computer quiz!!")

playing = input("Do You want to play!! ")
#print(playing)
if playing != "yes":
    quit()

print("Let's play together")   
score = 0
answer = input("What does GPU stand for? ")
#print("Write your answer here: ")
if answer.lower() == "graphics processing unit":
    print('Correct!!')
    score +=1
else:
    print('Wrong Information')


answer = input("What does RAM stand for? ")
#print("Write your answer here: ")
if answer.lower() == "random access memory":
    print('Correct!!')
    score +=1
else:
    print('Wrong Information')


answer = input("What does CPU stand for? ")
#print("Write your answer here: ")
if answer.lower() == "central processing unit":
    print('Correct!!')
    score +=1
else:
    print('Wrong Information')


answer = input("What does PSU stand for? ")
#print("Write your answer here: ")
if answer.lower() == "power supply unit":
    print('Correct!!')
    score +=1
else:
    print('Wrong Information')


answer = input("What does ML stand for? ")
#print("Write your answer here: ")
if answer.lower() == "machine learning":
    print('Correct!!')
    score +=1
else:
    print('Wrong Information')



print("Your total correct answer is ",score )
print("Your accuracy score is", ((score/5)*100),"%")