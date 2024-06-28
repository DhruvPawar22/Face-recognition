import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {

    'databaseURL': "https://face-authentication-real-time-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

def save_to_firebase():
    # Get a reference to the database
    ref = db.reference('Students')

    # Get user input
    student_id = id_entry.get()
    name = name_entry.get()
    major = major_entry.get()
    starting_year = int(starting_year_entry.get())
    standing = standing_entry.get()
    year = int(year_entry.get())
    last_attendance_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a dictionary with the user input data
    data = {
        "name": name,
        "Major": major,
        "starting_year": starting_year,
        "total_attendance": 0,  # Set default attendance to 0
        "Standing": standing,
        "year": year,
        "last_attendance_time": last_attendance_time
    }

    # Push the data to Firebase under the specified student ID
    ref.child(student_id).set(data)

    messagebox.showinfo("Success", "Data saved to Firebase!")

# Create the GUI window
root = tk.Tk()
root.title("Student Data Entry")

# Create and pack input fields
tk.Label(root, text="ID:").grid(row=0, column=0, sticky="e")
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

tk.Label(root, text="Name:").grid(row=1, column=0, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

tk.Label(root, text="Major:").grid(row=2, column=0, sticky="e")
major_entry = tk.Entry(root)
major_entry.grid(row=2, column=1)

tk.Label(root, text="Starting Year:").grid(row=3, column=0, sticky="e")
starting_year_entry = tk.Entry(root)
starting_year_entry.grid(row=3, column=1)

tk.Label(root, text="Standing:").grid(row=4, column=0, sticky="e")
standing_entry = tk.Entry(root)
standing_entry.grid(row=4, column=1)

tk.Label(root, text="Year:").grid(row=5, column=0, sticky="e")
year_entry = tk.Entry(root)
year_entry.grid(row=5, column=1)

# Create and pack save button
save_button = tk.Button(root, text="Save", command=save_to_firebase)
save_button.grid(row=6, column=0, columnspan=2)

# Run the GUI
root.mainloop()



