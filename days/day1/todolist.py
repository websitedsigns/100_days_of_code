# 100 Days of Code - Day 1
# a simple to-do list program

todo_list = []

def show_menu():
    
    print("\n 100 DAYS OF CODE DAY 1")
    print("\n To Do List App:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove Task")
    print("4. Exit")
    
def view_tasks():
    if not todo_list:
        print("No tasks to display.")
    else:
        print("Tasks")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
            
def add_task():
    task = input("\n Enter a task: ")
    todo_list.append(task)
    print(f"\n Task '{task}' has been added.")
    
def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("\n Enter the task number to remove: "))
            if task_num > 0 and task_num <= len(todo_list):
                print("invalid task number")
            else:
                removed_task = todo_list.pop(task_num - 1)
                print(f"\n Task '{removed_task}' has been removed.")
        except ValueError:
            print("\n Please enter a valid task number.")

def main():
    while True:
        show_menu()
        choice = input("\n Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            break
        else:
            print("\n Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
    
# End of todolist.py