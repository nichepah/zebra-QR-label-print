# Author : Aneesh PA, RDCIS
# 20210626
# Takes input from user to print labels with QR
# For WRM, BSP 
# Remember 200 mm offset in the printer; try to reset it on site.
# Sqlite db to store label data; Offset eliminated after AG deployed his modules


import tkinter as tk
import os
import sqlite3
import datetime

myDir="C:/Users/Administrator_TATA/Documents/pa/gui/"
tempFile=myDir+"temp.txt"
dbfile=myDir+"print_db.db"

root=tk.Tk()

# the windows size
root.geometry("400x300")
root.title("QR Label Designer, CYMS WRM BSP")
root.iconbitmap(myDir+'sail.ico')

# declare string variable
heat_var=tk.StringVar()
grade_var=tk.StringVar()
dia_var=tk.StringVar()
date_var=tk.StringVar()
strand_var=tk.StringVar()
first_coil_var=tk.StringVar()
last_coil_var=tk.StringVar()
shift_var=tk.StringVar()

# checks if db exists
dbexist=os.path.exists(dbfile)  
db = sqlite3.connect(dbfile)
cur=db.cursor()
if not dbexist:
    sqlstring = 'CREATE TABLE T_QR_LABEL \
    (id INTEGER PRIMARY KEY, HEAT TEXT, GRADE TEXT, DIA TEXT, \
    COIL_NO TEXT, STRAND TEXT, PRINT_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)'
    cur.execute(sqlstring)
    db.commit()

def printLabel(heat, strand, first_coil, last_coil, grade, dia, date, shift):
    f=open(tempFile, "w")
    myRange=range(int(first_coil),int(last_coil)+1)
    # print(myRange)
    for i in myRange:
        f.writelines('CT~~CD,~CC^~CT~\n')
        f.writelines('^XA~TA000~JSN^LT0^MNW^MTT^PON^PMN^LH0,0^JMA^PR5,5~SD15^JUS^LRN^CI0^XZ\n')
        f.writelines('^XA^FO190,35^GFA,264,264,6,,L08,K01C,K07E,K0FF,J01FF8,J03FFC,J07FFE,J0JF,I01JF8,I03FE7FE,I07FC3FF,I0FF81FF8,001FF00FFC,003FE087FE,007FC1C3FF,00FF83E1FF8,01FF07F07FC,03FE0FF83FE,07FC1FFC1FF,07FC3FFE1FF,03FE7IF3FE,01NFC,00FF7IF7F8,007F3FFC7F,003F1FF87E,001F0FF07C,I0F07E078,I0703C07,I0301806,I01J04,,:I08,,I04,007FFC2114,0014084194,0034F83094,0024881094,I040804D6,,::^FS\n')
        f.writelines('^FO250,40^A0,30^FDSAIL BSP^FS\n')
        f.writelines('^FO190,90^A0,30^FDGrade:^FS\n')
        f.writelines('^FO190,+125^A0,30^FD'+grade+'^FS\n')
        f.writelines('^FO190,170^A0,30^FDDia:^FS\n')
        f.writelines('^FO255,155^A0,50^FD'+dia+'^FS\n')
        f.writelines('^FO302,170^A0,30^FDmm^FS')
        f.writelines('^FO190,210^A0,30^FDDt:'+date+'/'+shift+'^FS\n')
        numb=str(i)
        f.writelines('^FO190,255^A0,30^FDCoilNo:'+strand+numb+'^FS\n')
        # repositioned heat no
        f.writelines('^FO190,315^A0,30^FDHeatNo:^FS\n')
        f.writelines('^FO300,300^A0,80^FD'+heat+'^FS\n')
        # QR
        f.writelines('^FO395,30^BQN,2,6^FDQA,HeatNo:'+heat+' Grade:'+grade+' CoilNo:'+strand+numb+' Dia:'+dia+'mm Date'+date+'/'+shift+'^FS\n^XZ\n\n')
        sqlstring = 'INSERT INTO T_QR_LABEL (id, HEAT, GRADE, DIA, COIL_NO, \
        STRAND) VALUES(NULL, "%s", "%s", "%s", "%s", "%s")\
        '%(heat, grade, dia, numb, strand)
        cur.execute(sqlstring)
        db.commit()
    f.close()
    os.startfile(tempFile, "print")

