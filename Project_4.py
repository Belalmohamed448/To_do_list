tasks=[] #global variable
def add_task():
    task=input("enter your task: ")
    tasks.append(task)

def remove_task():
    if len(tasks)==0:
        print("no tasks to remove")
        return
    view_allTasks()
    index=int(input("enter index to remove: "))
    if index>len(tasks) or index<=0:
        print("invalid input")
    else:
        tasks.pop(index-1)

def view_allTasks():
    if len(tasks)==0:
        print("Empty")
    else:
        print("YOUR TO DO LIST ")
        for i in range (len(tasks)):
            print(f"{i+1}.{tasks[i]}")


def menu():
    print("==========\nTO DO LIST\n==========")
    print("1.add task")
    print("2.remove task")
    print("3.view all tasks")
    print("4.exit")
    op=int(input("choose: "))
    n=0
    if op==1:
        add_task()
       
    elif op==2:
        remove_task()
    elif op==3:
        view_allTasks()
    elif op==4:
        exit()
    else:
        print("invalid index")

def main():
    while True:
        menu()
        print("-"*20)
main()