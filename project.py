#BY นายกิจจาวุฒิ  เดชานุภากรณ์
from tkinter import *
import tkinter.messagebox


window = Tk()
window.title("โปรแกรมคำนวณหาพื้นที่สี่เหลี่ยมผืนผ้า")  #ชื่อโปรแกรม
window.geometry("500x400+500+250")  #กำหนดขนาดหน้าจอและตำแหน่ง


#ชื่อหัวข้อ
mylabel = Label(text="โปรแกรมคำนวณหาพื้นที่สี่เหลี่ยมผืนผ้า",fg="#000000",font="Helvetica 18 bold italic")
mylabel.pack(pady=15)


#Allfunction
#แสดงผลลัพธ์หลังจากคำนวณ
def result():
    wide = int(input_wide.get())
    long = int(input_long.get())
    area = str(wide * long)
    print(area)
    Label(window,text=area,font="Verdana 25 bold",fg="#15EA00",bg="#878787",width=50,height=50).pack(pady=80)
#จัดทำโดย
def aboutme():
    tkinter.messagebox.showinfo("จัดทำโดย","นาย กิจจาวุฒิ  เดชานุภากรณ์")
#ล้างข้อมูล
def deleteText():
    input_wide.delete(0,END)
    input_long.delete(0,END)
#ออกจากโปรแกรม
def exitprogram():
    confirm = tkinter.messagebox.askquestion("ออกจากโปรแกรม","คุณต้องการออกจากโปรแกรมหรือไม่ ?")
    if confirm == "yes":
        window.destroy()


#กล่องกรอกข้อมูล
#ความกว้างของสี่เหลี่ยมผืนผ้า
Label(text="ความกว้าง",font=16).pack()
input_wide = Entry(width=28)
input_wide.pack(pady=5)

#ความยาวของสี่เหลี่ยมผืนผ้า
Label(text="ความยาว",font=16).pack()
input_long = Entry(width=28)
input_long.pack()


#AllButton
#ปุ่มคำนวณผลลัพธ์
btn = Button(window,text="คำนวณ",width=12,bg="#15EA00",command=result)
btn.place(x=165,y=185)

#ปุ่มเครดิต
btn1 = Button(window,text="จัดทำโดย",command=aboutme)
btn1.place(x=9,y=367)

#ปุ่มออกจากโปรแกรม
exit = Button(window,text="ออกจากโปรแกรม",command=exitprogram)
exit.place(x=403,y=367)

#ปุ่มล้างข้อมูล
dele = Button(window,text="ล้างข้อมูล",fg="#ffffff",bg="#D00000",width=8,command=deleteText)
dele.place(x=270,y=185)


window.mainloop()