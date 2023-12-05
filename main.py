import random
import time

print("Hallo!")
time.sleep(0.5)
print("Let's start!")

vocabulary={
    "sehr": "very",
    "gut": "good",
    "natürlich": "of course",
    "koche": "cook",
    "schach": "chess",
    "manchmal": "sometimes",
    "klein": "small",
    "gross": "big",
    "klug": "smart",
    "nett": "nice",
    "bitte": "please",
    "tschüss": "bye"
    }

n=int(input("Choose the number of questions: "))
tcount=0

for i in range(n):
    ran_word=random.choice(list(vocabulary.keys()))
    true_answer=vocabulary[ran_word]
    
    time.sleep(1)
    question="Translate it"
    print(question, ran_word, sep=": ")
    your_answer=input("Your answer: ")
    print("True answer: ",true_answer)
    
    
    if your_answer==true_answer:
        tcount=tcount+1

print("The number of true asnwers is: ", tcount)