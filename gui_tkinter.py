from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import os
import time
# check if 
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

window = Tk()
window.geometry('480x320')
window.title('PI GUI')
window.attributes('-fullscreen', True) 
# # Create a photoimage object of the image in the path
# image1 = Image.open("/home/pi/python-projects/thinking.gif")
# resized_image= image1.resize((200,200))
# test = ImageTk.PhotoImage(resized_image)

# label2 = Label(window, width=200, height=200, image=test)
# label2.image = test

# # Position image
# label2.place(x=10, y=100)

label1 = Label(window, text='Hello World', fg='orange', bg='black', font=('Helvetica', 20), relief='groove')
label1.grid(row=0, column=0,ipadx=20, padx=20, pady=20)

file="/home/pi/python-projects/smiley.gif"

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains
print(frames)
# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = window.after(50,lambda :animation(count))

def stop_animation():
    window.after_cancel(anim)

gif_label = tk.Label(window,image="")
gif_label.grid()
animation(count)

def showMsg(): 
    pass
    # label_welcome = Label(window, text='Welcome', fg='orange', bg='black', font=('Helvetica', 20), relief='groove')
    # label_welcome.grid(row=0, column=0,ipadx=20, padx=20, pady=20)


#create Button
btn = Button(window, text='Click Me', command=showMsg())
btn.grid()
# start = tk.Button(window,text="start",command=lambda :animation(count))
# start.pack()

# stop = tk.Button(window,text="stop",command=stop_animation)
# stop.pack()

window.mainloop()

# class MyLabel(Label):
#     def __init__(self, master, filename):
#         im = Image.open(filename)
#         seq =  []
#         try:
#             while 1:
#                 seq.append(im.copy())
#                 im.seek(len(seq)) # skip to next frame
#         except EOFError:
#             pass # we're done

#         try:
#             self.delay = im.info['duration']
#         except KeyError:
#             self.delay = 100

#         first = seq[0].convert('RGBA')
#         self.frames = [ImageTk.PhotoImage(first)]

#         Label.__init__(self, master, image=self.frames[0])

#         temp = seq[0]
#         for image in seq[1:]:
#             temp.paste(image)
#             frame = temp.convert('RGBA')
#             self.frames.append(ImageTk.PhotoImage(frame))

#         self.idx = 0

#         self.cancel = self.after(self.delay, self.play)

#     def play(self):
#         self.config(image=self.frames[self.idx])
#         self.idx += 1
#         if self.idx == len(self.frames):
#             self.idx = 0
#         self.cancel = self.after(self.delay, self.play)        


# root = Tk()
# anim = MyLabel(root, '/home/pi/python-projects/my-love.gif')
# anim.pack()

# def stop_it():
#     anim.after_cancel(anim.cancel)

# Button(root, text='stop', command=stop_it).pack()

# root.mainloop()

# class ImageLabel(tk.Label):
#     """a label that displays images, and plays them if they are gifs"""
#     def load(self, im):
#         if isinstance(im, str):
#             im = Image.open(im)
           
#         self.loc = 0
#         self.frames = []

#         try:
#             for i in count(1):
#                 self.frames.append(ImageTk.PhotoImage(im.copy()))
#                 im.seek(i)
#         except EOFError:
#             pass

#         try:
#             self.delay = im.info['duration']
#         except:
#             self.delay = 10

#         if len(self.frames) == 1:
#             self.config(image=self.frames[0])
#         else:
#             self.next_frame()

#     def unload(self):
#         self.config(image="")
#         self.frames = None

#     def next_frame(self):
#         if self.frames:
#             self.loc += 1
#             self.loc %= len(self.frames)
#             self.config(image=self.frames[self.loc])
#             self.after(self.delay, self.next_frame)

# root = tk.Tk()
# lbl = ImageLabel(root)
# lbl.pack()
# lbl.load('/home/pi/python-projects/my-love.gif')
# root.mainloop()

