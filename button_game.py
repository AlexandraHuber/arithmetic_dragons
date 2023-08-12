from tkinter import *


class ButtonGame:
    def __init__(self, counter):
        self.get_button_nei = None
        self.get_button_ja = None
        self.name = None
        self.counter = counter
        self.root = Tk()
        self.root.title('Button game')
        self.root.geometry("300x150")

        self.label = Label(text='What is your name?')
        self.entry = Entry()
        self.label.pack()
        self.entry.pack()

        self.get_button = Button(text="Button 1", command=self.create_button2)
        self.get_button.pack(pady=20)

    def create_button2(self):
        self.name = self.entry.get()
        self.get_button.destroy()
        self.label.destroy()
        self.entry.destroy()

        self.label = Label(text=f'Hi {self.name}, do you want to continue? Attempt: 1')
        self.label.grid(row=0, sticky='ne')

        self.get_button_ja = Button(text="Ja", command=self.continue_game)
        self.get_button_ja.grid(row=1, sticky='w')

        self.get_button_nei = Button(text="Nei", command=self.create_button3)
        self.get_button_nei.grid(row=1, sticky='e')

    def continue_game(self):
        self.get_button_nei.destroy()
        self.get_button_ja.destroy()
        self.label.destroy()

        self.label = Label(text=f'Hi {self.name}, do you want to continue? Attempt: {self.counter}')
        self.label.grid(row=0, sticky='ne')

        self.get_button_ja = Button(text="Ja", command=self.clicked)
        self.get_button_ja.grid(row=1, sticky='w')

        self.get_button_nei = Button(text="Nei", command=self.create_button3)
        self.get_button_nei.grid(row=1, sticky='e')

    def clicked(self):
        self.counter += 1
        self.label.config(text=f'Hi {self.name}, do you want to continue? Attempt: {self.counter}')

    def create_button3(self):
        self.get_button_nei.destroy()
        self.get_button_ja.destroy()
        self.label.destroy()

        self.label = Label(text='Good bye!')
        self.label.pack()

        self.get_button = Button(text="Bye!", command=self.root.destroy)
        self.get_button.pack(pady=20)

    def start_game(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = ButtonGame(2)
    app.start_game()
