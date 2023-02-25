import tkinter as tk

# Define a function to read the words from the file and display them in the text box
def read_file():
    # Open the file for reading
    with open('test.txt', 'r') as file:
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