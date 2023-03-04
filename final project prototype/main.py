
import tkinter
import tkinter as tk
import analyze

    ## Program class and definitions
class SEOGUI:
    def __init__(self):

            # Creating the main window
        self.main_window = tkinter.Tk()
        self.main_window.title('Project: SEO Extractor')
        self.main_window.geometry('600x150')

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

            # Error messaging with blank label
        self.errr = tkinter.StringVar()
        self.errr_label = tkinter.Label(self.main_frame, textvariable = self.errr, foreground = 'red')
        self.errr_label.grid(column=1, row=2, padx=0, pady=5)

            # Program button widgets
        self.calc_button = tkinter.Button(self.main_frame, text = 'Extract Tags', command = self.extract_tag)
        self.calc_button.grid(column=1, row=3, padx=0, pady=5)
        self.quit_button = tkinter.Button(self.main_frame, text = 'Quit', command = self.main_window.destroy)
        self.quit_button.grid(column=2, row=3, padx=0, pady=5)

            # Packaging the frame
        self.main_frame.pack()

            # Keeping the GUI running
        tkinter.mainloop()

        # Extract URL Tags button
    def extract_tag(self):
        
            #Exception net start
        try:

                # Retrieving the data for storage
            url0 = str(self.url_entry.get())
            html = analyze.project(url0)
            html.runProject()
          
            # Exception error protocol feedback
        except Exception as err:
            self.errr.set(err)

            # If no exceptions are caught
        else:
            self.errr.set('Extract Successful')

    ## Declaring the SEOGUI class into being
extract_url = SEOGUI()


# Define a function to read the words from the file and display them in the text box
def read_file():
    # Open the file for reading
    with open('YourKeywords.txt', 'r') as file:
        # Read the file contents into a string
        file_contents = file.read()
        # Split the string into individual words
        words = file_contents.split()
        # Display the words in the text box
        text_box.delete('1.0', 'end') # Clear any previous contents
        for word in words:
            text_box.insert('end', word + '\n')

# Create the GUI window
window = tk.Tk()

# Create a text box for displaying the words from the file
text_box = tk.Text(window, height=10, width=30)
text_box.pack()

# Create a button for reading the words from the file
button = tk.Button(window, text='Read File', command=read_file)
button.pack()

# Start the GUI main loop
window.mainloop()