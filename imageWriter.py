from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageFont

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Watermark")
        
        # Adding Components
        enterImageText = Label(root, text="Enter image", font=("Segoe UI", 12))
        self.enterImageEntry = Entry(root, width=50)
        submitButton1 = Button(root, text="Browse", command=lambda:self.openFile(self.enterImageEntry), font=("Segoe UI", 10))
                
        enterWatermarkText = Label(root, text="Enter watermark image", font=("Segoe UI", 12))
        self.enterWatermarkEntry = Entry(root, width=50)
        submitButton2 = Button(root, text="Browse", command=lambda:self.openFile(self.enterWatermarkEntry), font=("Segoe UI", 10))
        
        enterExtraText = Label(root, text="Enter extra text", font=("Segoe UI", 12))
        self.extraTextEntry = Entry(root, width=60)

        watermarkButton = Button(root, text="Watermark", command=self.processWatermark, font=("Segoe UI", 12))


        # Setting up grid
        enterImageText.grid(row=0, sticky=W, padx=10, pady=(10,0))
        self.enterImageEntry.grid(row=1, column=0, padx=15)
        submitButton1.grid(row=1, column=1)
        
        enterWatermarkText.grid(row=2, sticky=W, padx=10, pady=(10,0))
        self.enterWatermarkEntry.grid(row=3, column=0)
        submitButton2.grid(row=3, column=1)

        enterExtraText.grid(row=4, sticky=W, padx= 10, pady=(10,0))
        self.extraTextEntry.grid(row=5, columnspan=2, padx=(10,0))

        watermarkButton.grid(columnspan=2,pady=10)

    # Gets file path and sets the corresponding entry widget's value to the file path
    def openFile(self, target):
        self.filename = askopenfilename()
        target.delete(0,END)
        target.insert(0,self.filename)
        return

    # Places watermark on image 
    # Not handled yet!
    def processWatermark(self):
        # print("Here: ", 
        # self.enterImageEntry.get(),
        # self.enterWatermarkEntry.get(),
        # self.extraTextEntry.get())
        
        # Pass the image paths to their handlers
        image = Image.open(self.enterImageEntry.get())
        marker = Image.open(self.enterWatermarkEntry.get())
        markerX, markerY = marker.size
        
        # TO-DO
        # Fix picMark and textMark (combine them??)
        # Output to a file

    def picMark(pic):
        picX, picY = pic.size
        pic.paste(marker,(picX - markerX ,picY - markerY))
        
        return pic

    def textMark(pic):
        picX, picY = pic.size
        draw =ImageDraw.Draw(pic)
        font = ImageFont.truetype("CuteFont-Regular.ttf", size=40)
        location = (picX // 2, picY // 2)
        text = "Dan Carr\nPhotography"
        draw.text((location), text, fill = "blue", font = font)

        return pic

# textMark(image).show()
root = Tk()
root.geometry("400x300")
root.resizable(False, False)
app = Window(root)
root.mainloop()
