from tkinter import *


class ButtonGame:
    def __init__(self):
        self.root = Tk()
        self.root.title('Button game')
        self.root.geometry("200x100")

        self.get_button = Button(text="Button 1", command=self.create_button2)
        self.get_button.pack(pady=20)

    def create_button2(self):
        self.get_button.destroy()
        self.get_button = Button(text="Button 2", command=self.create_button3)
        self.get_button.pack(pady=20)

    def create_button3(self):
        self.get_button.destroy()
        self.get_button = Button(text="Button 3", command=self.root.destroy)
        self.get_button.pack(pady=20)

    def start_game(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = ButtonGame()
    app.start_game()
