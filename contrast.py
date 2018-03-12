from tkinter import *
import tkinter.filedialog
import os
import xlrd
import xlwt
from xlutils.copy import copy

root = Tk()
root.title('contrast the differences of the two files (you must choose forment is xls)')
root.geometry('400x200') 

list_file = []

def xz():
    filenames = tkinter.filedialog.askopenfilenames()
    print(" you choose file is",filenames)
    filenames_list = list(filenames)
    filenames_str =  filenames_list[0]
    if not is_xls(filenames_str):
        print(" is xls",is_xls(str(filenames)))
        lb.config(text = "this file is not xls");
        return

    if len(filenames) != 0:
        list_file.append(filenames)
        if(2 == len(list_file)):
            print("end ......")
            root.destroy()
            contrast_file()
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
    if not os.path.isfile(file):
        mark = False
    if not file.endswith('.xls'):
        mark = False
    return mark
    

# contrast two file 
def contrast_file():

    list_file0 = list_file[0]
    list_file1 = list_file[1]

    # book1 book2 read 
    book0_r  = xlrd.open_workbook(list_file[0])
    book1_r  = xlrd.open_workbook(list_file[1])

    sheets0_r=book0_r.sheets()
    sheets1_r=book1_r.sheets()

    list_sheet_dif = []

    for item0 in sheets0_r:
        for item1 in sheets1_r:
            if item0.name == item1.name:
                list_sheet_dif.append({"left":item0.name,"right":item1.name})

    # print(list_sheet_dif)

    list_dif = []

    for dic in list_sheet_dif:
        name0 = dic["left"]
        name1 = dic["right"]
        sheet0 = book0_r.sheet_by_name(name0)
        sheet1 = book1_r.sheet_by_name(name1)





        rows0 = sheet0.nrows
        rows1 = sheet1.nrows

        cols0 = sheet0.ncols
        cols1 = sheet1.ncols
        

        for row in range(rows0):
            for col in range(cols0):
                print("aaa",row,"bbb",col)
                cell0 = sheet0.cell_value(row,col)
                cell1 = sheet1.cell_value(row,col)
                # warning need judge row adn col 
                if cell0 != cell1:
                    list_dif.append({"sheet_name":name0,"row":row,"col":col,"val":cell0})



    # write to xls for dif data
        # 设置单元格颜色
    pattern = xlwt.Pattern() # Create the Pattern
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    pattern.pattern_fore_colour = 5 # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
    style = xlwt.XFStyle() # Create the Pattern
    style.pattern = pattern # Add Pattern to Style

    book0_w = xlrd.open_workbook(list_file0,formatting_info=True)
    book0_w_copy = copy(book0_w)
    for dic in list_dif:
        sheet_w = book0_w_copy.get_sheet(dic["sheet_name"])
        sheet_w.write(dic['row'], dic['col'],dic['val'],style)

    book0_w_copy.save("dif.xls")









    print("you come here ...")
    




# # # start

# lb = Label(root,text = '')
# lb.pack()
# btn = Button(root,text="弹出选择文件对话框",command=xz)
# btn.pack()
# root.mainloop()
list_file = ["model.xls","model1.xls"]
contrast_file()









# link http://blog.csdn.net/Abit_Go/article/details/77938938