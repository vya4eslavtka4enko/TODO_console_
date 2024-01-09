import sys
import random

def show_task(tasks_file):
    with open(tasks_file,'r') as file:
        tasks = file.read()
        print('[YOUR TASKS]')
        print(tasks)


def add_task(tasks_file):
    with open(tasks_file,'a+') as file:
        name_task = input('What is the task? ')
        deadline = input('What is the deadline? ')
        hash_num = f'{random.choice(range(1,100))}{random.choice(['!','#','^','%','&','@'])}'
        file.write(f'\n{hash_num}|{deadline}|{name_task}')
        file.close()

def complete_task(tasks_file):
    task_complete = input('Enter name of task ')
    with open(tasks_file,'w') as file:
        lines = file.readlines(1)
        for line in lines:
            words_list = line.split('|')
            for item in words_list:
                if item == task_complete:
                    line.write('')
                    print('Delete!')
        
            
def main():
    choose = [4]
    print('== TODO LIST ==')
    choice = ''
    while choice not in choose:
        print('[1] SHOW TASKS')
        print('[2] ADD TASKS')
        print('[3] COMPLETE TASK')
        print('[4] EXIT')
        try:
            choice =int(input('Your choice: '))
        except:
            print('Enter correct data ')
            
        if choice == 1:
            show_task('tasks.txt')
        elif choice == 2:
            add_task('tasks.txt')
        elif choice == 3:
            complete_task('tasks.txt')
        elif choice == 4:
            sys.exit()
main()