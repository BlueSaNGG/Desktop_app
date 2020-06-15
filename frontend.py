""" 
A program that stores this book information:
Title, Author
year,ISBN

user can:

View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
from backend import Database

database=Database() #建立对象
#启动init
#执行完毕则del执行


class Window:
    def __init__(self,window):
        self.window=window
        self.window.wm_title("BookStore")  #设置名称

        l1=Label(self.window,text="Title")
        l1.grid(row=0,column=0)

        l2=Label(self.window,text="Author")
        l2.grid(row=0,column=2)

        l3=Label(self.window,text="Year")
        l3.grid(row=1,column=0)

        l4=Label(self.window,text="ISBN")
        l4.grid(row=1,column=2)

        self.Title_text=StringVar()
        self.e1=Entry(self.window,textvariable=self.Title_text)
        self.e1.grid(row=0,column=1)

        self.Author_text=StringVar()
        self.e2=Entry(self.window,textvariable=self.Author_text)
        self.e2.grid(row=0,column=3)

        self.Year_text=StringVar()
        self.e3=Entry(self.window,textvariable=self.Year_text)
        self.e3.grid(row=1,column=1)

        self.ISBN_text=StringVar()
        self.e4=Entry(self.window,textvariable=self.ISBN_text)
        self.e4.grid(row=1,column=3)

        self.list1=Listbox(self.window,height = 10,width=40)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)

        #scrollbar
        sb1=Scrollbar(self.window)
        sb1.grid(row=2,column=2,rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)  #list1的y轴受sb1的y轴控制
        sb1.configure(command=self.list1.yview)    #sb1的y轴控制list1的y轴


        #bind 用于将函数作用于list，函数为get_selected_row
        self.list1.bind("<<ListboxSelect>>",self.get_selected_row)


        #6个按钮
        b1=Button(self.window,text="View all",width=12,command=self.view_command)   #commanda设置功能  若加（），则编译时就会执行这段代码
        b1.grid(row=2,column=3)

        b2=Button(self.window,text="Search entry",width=12,command=self.search_command)  #不能加括号，但是要传入参数
        b2.grid(row=3,column=3)

        b3=Button(self.window,text="Add entry",width=12,command=self.add_command)
        b3.grid(row=4,column=3)

        b4=Button(self.window,text="Update selected",width=12,command=self.update_command)
        b4.grid(row=5,column=3)

        b5=Button(self.window,text="Delete selected",width=12,command=self.delete_command)  #需要得到list1被选中的那行
        b5.grid(row=6,column=3)

        b6=Button(self.window,text="Close",width=12,command=self.window.destroy)  #关闭窗口
        b6.grid(row=7,column=3)

    def get_selected_row(self,event):  #固定的传入
        #self.selected_tuple   #全局变量
        try:
            index = self.list1.curselection()[0]       #得到被选中的那行的行数
            self.selected_tuple=self.list1.get(index)   #get得到地index行
            #return selected_tuple  #有了全局变量，则无需返回
            #在上面显示被选中的内容
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])
        except:
            pass


    def view_command(self):
        self.list1.delete(0,END)  #清除list1中所有的东西
        for row in database.view():
            self.list1.insert(END,row)   #End表示放在listbox的最后

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.Title_text.get(),self.Author_text.get(),self.Year_text.get(),ISBN_text.get()):
            self.list1.insert(END,row)

    def add_command(self):
        database.insert(self.Title_text.get(),self.Author_text.get(),self.Year_text.get(),self.ISBN_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.Title_text.get(),self.Author_text.get(),self.Year_text.get(),self.ISBN_text.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])
        self.view_command()

    def update_command(self):
        database.update(self.selected_tuple[0],self.Title_text.get(),self.Author_text.get(),self.Year_text.get(),self.ISBN_text.get())
        self.view_command()



window=Tk()
Window(window)
window.mainloop()