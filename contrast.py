from tkinter import *
import tkinter.filedialog
root = Tk()
list_file = []

def xz():
    filenames = tkinter.filedialog.askopenfilenames()
    print(" you choose file is",filenames)
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

lb = Label(root,text = '')
lb.pack()
btn = Button(root,text="弹出选择文件对话框",command=xz)
btn.pack()
root.mainloop()



# link http://blog.csdn.net/Abit_Go/article/details/77938938