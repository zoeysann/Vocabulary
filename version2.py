import random
import time

print("Hallo!")
time.sleep(0.5)

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
question="Choose the correct answer for"

for i in range(n):
    random.shuffle(list(vocabulary.keys()))
    ran_word=random.choice(list(vocabulary.keys()))
    answer_true=vocabulary[ran_word]
    answers=list(vocabulary.values())
    answers.remove(answer_true)
    random.shuffle(answers)
    
    variants={"a)": 1,
              "b)": 2,
              "c)": answer_true
              }
    
    for key in list(variants.keys())[:-1]:
        variants[key]=random.choice(answers)

    random.shuffle(list(variants.items()))
    
    print(question, ran_word, sep=": ")
    for key, value in variants.items():
        random.shuffle(list(variants.values()))
        print(f'{key}: {value}')
    
    your_answer=input("Your answer: ")
    #if your_answer==
    