import tkinter as tk
from tkinter import filedialog

# Define the function that generates the .py file
def generate_py():
    label = label_entry.get()
    smiles = smiles_entry.get()
    reactive = reactive_var.get()

    # Open a save dialog box for the user to choose where to save the .py file
    file_path = filedialog.asksaveasfilename(defaultextension=".py")

    # Write the .py file in the specified format with the input values from the GUI
    with open(file_path, "w") as f:
        f.write(f"""species(
    label='{label}',
    reactive={reactive},
    structure=SMILES("{smiles}"),
)\n""")

# Create the main window
root = tk.Tk()
root.title("Species Generator")

# Add a label and entry box for the label
label_label = tk.Label(root, text="Label:")
label_label.grid(row=0, column=0)
label_entry = tk.Entry(root)
label_entry.grid(row=0, column=1)

# Add a label and entry box for the SMILES structure
smiles_label = tk.Label(root, text="SMILES:")
smiles_label.grid(row=1, column=0)
smiles_entry = tk.Entry(root)
smiles_entry.grid(row=1, column=1)

# Add a checkbox for the reactive parameter
reactive_var = tk.BooleanVar()
reactive_check = tk.Checkbutton(root, text="Reactive", variable=reactive_var)
reactive_check.grid(row=2, column=0)

# Add a button to generate the .py file
generate_button = tk.Button(root, text="Generate", command=generate_py)
generate_button.grid(row=3, column=0)

# Start the main loop
root.mainloop()