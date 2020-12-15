import tkinter as tk

class Ubuntu_Fullscreen_Example:
    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-zoomed', True)  
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-zoomed", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-zoomed", self.fullScreenState)

if __name__ == '__main__':
    app = Ubuntu_Fullscreen_Example()  
