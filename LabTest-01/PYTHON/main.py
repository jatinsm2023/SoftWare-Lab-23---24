import tkinter as tk
from tkinter import ttk
import random
import numpy as np

Mat1 = []
Mat2 = []

def Create(frame):
    frame.destroy()
    frame = ttk.Frame(root)
    frame.pack(expand=True, fill="both", padx=10, pady=10)
    
    label_M = tk.Label(frame, text = "Enter M")
    label_M.pack()
    entry_M = tk.Entry(frame)
    entry_M.pack()
    
    label_Type = tk.Label(frame, text= "Enter Data Type :- Odd / Even")
    label_Type.pack()
    entry_type = tk.Entry(frame)
    entry_type.pack()
    
    label_range = tk.Label(frame, text="Enter Range :")
    label_range.pack()
    label_x= tk.Label(frame, text="Enter x:")
    label_x.pack()
    entry_x = tk.Entry(frame)
    entry_x.pack()
    label_y= tk.Label(frame, text="Enter y:")
    label_y.pack()
    entry_y = tk.Entry(frame)
    entry_y.pack()
    def Do():
        if entry_type.get() == 'Odd':
            f = open("Odd.dat", 'a')
            for _ in range(0,int(entry_M.get())):
                num = random.randint(int(entry_x.get()),int(entry_y.get()))
                if num % 2 == 0:
                    f.write(str(num+1)+"\n")
                else :
                    f.write(str(num)+"\n")
            f.close()
        if entry_type.get() == 'Even':
            f = open("Even.dat", 'a')
            for _ in range(0,int(entry_M.get())):
                num = random.randint(int(entry_x.get()),int(entry_y.get()))
                if num % 2 == 0:
                    f.write(str(num)+"\n")
                else :
                    f.write(str(num+1)+"\n")
            f.close()
    print("Hello")
    register_button = tk.Button(frame, text="Enter", command=Do)
    register_button.pack(pady=10)
    

def GetM(frame):
    frame.destroy()
    frame = ttk.Frame(root)
    frame.pack(expand=True, fill="both", padx=10, pady=10)
    
    label_m = tk.Label(frame, text = "Enter m")
    label_m.pack()
    entry_m = tk.Entry(frame)
    entry_m.pack()
    
    label_n = tk.Label(frame, text = "Enter n")
    label_n.pack()
    entry_n = tk.Entry(frame)
    entry_n.pack()
    
    label_major = tk.Label(frame, text = "Enter Major (Row/Coulumn)")
    label_major.pack()
    entry_major = tk.Entry(frame)
    entry_major.pack()
    
    label_file = tk.Label(frame, text = "Enter File Name: (Odd / Even)")
    label_file.pack()
    entry_file = tk.Entry(frame)
    entry_file.pack()
    
    def GetDo():
        ll = []
        if entry_file.get() == 'Odd':
            p = open("Odd.dat", "r")
            for each in p:
                ll.append(int(each))
            l1 =[]

            for i in range(0, int(entry_n.get())):
                for j in range(i*int(entry_m.get()), (i+1)*int(entry_m.get())):
                    l1.append(ll[j])
                Mat1.append(l1)
        if entry_file.get() == 'Even':
            p = open("Even.dat", "r")
            for each in p:
                ll.append(int(each))
            l1 =[]

            for i in range(0, int(entry_n.get())):
                for j in range(i*int(entry_m.get()), (i+1)*int(entry_m.get())):
                    l1.append(ll[j])
                Mat2.append(l1)
  
    register_button = tk.Button(frame, text="Enter", command=GetDo)
    register_button.pack(pady=10)
    
    registr_button = tk.Button(frame, text="Merge", command=Merge)
    registr_button.pack(pady=10)
    
def Merge():
    C = np.matmul(Mat1,Mat2)
    print (C)
    
# Main window
root = tk.Tk()
root.title("Python Imaging")
root.geometry("400x400")

# Frame to hold the content
main_frame = ttk.Frame(root)
main_frame.pack(expand=True, fill="both", padx=10, pady=10)

# Buttons
button1 = tk.Button(
    main_frame, text="Create Data File", command=lambda: Create(main_frame)
)
button1.pack(pady=10)

button2 = tk.Button(main_frame, text="Get Matrix", command=lambda: GetM(main_frame))
button2.pack(pady=10)

button3 = tk.Button(main_frame, text="Merge Matrices", command=lambda: Merge())
button3.pack(pady=10)

# button3 = tk.Button(main_frame, text="Display Image", command=lambda: Display(main_frame))
# button3.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
