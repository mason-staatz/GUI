from time import strftime
import tkinter
import tkinter.messagebox


class PizzaGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # configure the main window
        self.main_window.geometry("600x300")

        self.first_frame = tkinter.Frame(self.main_window)
        self.second_frame = tkinter.Frame(self.main_window)
        self.third_frame = tkinter.Frame(self.main_window)
        self.fourth_frame = tkinter.Frame(self.main_window)

        self.first_frame.pack(side="top")
        self.second_frame.pack(side="left")
        self.third_frame.pack(side="right")
        self.fourth_frame.pack(side="bottom")

        # 1st frame-- customer name-- input box

        self.prompt_label1 = tkinter.Label(self.first_frame, text="Enter your name: ")

        self.name_entry = tkinter.Entry(self.first_frame, width=20)

        self.prompt_label1.pack(side="left")
        self.name_entry.pack(side="right")

        # 2nd frame-- crust choice -- radio buttons

        self.radio_var = tkinter.IntVar()

        self.rb1 = tkinter.Radiobutton(
            self.second_frame, text="Thin Crust", variable=self.radio_var, value=1.00
        )
        self.rb2 = tkinter.Radiobutton(
            self.second_frame, text="Thick Crust", variable=self.radio_var, value=2.00
        )
        self.rb3 = tkinter.Radiobutton(
            self.second_frame, text="Stuffed Crust", variable=self.radio_var, value=3.00
        )

        self.rb1.select()

        self.rb1.pack(side="left")
        self.rb2.pack(side="left")
        self.rb3.pack(side="left")

        # 3rd frame-- Topping choices-- checkboxes

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)

        self.cb1 = tkinter.Checkbutton(
            self.third_frame, text="Pepperoni: $1.00", variable=self.cb_var1
        )
        self.cb2 = tkinter.Checkbutton(
            self.third_frame, text="Sausage: $1.50", variable=self.cb_var2
        )
        self.cb3 = tkinter.Checkbutton(
            self.third_frame, text="Extra Cheese: $0.50", variable=self.cb_var3
        )
        self.cb4 = tkinter.Checkbutton(
            self.third_frame, text="Loads of Bacon: $2.50", variable=self.cb_var3
        )
        self.cb5 = tkinter.Checkbutton(
            self.third_frame, text="Spinach: $0.75", variable=self.cb_var3
        )

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()

        # 4th frame-- cost calc and quit-- buttons

        self.costbutton = tkinter.Button(
            self.fourth_frame, text="Calculate Cost", command=self.calc_cost
        )
        self.quit_button = tkinter.Button(
            self.fourth_frame, text="Quit", command=self.main_window.destroy
        )

        self.costbutton.pack(side="left")
        self.quit_button.pack(side="right")

        tkinter.mainloop()

    def calc_cost(self):
        tcost = topping_cost + crust_cost
        self.message = (
            "Customer Name: ",
            self.name_entry,
            "\n",
            "Total Cost: ",
            tcost,
        )

        if self.cb_var1.get() == 1:
            topping_cost += 1.00
        if self.cb_var2.get() == 1:
            topping_cost += 1.50
        if self.cb_var3.get() == 1:
            topping_cost += 0.50
        if self.cb_var4.get() == 1:
            topping_cost += 2.50
        if self.cb_var5.get() == 1:
            topping_cost += 0.75

        if self.rb1.get() == 1:
            crust_cost = 1.00
        if self.rb2.get() == 1:
            crust_cost = 2.00
        if self.rb3.get() == 1:
            crust_cost = 3.00

        tkinter.messagebox.showinfo("Order Confirmation", self.message)


my_gui = PizzaGUI()

print("moving on...")
