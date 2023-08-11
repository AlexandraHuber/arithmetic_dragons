from tkinter import *


class ButtonGame:
    def __init__(self):
        self.root = Tk()
        self.root.title('Button game')
        self.root.geometry("200x100")

        self.get_button = Button(text="Button 1", command=self.root.destroy)
        self.get_button.pack(pady=20)

    def start_game(self):
        self.root.mainloop()

        root = Tk()
        root.title('Button game')
        root.geometry("200x100")

        get_button = Button(text="Button 2", command=root.destroy)
        get_button.pack(pady=20)

        root.mainloop()

        root = Tk()
        root.title('Button game')
        root.geometry("200x100")

        get_button = Button(text="Button 3", command=root.destroy)
        get_button.pack(pady=20)

        root.mainloop()


if __name__ == '__main__':
    app = ButtonGame()
    app.start_game()
