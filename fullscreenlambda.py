import tkinter as tk


class Fullscreen_Example:
    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)  
        self.window.bind("<F11>",
                         lambda event: self.window.attributes("-fullscreen",
                                    not self.window.attributes("-fullscreen")))
        self.window.bind("<Escape>",
                         lambda event: self.window.attributes("-fullscreen",
                                    False))

        self.window.mainloop()

if __name__ == '__main__':
    app = Fullscreen_Example()    
