import tkinter as tk

root = tk.Tk()
root.geometry("700x500")
root.config(background="#DACCE8")


class Morpion:
    def __init__(self):
        self.case_button_1 = tk.Button(root, text="|-|", font=("Arial", 30))
        self.case_button_2 = tk.Button(root, text="|-|", font=("Arial", 30))
        self.case_button_3 = tk.Button(root, text="|-|", font=("Arial", 30))
        self.case_button_4 = tk.Button(root, text="|-|", font=("Arial", 30))
        self.case_button_5 = tk.Button(root, text="|-|", font=("Arial", 30))
        self.case_button_6 = tk.Button(root, text="|-|", font=("Arial", 30))
        self.case_button_7 = tk.Button(root, text="|-|", font=("Arial", 30))
        self.case_button_8 = tk.Button(root, text="|-|", font=("Arial", 30))
        self.case_button_9 = tk.Button(root, text="|-|", font=("Arial", 30))
        self.list_button = [self.case_button_1, self.case_button_2, self.case_button_3, self.case_button_4,
        self.case_button_5, self.case_button_6, self.case_button_7, self.case_button_8, self.case_button_9]
        self.button_index = 0
        

    def place_button_l1(self):
        self.x = 250
        self.y = 150
        for l1 in range(0, 3):
            self.list_button[l1].place(x=self.x, y=self.y)
            self.x += 70

    def place_button_l2(self):
        self.x = 250
        self.y = 230
        for l2 in range(3, 6):
            self.list_button[l2].place(x=self.x, y=self.y)
            self.x += 70

    def place_button_l3(self):
        self.x=250
        self.y = 310
        for l3 in range(6, 9):
            self.list_button[l3].place(x=self.x, y=self.y)
            self.x += 70


                



    


morpion = Morpion()
morpion.place_button_l1()
morpion.place_button_l2()
morpion.place_button_l3()


root.mainloop()

