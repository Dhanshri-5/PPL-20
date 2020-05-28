from tkinter import *
from tkinter import ttk, colorchooser
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.messagebox import *
from PIL import ImageTk, Image
import PIL.Image
filename =name= 'demo'
class main :
    DEFAULT_BRUSH_SIZE = 5.0
    DEFAULT_COLOR = 'black'	 
    
    def __init__(self ,root):
        self.root = root
        root.geometry("1200x680")
        self.fg = 'black'
        self.bg = 'white'
        self.eColor = 'white'
        self.xp = None
        self.yp = None
        self.width = 5
        self.setup()

        #Binding the events to the canvas widget

        self.canvas.bind('<B1-Motion>',self.paint)
        self.canvas.bind('<ButtonRelease-1>',self.reset)
        self.root.config(cursor = 'cross')

    #Paint method to draw on user input
    def paint(self,pos):
        if self.xp and self.yp:
            self.canvas.create_line(self.xp,self.yp,pos.x,pos.y,width = self.width, fill = self.fg , capstyle = ROUND ,smooth = True)
        self.xp = pos.x
        self.yp = pos.y
    
    #Sets the cursor to inital state
    def reset(self , e):
        self.xp = None
        self.yp = None

    #Choose eraser
    def eraser(self):
        self.root.config(cursor = 'dot')
        self.fg = self.bg
        self.eColor = self.bg

    #Choose brush
    def brushCursor(self):
        self.root.config(cursor = 'cross')
        
    #Choose brush size by hotkey detection
    def brushSize(self):
        self.width = self.scale.get()
    
    #Setting the Brush color
    def BrushColor(self):
        color = colorchooser.askcolor()
        self.fg = (str(color)[-9:-2])

    #Fill tool 
    def fillbg(self):
        color = colorchooser.askcolor()
        self.bg = (str(color)[-9:-2])
        self.eColor = self.bg
        self.canvas.config(background = self.bg)
    #Clears the content of the screen
    def clear(self):
        self.canvas.config(background = self.bg)
        self.canvas.delete(ALL)
    
    #Utility function for palette
    def setfg(self,color):
        self.fg = color
        self.eColor = self.bg
        
   
    #Save function
    def write(self,canvas,fileName):
        canvas.postscript(file = fileName + '.eps') 
        img = PIL.Image.open(fileName + '.eps') 
        img.save(fileName + '.png', 'png') 
         
        
    def save(self):
        filename = asksaveasfilename(title="Save Pictures As...")
        self.write(self.canvas,filename)
    
    def open(self):
        name = askopenfilename()
        my_img = ImageTk.PhotoImage(Image.open(name))
        
    def setup(self):
        #Define a Menu
        mymenu = Menu(root)
        root.config(menu=mymenu)
  
        self.toolBar = Frame(root, padx=5, pady=5,height = 500,width = 80)
        self.toolBar.pack(side=LEFT, fill=BOTH)

        self.canvas = Canvas(root,width =1600, height = 900, bg = self.bg )
        self.canvas.pack()

        #Create Menu Items
        fileMenu = Menu(mymenu)
        mymenu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="New", command=self.clear)
        fileMenu.add_command(label="SaveAs", command=self.save)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=root.quit)

        editmenu = Menu(mymenu)
        mymenu.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Brush Color", command=self.BrushColor)
        editmenu.add_command(label="Backgrouond Color", command=self.fillbg)
        #editmenu.add_command(label="Paste", command=fake_command)

        toolsmenu = Menu(mymenu)
        mymenu.add_cascade(label="Tools", menu=toolsmenu)
        toolsmenu.add_command(label="Eraser", command=self.eraser)
        toolsmenu.add_command(label="Clear", command=self.clear)
        #toolsmenu.add_command(label="--", command=fake_command)

        openmenu = Menu(mymenu)
        mymenu.add_cascade(label="Insert", menu=openmenu)
        openmenu.add_command(label="Image", command=self.open)
        #openmenu.add_command(label="Background", command=fake_command)
        #openmenu.add_command(label="--", command=fake_command)
        
        colorLabel = Label(self.toolBar,text= "Colors")
        colorLabel.grid(row = 0 ,column = 0 , columnspan = 3)
        colorBtn = Button(self.toolBar,text = " " ,background = 'pink' , height = 1,width = 2,command = lambda :self.setfg('pink'))
        colorBtn.grid(row = 1,column = 0)       
        colorBtn = Button(self.toolBar,text = " " ,background = 'red4' , height = 1,width = 2,command = lambda :self.setfg('red4'))
        colorBtn.grid(row = 1,column = 1)
        colorBtn = Button(self.toolBar,text = " " ,background = 'red', height = 1,width = 2,command =lambda : self.setfg('red'))
        colorBtn.grid(row = 1,column = 2)
        colorBtn = Button(self.toolBar,text = " " ,background = 'yellow', height = 1,width = 2,command =lambda : self.setfg('yellow'))
        colorBtn.grid(row = 2,column = 0)
        colorBtn = Button(self.toolBar,text = " " ,background = 'gold2', height = 1,width = 2,command =lambda : self.setfg('gold2'))
        colorBtn.grid(row = 2,column = 1)
        colorBtn = Button(self.toolBar,text = " " ,background = 'orange', height = 1,width = 2,command =lambda : self.setfg('orange'))
        colorBtn.grid(row = 2,column = 2)
        colorBtn = Button(self.toolBar,text = " " ,background = 'violet' , height = 1,width = 2,command =lambda : self.setfg('violet'))
        colorBtn.grid(row = 3,column = 0)
        colorBtn = Button(self.toolBar,text = " " ,background = 'blue' , height = 1,width = 2,command =lambda : self.setfg('blue'))
        colorBtn.grid(row = 3,column = 1)
        colorBtn = Button(self.toolBar,text = " " ,background = 'grey', height = 1,width = 2,command =lambda : self.setfg('grey'))
        colorBtn.grid(row = 3,column = 2)
        colorBtn = Button(self.toolBar,text = " " ,background = 'lime green', height = 1,width = 2,command =lambda : self.setfg('lime green'))
        colorBtn.grid(row = 4,column = 0)
        colorBtn = Button(self.toolBar,text = " " ,background = 'green', height = 1,width = 2,command = lambda : self.setfg('green'))
        colorBtn.grid(row = 4,column = 1)
        colorBtn = Button(self.toolBar,text = " " ,background = 'black', height = 1,width = 2,command =lambda : self.setfg('black'))
        colorBtn.grid(row = 4,column = 2)
         
        #Buttons
        brush = Button(self.toolBar,text = 'Brush',command = self.brushCursor ,  height = 2, pady = 2)
        brush.grid(row = 5 ,column = 0 ,columnspan = 3 ,sticky = W+E )

        btnClear = Button(self.toolBar,text = 'Clear',command = self.clear ,height = 2, pady = 2)
        btnClear.grid(row = 6 ,column = 0 ,columnspan = 3 ,sticky = W+E)

        btneraser = Button(self.toolBar,text = 'Eraser',command = self.eraser,height = 2, pady = 2)
        btneraser.grid(row = 7 ,column = 0 ,columnspan = 3 ,sticky = W+E)

        btncolor = Button(self.toolBar, text = "Brush Color" ,command=self.BrushColor,height = 2, pady = 2)
        btncolor.grid(row = 9 ,column = 0 ,columnspan = 3 ,sticky = W+E)

        btnfill = Button(self.toolBar, text = "Fill BG", command=self.fillbg,height = 2, pady = 2)
        btnfill.grid(row = 10 ,column = 0 ,columnspan = 3 ,sticky = W+E)

        btnExit = Button(self.toolBar,text = 'Exit',command = root.destroy,height = 2, pady = 2)
        btnExit.grid(row = 11 ,column = 0 ,columnspan = 3 ,sticky = W+E)
                 
        btnSetSize = Button(self.toolBar,text = 'Set Size',command = self.brushSize,height = 2, pady = 2)
        btnSetSize.grid(row = 13 ,column = 0 ,columnspan = 3 ,sticky = W+E)

        #slider
        self.scale = Scale(self.toolBar ,from_ = 50, to = 5, orient = VERTICAL)
        self.scale.grid(row = 12 ,column = 0 ,columnspan = 3 ,sticky = W+E)



#Main program to run the application
if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Paint   -by Dhanshri')
    root.mainloop()
