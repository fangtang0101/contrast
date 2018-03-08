from tkinter import *
import tkinter.filedialog
import os

root = Tk()
root.title('contrast the differences of the two files (you must choose forment is xls)')
root.geometry('400x200') 

list_file = []

def xz():
    filenames = tkinter.filedialog.askopenfilenames()
    print(" you choose file is",filenames)
    if not is_xls(str(filenames)):
        print(" is xls",is_xls(str(filenames)))
        lb.config(text = "this file is not xls");
        return

    if len(filenames) != 0:
        list_file.append(filenames)
        if(2 == len(list_file)):
            print("end ......")
            root.destroy()
        else:
            string_filename =""
            for i in range(0,len(filenames)):
                string_filename += str(filenames[i])+"\n"
            lb.config(text = "您选择的文件是："+string_filename)
    else:
        lb.config(text = "您没有选择任何文件");

# def  is file (xls)
def is_xls(file):
    mark = True
    if os.path.isfile(file):
        mark = False
    if not file.endswith('.xls'):
        mark = False
    return mark
    

# contrast two file 
def contrast_file():
    pass




# # # start

lb = Label(root,text = '')
lb.pack()
btn = Button(root,text="弹出选择文件对话框",command=xz)
btn.pack()
root.mainloop()



# link http://blog.csdn.net/Abit_Go/article/details/77938938