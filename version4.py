import random
import time
import csv

# file = open("opening.txt",'r')
# for each in file:
#     time.sleep(0.3)
#     print(each, end='')

print("Hahahahah, Hello again!")
username=input("Please enter an username: ")
mode=int(input(f"{username}, Which mode would you like to play in? "))


vocabulary={}
with open("de-en_adjective.csv", encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        key=row[0]
        value=row[1]
        vocabulary[key]=value

question="Choose the correct answer for: "
score=0
tcount=0

with open("mistakes.txt",'w', encoding='UTF-8') as file:
    if mode==1: 
        n=int(input("Choose the number of questions: "))
        start=time.time()
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
            else:
                mistake= answer_true + '\n'
                file.write(mistake)

        end=time.time()
        elepsed_time=end-start
        score=(tcount*100)/n
        minutes, seconds = divmod(elepsed_time, 60)
        print(f'project finished in {minutes} minutes and {seconds} seconds')
        print(f"You've made {tcount} corrects!")
        print(f"Your score is {score}%")

    elif mode==2:
        import time
        start=time.time()
        qcount=0
        while time.time() - start < 60 :
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
            qcount=qcount+1

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
            else:
                mistake= answer_true + '\n'
                file.write(mistake)

        score=(tcount*100)/(qcount)
        print(f"You've answered {qcount} questions!")
        print(f"You've made {tcount} corrects! <3")
        print(f"Your score is {score}%")
    