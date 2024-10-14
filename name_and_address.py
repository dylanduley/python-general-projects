import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Information Display")

        # StringVars to hold the displayed values.
        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.csz_value = tkinter.StringVar()

        # Create frames.
        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack labels with the correct text variable bindings.
        self.name_label = tkinter.Label(self.info_frame, textvariable=self.name_value)
        self.street_label = tkinter.Label(self.info_frame, textvariable=self.street_value)
        self.csz_label = tkinter.Label(self.info_frame, textvariable=self.csz_value)

        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()

        # Create buttons.
        self.show_info_button = tkinter.Button(
            self.button_frame,
            text='Show Info',
            command=self.show
        )
        self.quit_button = tkinter.Button(
            self.button_frame,
            text='Quit',
            command=self.main_window.destroy
        )

        # Pack buttons with proper alignment.
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        # Pack frames.
        self.info_frame.pack(padx=10, pady=10)
        self.button_frame.pack(padx=10, pady=10)

        # Start the Tkinter main loop.
        tkinter.mainloop()

    # Define the show method to update the StringVar values.
    def show(self):
        self.name_value.set('Matt Hoyle')
        self.street_value.set('123 Walnut Street')
        self.csz_value.set('Asheville, NC 29999')

# Create an instance of MyGUI.
my_gui = MyGUI()
