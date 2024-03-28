import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window=tk.Tk()
window.title("Costum Widgets")

label1=tk.Label(
    window,
    text="Name",
    foreground="white", 
    background="purple",
    width=10,
    height=1
)
label1.pack()

entry1=tk.Entry(window)
entry1.pack()

label2=tk.Label(
    window,
    text="Address Line 1",
    foreground="white", 
    background="blue",
    width=10,
    height=1
)
label2.pack()

entry2=tk.Entry(window)
entry2.pack()

label3=tk.Label(
    window,
    text="Address Line 2",
    foreground="white", 
    background="purple",
    width=10,
    height=1
)
label3.pack()

entry3=tk.Entry(window)
entry3.pack()

label4=tk.Label(
    window,
    text="City",
    foreground="white", 
    background="blue",
    width=10,
    height=1
)
label4.pack()

entry4=tk.Entry(window)
entry4.pack()

label5=tk.Label(
    window,
    text="State",
    foreground="white", 
    background="purple",
    width=10,
    height=1
)
label5.pack()

entry5=tk.Entry(window)
entry5.pack()

label6=tk.Label(
    window,
    text="Zipcode",
    foreground="white", 
    background="blue",
    width=10,
    height=1
)
label6.pack()

entry6=tk.Entry(window)
entry6.pack()

label7=tk.Label(
    window,
    text="Phone Number",
    foreground="white", 
    background="purple",
    width=10,
    height=1
)
label7.pack()

entry7=tk.Entry(window)
entry7.pack()

label8=tk.Label(
    window,
    text="Email Address",
    foreground="white", 
    background="blue",
    width=10,
    height=1
)
label8.pack()

entry8=tk.Entry(window)
entry8.pack()

button1 = tk.Button(
    window, 
    text="Submit",
    width=12,
    height=2
)
button1.pack()

window.mainloop()