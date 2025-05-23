# import the modulees
import tkinter as tk 

class Whiteboard(tk.Tk):
    def __init__(self):
        super().__init__() 

        self.title('whiteboard')
        self.geometry('800x600')

        # create the canvas 
        self.canvas = tk.Canvas(self, bg='white',width=800,height=500)
        self.canvas.pack(pady=10)

        self.clear_btn = tk.Button(self, text="Clear" , command=self.clear_canvas)
        self.clear_btn.pack()

        self.canvas.bind('<B1-Motion>',self.draw)

    def draw(self,event):
        x , y = event.x , event.y
        # self.canvas.create_oval(x, y , x+3 , y+3, fill='black',outline='black')
        self.canvas.create_line(x,y , x+3, y+3, fill='black', width=2)

    def clear_canvas(self):
        self.canvas.delete("all")
if __name__ == "__main__":
    Whiteboard().mainloop()

