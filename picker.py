from os import system
import random
questions = [
    'What would you do if you do not get a job immediately after graduating',
    'What is your biggest achievement?',
    'What is your biggest fear till now?',
    'What so far has been your toughest time, How did u overcome that?',
    'Who is your role model?',
    'what was the badest day of your life'
]
try:
    system('cls || clear')
    f_que=''
    key=input("> Press Enter Key To Pick Question: ")
    flag=0
    while True:
        if key=='' and flag==0:
            flag=1
        elif key=='x':
            break
        elif key=='add':
            print('n')
            system('cls || clear')
            newq = input("> Enter new question that you want to add in the list(will get erased after new execution): ")
            questions.append(newq) if newq!='' else None
            system('cls || clear')
            print('[+] New entry for question has been added!') if newq!='' else print("You skipped action!")
            key=input("> Press Enter Key To Pick Question: ")
        elif key=='del':
            system('cls || clear')
            print('+ Select number of question you want to delete!')
            for i in range(len(questions)):
                print(f"{i+1}] {questions[i]}")
            index=input('> Enter Option: ')
            try:
                index=int(index)
                questions.pop(int(index)-1)
                system('cls || clear')
                key=input("[+] Successfully removed question from the list\n> Press Enter Key To Pick Question: ")
            except:
                system("cls || clear")
                print("Something went wrong while removing question from list\nTry to do it carefully again!")  if index!='' else print("You skipped action!")
                key=input("> Press Enter Key To Pick Question: ")
        else:
            key=input("> Press Enter Key To Pick Another Question: ")
        while(key!='' and key!='x' and key!='add' and key!='del'):
            system('cls || clear')
            key=input("> Please only press Enter Key to Pick New Question!: ")
            continue
        system('cls || clear')
        que = random.choice(questions)
        while f_que==que:
            que = random.choice(questions)
        f_que = que
        print(que,end='\n\n')
    system('cls || clear')
    print('[+] Thank-You For using this script!\nHave a great day\n:-)')
except KeyboardInterrupt:
    system('cls || clear')
    print('[+] Thank-You For using this script!\nHave a great day\n:-)')