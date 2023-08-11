from tkinter import *


class ButtonGame:

    def start_game(self):
        root = Tk()
        root.title('Dragon game')
        root.geometry("200x100")

        get_button = Button(text="Button 1", command=root.destroy)
        get_button.pack(pady=20)

        root.mainloop()

        root = Tk()
        root.title('Dragon game')
        root.geometry("200x100")

        get_button = Button(text="Button 2", command=root.destroy)
        get_button.pack(pady=20)

        root.mainloop()

        root = Tk()
        root.title('Dragon game')
        root.geometry("200x100")

        get_button = Button(text="Button 3", command=root.destroy)
        get_button.pack(pady=20)

        root.mainloop()


if __name__ == '__main__':
    app = ButtonGame()
    app.start_game()
