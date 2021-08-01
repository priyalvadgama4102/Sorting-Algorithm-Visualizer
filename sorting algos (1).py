import random
from tkinter import *
from tkinter import ttk
from bubblesort import bubble_sort
from qicksort import quick_sort
from mergesort import merge_sort

root = Tk()
root.title('Sorting Algorithms Visualiser')
#root.geometry('900x600+200+80')
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" %(width,height))
root.config(bg='#082A46')
data = []


def drawData(data, colorArray):
    canvas.delete("all")
    canvas_height = 650
    canvas_width = 1490
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rect = 10
    normalized_data = [i / max(data) for i in data]
    print(data)
    print(normalized_data)
    for i, height in enumerate(normalized_data):
        #print(i,height)
        x0 = i * x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 400
        x1 = (i + 1) * x_width
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), font=("new roman", 14, "italic bold"),
                           fill="orange")

    root.update_idletasks()


def Startalgorithm():
    global data
    if not data:
        # novalue = Label(canvas, text="you have to enter data: ", font=("new roman", 16, "italic bold"), bg="#0E6DA5",
        #                       width=80, fg="orange", height=20, relief=GROOVE, bd=5)
        # canvas.place(x=0,y=0)
        return

    if algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, drawData, speedscale.get())

    elif algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedscale.get())

    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedscale.get())
    drawData(data, ['green' for x in range(len(data))])


def Generate():
    global data
    #print('Select Algorithm: ' + selected_algorithm.get())
    minivalue = int(minvalue.get())
    maxivalue = int(maxvalue.get())
    sizeevalue = int(sizevalue.get())

    data = []

    for _ in range(sizeevalue):
        data.append(random.randrange(minivalue, maxivalue + 1))

    drawData(data, ['#A90042' for x in range(len(data))])


selected_algorithm = StringVar()
# label,buttons,speed scale
mainlabel = Label(root, text="Algorithm: ", font=("new roman", 16, "italic bold"), bg="red",
                  width=10, fg="black", relief=GROOVE, bd=5)
mainlabel.place(x=0, y=0)

algo_menu = ttk.Combobox(root, width=15, font=("new roman", 19, "italic bold"), textvariable=selected_algorithm,
                         values=['Bubble Sort', 'Merge Sort', 'Quick Sort'])
algo_menu.place(x=145, y=0)
algo_menu.current(0)  # by default bubble sort

random_generate = Button(root, text="Generate", bg="pink", font=("arial", 12, "italic bold"), relief=SUNKEN,
                         activebackground="#05945B", activeforeground="white", bd=5, width=20,height=2,
                         command=Generate)
random_generate.place(x=1259, y=62)

sizevaluelabel = Label(root, text="Size: ", font=("new roman", 16, "italic bold"), bg="#0E6DA5",
                       width=10, fg="black", height=2, relief=GROOVE, bd=5)
sizevaluelabel.place(x=0, y=60)

sizevalue = Scale(root, from_=0, to=30, resolution=1, orient=HORIZONTAL, font=("arial", 14, "italic bold"),
                  relief=GROOVE, bd=2, width=10)
sizevalue.place(x=150, y=65)

minvaluelabel = Label(root, text="Min value: ", font=("new roman", 16, "italic bold"), bg="#0E6DA5",
                      width=10, fg="black", height=2, relief=GROOVE, bd=5)
minvaluelabel.place(x=270, y=60)

minvalue = Scale(root, from_=0, to=10, resolution=1, orient=HORIZONTAL, font=("arial", 14, "italic bold"),
                 relief=GROOVE, bd=2, width=10)
minvalue.place(x=420, y=65)

maxvaluelabel = Label(root, text="Max Value: ", font=("new roman", 16, "italic bold"), bg="#0E6DA5",
                      width=10, fg="black", height=2, relief=GROOVE, bd=5)
maxvaluelabel.place(x=540, y=60)

maxvalue = Scale(root, from_=0, to=100, resolution=1, orient=HORIZONTAL, font=("arial", 14, "italic bold"),
                 relief=GROOVE, bd=2, width=10)
maxvalue.place(x=690, y=65)

start = Button(root, text="Start", bg="#C45809", font=("arial", 12, "italic bold"), relief=SUNKEN,
               activebackground="#05945B", activeforeground="white", bd=5, width=20,height=2, command=Startalgorithm)
start.place(x=1260, y=0)

speedlabel = Label(root, text="Speed: ", font=("new roman", 16, "italic bold"), bg="#0E6DA5",
                   width=12, fg="black", relief=GROOVE, bd=5)
speedlabel.place(x=855, y=8)

speedscale = Scale(root, from_=0.1, to=5.0, resolution=0.2, length=200, digits=2, orient=HORIZONTAL,
                   font=("arial", 14, "italic bold"), fg="#1AA3E8",bg="#AEDCED",relief=GROOVE, bd=2, width=5)
speedscale.place(x=1030, y=7)

canvas = Canvas(root, width=1490, height=650, bg="black")
canvas.place(x=10, y=130)

root.mainloop()