import tkinter as tk
import time
from PIL import ImageTk, Image

app = tk.Tk()
app.title('PopRock')
app.geometry("400x500")

img1 = Image.open('the_rock_2.jpg')
new_img1 = img1.resize((400, 500))
new_img1.save('new_the_rock_2.jpg')
bg1 = ImageTk.PhotoImage(new_img1)
canva = tk.Label(app, image = bg1)
canva.pack()

def Onclick():
    img2 = Image.open('the_rock_1.jpg')
    new_img2 = img2.resize((400, 500))
    new_img2.save('new_the_rock_1.jpg')
    bg2 = ImageTk.PhotoImage(img2)
    canva.configure(image = bg2)
    canva.image = bg2
    

b1 = tk.Button(app, text = 'POP!', command = Onclick)
b1.place(x = 40, y = 100)

app.mainloop()