### Group 5 - Caleb Rivich, John Wolfe, Kacie Jordan, Zander Cross
### March 4, 2023
### SEO Tag Extractor Prototype

import tkinter
import analyze

    ## Program class and definitions
class SEOGUI:
    def __init__(self):

            # Creating the main window
        self.main_window = tkinter.Tk()
        self.main_window.title('Project: SEO Extractor')
        self.main_window.geometry('700x375')

            # Creating main frame
        self.main_frame = tkinter.Frame(self.main_window)

            # Configuring the grid columns
        self.main_frame.columnconfigure(0, weight=2)
        self.main_frame.columnconfigure(1, weight=2)

            # Program instruction tag

        self.program_label = tkinter.Label(self.main_frame, text = 'Insert HTML')
        self.program_label.grid(column=1, row=0, sticky=tkinter.W, padx=0, pady=5)

            # URL Entry Widgets
        self.url_label = tkinter.Label(self.main_frame, text = 'HTML: ')
        self.url_label.grid(column=0, row=1, sticky=tkinter.E, padx=0, pady=5)
        self.url_entry = tkinter.Entry(self.main_frame, width = 75)
        self.url_entry.grid(column=1, row=1, sticky=tkinter.W, padx=0, pady=5)
        self.url_entry.insert(0, '')
        self.text_box = tkinter.Text(self.main_frame, height=10, width=75)
        self.text_box.grid(column=1, row=2, sticky=tkinter.W, padx=0, pady=5)

            # Error messaging with blank label
        self.errr = tkinter.StringVar()
        self.errr_label = tkinter.Label(self.main_frame, textvariable = self.errr, foreground = 'red')
        self.errr_label.grid(column=1, row=3, padx=0, pady=5)
        self.yaay = tkinter.StringVar()
        self.yaay_label = tkinter.Label(self.main_frame, textvariable = self.yaay, foreground = 'green')
        self.yaay_label.grid(column=1, row=3, padx=0, pady=5)

            # Program button widgets
        self.calc_button = tkinter.Button(self.main_frame, text = 'Extract Tags', command = self.extract_tag)
        self.calc_button.grid(column=1, row=4, padx=0, pady=5)
        self.read_button = tkinter.Button(self.main_frame, text = 'Read Tags', command = self.reading_time)
        self.read_button.grid(column=1, row=5, padx=0, pady=5)
        self.quit_button = tkinter.Button(self.main_frame, text = 'Quit', command = self.main_window.destroy)
        self.quit_button.grid(column=1, row=6, padx=0, pady=5)

            # Packaging the frame
        self.main_frame.pack()

            # Keeping the GUI running
        tkinter.mainloop()

        # Extract URL Tags button
    def extract_tag(self):
        
            # Exception net start
        try:

                # Retrieving the data for storage
            url0 = str(self.url_entry.get())
            html = analyze.project(url0)
            html.runProject()
            self.text_box.delete('1.0', 'end')
          
            # Exception error protocol feedback
        except Exception as err:
            self.errr.set(err)
            self.yaay.set('')
            self.text_box.delete('1.0', 'end')

            # If no exceptions are caught
        else:
            self.yaay.set('Extract Successful')
            self.errr.set('')

        # Define a function to read the words from the file and display them in the text box
    def reading_time(self):

            # Exception net start
        try:

                # Open the file for reading
            with open('YourKeywords.txt', 'r') as file:

                    # Read the file contents into a string
                    # Split the string into individual words
                file_contents = file.read()
                words = file_contents.split()

                    # Clear any previous contents
                    # Display the words in the text box
                self.text_box.delete('1.0', 'end')
                for word in words:
                    self.text_box.insert('end', word + '\n')

            # Exception error protocol feedback
        except Exception as err:
            self.errr.set(err)
            self.yaay.set('')

            # If no exceptions are caught
        else:
            self.yaay.set('Reading Successful')
            self.errr.set('')

    ## Declaring the SEOGUI class into being
extract_url = SEOGUI()
