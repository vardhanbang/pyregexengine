import customtkinter as ctk

def check():
    pass

ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("PyRegexEngine")
app.geometry("1280x720")
app.resizable(width=False, height=False)
app.grid_columnconfigure((0), weight = 1)

regexLabel = ctk.CTkLabel(app, 
    text="Enter Regex", 
    font = ctk.CTkFont('roboto', 25)
)
regexLabel.grid(row = 0,
    column = 0, 
    padx = 15, 
    pady = (15,0), 
    sticky = 'w'
)

regexField = ctk.CTkTextbox(app, 
    height=30,
    font = ctk.CTkFont('roboto', 22)
)
regexField.grid(row = 1, 
    column = 0,
    padx = 15, 
    pady = (15,0), 
    sticky = 'ew'
)

checkButton = ctk.CTkButton(app, 
    text = 'Check', 
    font = ctk.CTkFont('roboto', 25), 
    height = 30, 
    width = 100,
    command=check
)
checkButton.grid(row = 1, 
    column = 1, 
    padx = (0, 15), 
    pady = (15,0),
    sticky = 'ns'
)

frame = ctk.CTkFrame(app, height = 500)
frame.grid(row = 2,
    padx = 15,
    pady = 15,
    column = 0,
    sticky = 'nsew',
    columnspan = 2,
    rowspan = 2
)

frame.grid_columnconfigure((0,1), weight=1)

inputLabel = ctk.CTkLabel(frame, 
    text="Enter Text", 
    font = ctk.CTkFont('roboto', 25)
)
inputLabel.grid(row = 0,
    column = 0, 
    padx = 15, 
    pady = (15,0), 
    sticky = 'w'
)

outputLabel = ctk.CTkLabel(frame, 
    text="Matched subtrings", 
    font = ctk.CTkFont('roboto', 25)
)
outputLabel.grid(row = 0,
    column = 1, 
    padx = 15, 
    pady = (15,0), 
    sticky = 'w'
)

inputField = ctk.CTkTextbox(frame,
    font = ctk.CTkFont('roboto', 22),
    height = 500
)
inputField.grid(row = 1, 
    column = 0,
    padx = 15, 
    pady = 15, 
    sticky = 'nsew',
)

outputVar = ctk.StringVar()

output = ctk.CTkLabel(frame, 
    text=outputVar.get(), 
    font = ctk.CTkFont('roboto', 25)
)
output.grid(row = 1,
    column = 1, 
    padx = 15, 
    pady = (15,0), 
    sticky = 'nw',
)





app.mainloop()