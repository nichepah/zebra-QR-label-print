# gui_3
# Author : Aneesh PA, RDCIS
# 20210520
# Takes input from user to print labels with QR
# For WRM, BSP 
# Remember 200 mm offset in the printer; try to reset it on site.

import Tkinter as tk
import os

root=tk.Tk()

# the windows size
root.geometry("400x300")

# declare string variable
heat_var=tk.StringVar()
grade_var=tk.StringVar()
dia_var=tk.StringVar()
date_var=tk.StringVar()
strand_var=tk.StringVar()
firstCoil_var=tk.StringVar()
coilCount_var=tk.StringVar()
shift_var=tk.StringVar()

tempFile="C:/Users/aapc-pa/Documents/mattrack/label_print_test/code_zpl/label/temp.txt"

def printLabel(heat, strand, firstCoil, coilCount, grade, dia, date, shift):
    f=open(tempFile, "w")
    myRange=range(int(coilCount))
    print(myRange)
    for i in myRange:
        f.writelines('CT~~CD,~CC^~CT~\n')
        f.writelines('^XA~TA000~JSN^LT0^MNW^MTT^PON^PMN^LH0,0^JMA^PR5,5~SD15^JUS^LRN^CI0^XZ\n')
        f.writelines('^XA^FO210,35^GFA,264,264,6,,L08,K01C,K07E,K0FF,J01FF8,J03FFC,J07FFE,J0JF,I01JF8,I03FE7FE,I07FC3FF,I0FF81FF8,001FF00FFC,003FE087FE,007FC1C3FF,00FF83E1FF8,01FF07F07FC,03FE0FF83FE,07FC1FFC1FF,07FC3FFE1FF,03FE7IF3FE,01NFC,00FF7IF7F8,007F3FFC7F,003F1FF87E,001F0FF07C,I0F07E078,I0703C07,I0301806,I01J04,,:I08,,I04,007FFC2114,0014084194,0034F83094,0024881094,I040804D6,,::^FS\n')
        f.writelines('^FO260,40^A0,40^FDSAIL BSP WRM^FS\n')
        f.writelines('^FO210,100^A0,30^FDHEAT:'+heat+'/'+strand+str(int(firstCoil)+i)+'^FS\n')
        f.writelines('^FO210,140^A0,30^FDGRADE:'+grade+'^FS\n')
        f.writelines('^FO210,180^A0,30^FDDIA:'+dia+'^FS\n')
        f.writelines('^FO210,220^A0,30^FDDATE:'+date+'^FS\n')
        f.writelines('^FO210,260^A0,30^FDSHIFT:'+shift+'^FS\n')
        f.writelines('^FO430,80^BQN,2,6^FDQA,HEAT:'+heat+'/'+strand+str(i+1)+';GRADE:'+grade+';DIA:'+dia+';DT:'+date+'/'+shift+'^FS\n^XZ\n')
    f.close()
    os.startfile(tempFile, "print")

# defining a function that will get the input from user 
def submit():
    heat=heat_var.get()
    strand=strand_var.get()
    firstCoil=firstCoil_var.get()
    coilCount=coilCount_var.get()
    grade=grade_var.get()
    dia=dia_var.get()
    date=date_var.get()
    shift=shift_var.get()
    print("heat : " + heat)
    print("strand : " + strand)
    print("firstCoil : " + firstCoil)
    print("coilCount : " + coilCount)
    print("grade : " + grade)
    print("dia : " + dia)
    print("date : " + date)
    heat_var.set("")
    strand_var.set("")
    firstCoil_var.set("")
    coilCount_var.set("")    
    grade_var.set("")
    dia_var.set("")
    date_var.set("")
    shift_var.set("")
    printLabel(heat, strand, firstCoil, coilCount, grade, dia, date, shift)
	
# creating a label for heat using widget Label
heat_label = tk.Label(root, text = 'HEAT', font=('calibre',15, 'bold'))
# creating a entry for input heat using widget Entry
heat_entry = tk.Entry(root,textvariable = heat_var, font=('calibre',15,'normal'))

# creating a label for strand using widget Label
strand_label = tk.Label(root, text = 'STRAND', font=('calibre',15, 'bold'))
# creating a entry for input strand using widget Entry
strand_entry = tk.Entry(root,textvariable = strand_var, font=('calibre',15,'normal'))

# creating a label for firstCoil using widget Label
firstCoil_label = tk.Label(root, text = 'FIRST COIL', font=('calibre',15, 'bold'))
# creating a entry for input first coil using widget Entry
firstCoil_entry = tk.Entry(root,textvariable = firstCoil_var, font=('calibre',15,'normal'))

# creating a label for coil count using widget Label
coilCount_label = tk.Label(root, text = 'COIL COUNT', font=('calibre',15, 'bold'))
# creating a entry for input heat using widget Entry
coilCount_entry = tk.Entry(root,textvariable = coilCount_var, font=('calibre',15,'normal'))

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
firstCoil_label.grid(row=2,column=0)
firstCoil_entry.grid(row=2,column=1)
coilCount_label.grid(row=3,column=0)
coilCount_entry.grid(row=3,column=1)
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
