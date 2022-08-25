from tkinter import *
from tkinter import messagebox

tasks_list = []
counter= 1

def inputError():
    if enterTaskField.get() == "" :
        messagebox.showerror("Input Error")
        print("Please Enter a task")
        return 0
    return 1

def clear_taskNumberArea():
    taskNumberArea.delete(0.0, END)

def clear_taskField():
    enterTaskField.delete(1.0, END)

def insertTask():
    global counter

    Value = inputError()

    if Value == 0:
        return

    content = enterTaskField.get() + "\n"
    tasks_list.append(content)

    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)

    counter += 1

    clear_taskField()

def delete():
    global counter

    if len(tasks_list) == 0:
        messagebox.showerror("No more Task")
        return

    number = taskNumberArea.get(1.0, END)

    if number == "\n":
        messagebox.showerror("Input Error")
        return

    else:
        task_number = int(number)

    clear_taskNumberArea()

    tasks_list.pop(task_number - 1)

    counter -= 1

    TextArea.delete(1.0, END)

    for i in range(len(tasks_list)) :
	    TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])




if __name__ == "__main__":
    gui = Tk()

    # gui bg_frame
    gui.configure(background="#191925")
    gui.title("MY-TODO-LIST app")
    gui.geometry("325x600")

    #label for enter task
    enterTask = Label(gui, text = "Enter your task", bg = "white")
    enterTask.grid(row=0, column=2, pady=5)

    #label for enter task field
    enterTaskField = Entry(gui)
    enterTaskField.grid(row=1, column=2, ipadx=60, pady=3, ipady=3)

    #submit button
    Submit = Button(gui, text = "Submit", fg = "white", bg = "green", command = insertTask)
    Submit.grid(row=2, column=2)

    #task display area
    TextArea = Text(gui, height = 7, width = 20, font = "lucida 13")
    TextArea.grid(row=3, column=2, padx=10, pady=2, sticky=W, ipadx=60)

    #completed tasks
    completedTaskArea = Text(gui, height = 7, width = 20, font = "lucida 13")
    completedTaskArea.grid(row=4, column=2, padx=10, pady=20, sticky=W, ipadx=60)

    #task number label
    taskNumber = Label(gui, text="Delete Task Number", bg="red", fg="white")
    taskNumber.grid(row=5, column=2, pady=5)

    #task number area
    taskNumberArea = Text(gui, height=1, width=2, font="lucida 13", bg="yellow")
    taskNumberArea.grid(row=6, column=2, pady=5)

    #delete button
    Delete = Button(gui, text="Delete", fg="white", bg="red", command= delete)
    Delete.grid(row=7, column=2)

    #Exit button
    Xxit = Button(gui, text="Exit", bg="green", fg="white", command= exit)
    Xxit.grid(row=8, column=2, pady=5)


    gui.mainloop()

