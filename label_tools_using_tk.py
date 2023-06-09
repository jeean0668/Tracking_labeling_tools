import cv2
from tkinter import Label, Tk, Button,ttk
from PIL import ImageTk,Image
import os

def main():
    
    global win, list2, com_box, path
    win = Tk()
    win.geometry("2000x2000")

    filters ="RGB","GRAY","HSV","FHSV","HLS"
    com_box = ttk.Combobox(win,values = filters)
    com_box.current(0)
    com_box.place(x=50,y=900,width = 100)
    
    path = "YOLOX_outputs/yolox_x_mix_det/track_vis/2023_04_02_05_46_10/images"
    myList = os.listdir(path)
    
    for i, fp in enumerate(myList):
        file_index = fp.split('.')[0]
        dst = os.path.join(path, f"{int(file_index):06d}.jpg")
        src = os.path.join(path, fp) 
        os.rename(src, dst)
    myList = os.listdir(path)
    myList = sorted(myList)
    list2 = []

    for _, imgs in enumerate(myList):    
        img =  imgs.split(".")
        if img[1] =="jpg" or img[1] =="png":
            list2.append(imgs)
    
    right = Button(win,text="▶",bg="gray",fg="white",command=counup).place(x=330,y=900,width = 40)
    left = Button(win,text="◀",bg="gray",fg="white",command=coundown).place(x=230,y=900,width = 40)

    win.mainloop()
    
def change_filter(img):
    if com_box.get() =="RGB":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if com_box.get() =="GRAY":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if com_box.get() =="HSV":
        img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    if com_box.get() =="FHSV":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
    if com_box.get() =="HLS":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    return img

# print(myList)
def to_display(img, label, x, y, w, h):
    print(img)
    image = Image.fromarray(img)
    #i mage = image.resize((w, h), Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(image)
    label.configure(image=pic)
    label.image = pic
    label.place(x=x, y=y)

def switch(i):
    label = Label(win, bg="black")
    img = cv2.imread(os.path.join(path, list2[i]))
    img = change_filter(img)
    to_display(img,label,150,20,300,400)

count = 0
#next img
def counup():
    global count
    count +=1
    if count > len(list2)-1:
        count = 0
    switch(count)

# previous img
def coundown():
    global count
    count -=1
    if count < 0:
        count = len(list2)-1
    switch(count)
#     win.after(700,coundown)
# coundown()



if __name__ == "__main__":
    main()