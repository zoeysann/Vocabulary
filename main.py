import random
import time
import csv

print("Hallo!")
time.sleep(0.5)
print("Let's start!")



with open("C:\\Users\\Monster\\Desktop\\Vocabulary\\de-en_adjective.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
            print(f'\t{row[0]} word is {row[1]} in German, and was {row[3]} as a {row[2]} level.')
            line_count += 1
            
    print(f'Processed {line_count} lines.')


# n=int(input("Choose the number of questions: "))
# tcount=0

# for i in range(n):
#     ran_word=random.choice(list(vocabulary.keys()))
#     true_answer=vocabulary[ran_word]
    
#     time.sleep(1)
#     question="Translate it"
#     print(question, ran_word, sep=": ")
#     your_answer=input("Your answer: ")
#     print("True answer: ",true_answer)
    
    
#     if your_answer==true_answer:
#         tcount=tcount+1

# print("The number of true asnwers is: ", tcount)