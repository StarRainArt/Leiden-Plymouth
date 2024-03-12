import tkinter as tk

# Function to handle option selection
def select_option(option):
    if option in selected_options:
        selected_options.remove(option)
        print(f"Deselected {option}")
    else:
        selected_options.add(option)
        print(f"Selected {option}")
    update_display()

# Function to update the GUI display
def update_display():
    if selected_options:
        display_label.config(text="Selected options: " + ", ".join(selected_options))
    else:
        display_label.config(text="Selected options: None")

# Function to save bio
def save_bio():
    global bio_saved
    bio_saved = bio_entry.get()
    bio_textbox.config(state=tk.NORMAL)
    bio_textbox.delete("1.0", tk.END)
    bio_textbox.insert(tk.END, bio_saved)
    bio_textbox.config(state=tk.DISABLED)
    save_button.pack_forget()
    edit_button.pack(side=tk.LEFT)
    bio_entry.pack_forget()

# Function to edit bio
def edit_bio():
    bio_textbox.config(state=tk.NORMAL)
    bio_entry.delete(0, tk.END)
    bio_entry.insert(tk.END, bio_saved)
    bio_entry.pack()
    save_button.pack(side=tk.LEFT)
    edit_button.pack_forget()
    bio_textbox.delete("1.0", tk.END)

# Initialize selected options set
selected_options = set()

# Create main window
root = tk.Tk()
root.title("Options Selection")

# Create labels for each option
options = ['Adventure', 'Fitness', 'Technology', 'Travel', 'Art', 'Cuisine', 'Music', 'Entrepreneurship']
option_labels = []
for option in options:
    label = tk.Label(root, text=option, padx=10, pady=5, relief=tk.RAISED)
    label.bind("<Button-1>", lambda event, opt=option: select_option(opt))
    label.pack()
    option_labels.append(label)

# Create label to display selected options
display_label = tk.Label(root, text="Selected options: None", padx=10, pady=5)
display_label.pack()

# Bio entry field
bio_entry_label = tk.Label(root, text="Bio:")
bio_entry_label.pack()
bio_entry = tk.Entry(root, width=40)
bio_entry.pack()

# Text box to display/save bio
bio_textbox_label = tk.Label(root, text="Saved Bio:")
bio_textbox_label.pack()
bio_textbox = tk.Text(root, width=40, height=4, state=tk.DISABLED)
bio_textbox.pack()

# Save and Edit buttons
save_button = tk.Button(root, text="Save", command=save_bio)
save_button.pack(side=tk.LEFT)
edit_button = tk.Button(root, text="Edit", command=edit_bio)
edit_button.pack(side=tk.LEFT)

# Run the GUI
root.mainloop()
