import sqlite3

class Database:  #类
    #构造函数
    def __init__(self):  #默认执行的动作  即构造函数 #需要加入self，即构造的那个对象
        self.conn = sqlite3.connect("books.db")
        self.cur=self.conn.cursor()  #构造函数连接database并构造cursor
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text, author text, year integer, isbn integer)")
        self.conn.commit()  #commit change
        #conn.close()
        #无需关闭，调用类则一直连接


    #插入func
    def insert(self,title,author,year,isbn):
        #conn = sqlite3.connect("books.db")  #connect to database  #无需连接
        #cur=conn.cursor()  #无需创建cursor
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        #conn.close()

    def view(self):
        #conn = sqlite3.connect("books.db")  #connect to database
        #cur=conn.cursor()
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        #conn.close()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        #conn = sqlite3.connect("books.db")  #connect to database
        #cur=conn.cursor()
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()             #cursor 来fetchall
        #conn.close()   
        return rows
        
    #选中一行删除
    def delete(self,id):           #得到id，去SQL删除该id
        #conn = sqlite3.connect("books.db")  #connect to database
        #cur=conn.cursor()
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
        #conn.close()

    #选中一行修改
    def update(self,id,title,author,year,isbn):
        #conn = sqlite3.connect("books.db")  #connect to database
        #cur=conn.cursor()
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id =?",(title,author,year,isbn,id))
        self.conn.commit()
        #conn.close()
    
    #关闭链接
    def __del__(self):
        self.conn.close()


#self.cur 作为全局变量

#connect()
#insert("The Sun","John Smith",1918,9132131)
#delete(3)
#update(2,"The shy","SJ",2020,123213)
# print(view())
#print(search(author="John Smith"))