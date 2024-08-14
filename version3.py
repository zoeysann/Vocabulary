import random
import time
import csv

# file = open("opening.txt",'r')
# for each in file:
#     time.sleep(0.5)
#     print(each, end='')

vocabulary={}

with open("C:\\Users\\Monster\\Desktop\\Vocabulary\\de-en_adjective.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        key=row[0]
        value=row[1]
        vocabulary[key]=value


n=int(input("Choose the number of questions: "))
tcount=0
question="Choose the correct answer for: "


for i in range(n):
    random.shuffle(list(vocabulary.keys()))
    ran_word=random.choice(list(vocabulary.keys()))
    answer_true=vocabulary[ran_word]
    answers=list(vocabulary.values())
    answers.remove(answer_true)
    
    variants={"a": 1,
              "b": 2,
              "c": answer_true
              }
    
    print(question, ran_word)

    v_list=[answer_true]
    for key in list(variants.keys())[:-1]:
        random.shuffle(answers)
        variants[key]=random.choice(answers)
        v_list.append(variants[key])
    
    random.shuffle(v_list)
    for key in variants.keys():
        variants[key]=v_list.pop()
    
    for key, value in variants.items():
        print(f'{key}: {value}')
    
    your_answer=input("Your answer: ")
    your_answer_l=variants[your_answer]

    if your_answer_l==answer_true:
        tcount=tcount+1
    
print("The number of true asnwers is: ", tcount)