from tkinter import *


class CheeseGame:
    def __init__(self):
        self.get_button_nei = None
        self.get_button_ja = None
        self.cheese_list = None
        self.cheese = None
        self.root = Tk()
        self.root.title('Cheese game')
        self.root.geometry("300x150")

        self.label = Label(text='Ask Herr Mouse if it is cheese:')
        self.entry = Entry()
        self.label.pack()
        self.entry.pack()

        self.get_button = Button(text="Ask!", command=self.mouse_answer)
        self.get_button.pack(pady=20)

    def mouse_answer(self):
        self.cheese_list = ['cheddar', 'mozzarella', 'gorgonzola', 'tilsiter',
                            'emmental', 'maasdam', 'parmesan', 'jarlsberg', 'norwegian']
        self.cheese = self.entry.get()
        self.get_button.destroy()
        self.label.destroy()
        self.entry.destroy()

        if self.cheese in self.cheese_list:
            self.label = Label(text=f'Herr Mouse approves your knowledge! \n Do you want one more attempt?')
            self.label.grid(row=0, sticky='ne')
        else:
            self.label = Label(text=f'Herr Mouse is sad, \n Learn better! \n Do you want one more attempt?')
            self.label.grid(row=0, sticky='ne')

        self.get_button_ja = Button(text="Ja", command=self.continue_game)
        self.get_button_ja.grid(row=1, sticky='w')

        self.get_button_nei = Button(text="Nei", command=self.root.destroy)
        self.get_button_nei.grid(row=1, sticky='e')

    def continue_game(self):
        self.get_button_nei.destroy()
        self.get_button_ja.destroy()
        self.label.destroy()

        self.label = Label(text='Ask Herr Mouse if it is cheese:')
        self.entry = Entry()
        self.label.pack()
        self.entry.pack()

        self.get_button = Button(text="Ask!", command=self.mouse_answer)
        self.get_button.pack(pady=20)

    def start_game(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = CheeseGame()
    app.start_game()