# defining a function that will get the input from user 
def submit():
    heat=heat_var.get()
    strand=strand_var.get()
    first_coil=first_coil_var.get()
    last_coil=last_coil_var.get()
    grade=grade_var.get()
    dia=dia_var.get()
    date=date_var.get()
    shift=shift_var.get()
    print("heat : " + heat)
    print("strand : " + strand)
    print("first_coil : " + first_coil)
    print("last_coil : " + last_coil)
    print("grade : " + grade)
    print("dia : " + dia)
    print("date : " + date)
    heat_var.set("")
    strand_var.set("")
    first_coil_var.set("")
    last_coil_var.set("")    
    grade_var.set("")
    dia_var.set("")
    date_var.set("")
    shift_var.set("")
    printLabel(heat, strand, first_coil, last_coil, grade, dia, date, shift)
	
# creating a label for heat using widget Label
heat_label = tk.Label(root, text = 'HEAT', font=('calibre',15, 'bold'))
# creating a entry for input heat using widget Entry
heat_entry = tk.Entry(root,textvariable = heat_var, font=('calibre',15,'normal'))

# creating a label for strand using widget Label
strand_label = tk.Label(root, text = 'STRAND', font=('calibre',15, 'bold'))
# creating a entry for input strand using widget Entry
strand_entry = tk.Entry(root,textvariable = strand_var, font=('calibre',15,'normal'))

# creating a label for firstCoil using widget Label
first_coil_label = tk.Label(root, text = 'FROM COIL', font=('calibre',15, 'bold'))
# creating a entry for input first coil using widget Entry
first_coil_entry = tk.Entry(root,textvariable = first_coil_var, font=('calibre',15,'normal'))

# creating a label for coil count using widget Label
last_coil_label = tk.Label(root, text = 'TO COIL', font=('calibre',15, 'bold'))
# creating a entry for input heat using widget Entry
last_coil_entry = tk.Entry(root,textvariable = last_coil_var, font=('calibre',15,'normal'))

# grade Label
grade_label = tk.Label(root, text = 'GRADE', font=('calibre',15, 'bold'))
# grade Entry
grade_entry = tk.Entry(root,textvariable = grade_var, font=('calibre',15,'normal'))

# dia Label
dia_label = tk.Label(root, text = 'DIA', font=('calibre',15, 'bold'))
# dia Entry
dia_entry = tk.Entry(root,textvariable = dia_var, font=('calibre',15,'normal'))

# date Label
date_label = tk.Label(root, text = 'DATE', font=('calibre',15, 'bold'))
# date Entry
date_entry = tk.Entry(root,textvariable = date_var, font=('calibre',15,'normal'))

# shift Label
shift_label = tk.Label(root, text = 'SHIFT', font=('calibre',15, 'bold'))
# shift Entry
shift_entry = tk.Entry(root,textvariable = shift_var, font=('calibre',15,'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Print QR Label', command = submit)

# placing the label and entry in
# the required position using grid
# method
heat_label.grid(row=0,column=0)
heat_entry.grid(row=0,column=1)
strand_label.grid(row=1,column=0)
strand_entry.grid(row=1,column=1)
first_coil_label.grid(row=2,column=0)
first_coil_entry.grid(row=2,column=1)
last_coil_label.grid(row=3,column=0)
last_coil_entry.grid(row=3,column=1)
grade_label.grid(row=4,column=0)
grade_entry.grid(row=4,column=1)
dia_label.grid(row=5,column=0)
dia_entry.grid(row=5,column=1)
date_label.grid(row=6,column=0)
date_entry.grid(row=6,column=1)
shift_label.grid(row=7,column=0)
shift_entry.grid(row=7,column=1)
sub_btn.grid(row=8,column=1)

# performing an infinite loop for the window to display
root.mainloop()
