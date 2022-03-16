from time import strftime
import tkinter
import tkinter.messagebox


class ExerciseGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # configure the main window
        self.main_window.geometry("600x300")
        gui.configure(bg="green")

        self.first_frame = tkinter.Frame(self.main_window)
        self.second_frame = tkinter.Frame(self.main_window)
        self.third_frame = tkinter.Frame(self.main_window)
        self.fourth_frame = tkinter.Frame(self.main_window)
        self.fifth_frame = tkinter.Frame(self.main_window)

        self.first_frame.pack(side="top")
        self.second_frame.pack(side="top")
        self.third_frame.pack(side="top")
        self.fourth_frame.pack(side="top")
        self.fifth_frame.pack(side="bottom")

        self.prompt_label1 = tkinter.Label(
            self.first_frame, text="Enter the score for test 1: "
        )

        self.prompt_label2 = tkinter.Label(
            self.second_frame, text="Enter the score for test 2: "
        )

        self.prompt_label3 = tkinter.Label(
            self.third_frame, text="Enter the score for test 3: "
        )

        self.test_entry1 = tkinter.Entry(self.first_frame, width=20)
        self.test_entry2 = tkinter.Entry(self.second_frame, width=20)
        self.test_entry3 = tkinter.Entry(self.third_frame, width=20)

        self.prompt_label1.pack(side="left")
        self.test_entry1.pack(side="right")
        self.prompt_label2.pack(side="left")
        self.test_entry2.pack(side="right")
        self.prompt_label3.pack(side="left")
        self.test_entry3.pack(side="right")

        self.average_label = tkinter.Label(self.fourth_frame, text="Average: ")

        self.avg_var = tkinter.StringVar()

        self.avg_response_label = tkinter.Label(
            self.fourth_frame, textvariable=self.avg_var
        )
        self.average_label.pack(side="left")
        self.avg_response_label.pack(side="right")

        self.avgbutton = tkinter.Button(
            self.fifth_frame, text="Average", command=self.average
        )
        self.quit_button = tkinter.Button(
            self.fifth_frame, text="Quit", command=self.main_window.destroy
        )

        self.avgbutton.pack(side="left")
        self.quit_button.pack(side="right")

        tkinter.mainloop()

    def average(self):
        test1 = float(self.test_entry1.get())
        test2 = float(self.test_entry2.get())
        test3 = float(self.test_entry3.get())

        average = (test1 + test2 + test3) / 3

        self.avg_var.set(average)


average = ExerciseGUI()

print("moving on...")
