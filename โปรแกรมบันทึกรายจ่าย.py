from tkinter import *
from tkinter import ttk
import csv
from datetime import datetime

UI = Tk()
UI.title('โปรแกรมบันทึกรายจ่าย')
UI.geometry('500x500')

F1 = Frame(UI)
F1.place(x=150,y=50)


def Save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    quantity = v_quantity.get()
    total = int(price) * int(quantity)
    print('รายการ: {} ราคา: {} บาท ' .format(expense,price))
    print('จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total))
    v_expense.set('')
    v_price.set('')
    v_quantity.set('')

    #บันทึกข้อมูลลง csv
    dt = datetime.now().strftime('%yY-%m-%d %H:%M:%S')
    with open('savedata.csv','a',encoding='utf-8',newline='') as f:
        # with คือ สั่งเปิดไฟล์แล้วปิดอัตโนมัติ
        # a คือ การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
        # newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
        fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
        data = [expense,price,quantity,total]
        fw.writerow(data)

    #ทำให้เคอเซอร์กลับไปช่องกลอก E1
    E1.focus()

UI.bind('<Return>', Save)        
    
FONT1 = ('Angsana New' , 25)
FONT2 = ('Angsana New' , 30)

########## text 1 ############

L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font = FONT2).pack()
v_expense = StringVar()
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()

##############################

########## text 2 ############

L = ttk.Label(F1,text='ราคา',font = FONT2).pack()
v_price = StringVar()
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()

##############################

########## text 3 ############

L = ttk.Label(F1,text='จำนวน ',font = FONT2).pack()
v_quantity = StringVar()
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()

##############################

B2 = ttk.Button(F1,text='SAVE',command=Save)
B2.pack(ipadx=50,ipady=20)

UI.bind('<Tab>',lambda x: E2.focus())
UI.mainloop()
