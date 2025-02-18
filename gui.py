import customtkinter as ctk
from regex import regex
#test2
def check():
    for child in outputFrame.winfo_children():
        child.destroy()

    expression = regexField.get("1.0", "end-1c")
    if not expression:
        return
    
    input_strings = inputField.get("1.0", "end-1c").split('\n')

    outputs = []
    for inp in input_strings:
        for i,j in regex(expression, inp):
            outputs.append(inp[i:j])
    for i, output in enumerate(outputs):
        temp = ctk.CTkLabel(outputFrame,
            font = ctk.CTkFont('roboto', 22),
            justify = 'left',
            text = output
        )
        temp.grid(row = i,
            padx = 15,
            sticky = 'w'
        )
    app.update_idletasks()
    print(input_strings)
    print(expression)

def limit_to_one_line(event):
    content = regexField.get("1.0", "end-1c")
    if "\n" in content:
        regexField.delete("1.0", "end")
        regexField.insert("1.0", content.replace("\n", ""))

def handle_event(event):
    check()

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
regexField.bind('<KeyRelease>', limit_to_one_line)
regexField.bind("<Return>", handle_event)

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
    text="Matched substrings", 
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

outputFrame = ctk.CTkScrollableFrame(frame)
outputFrame.grid(row = 1,
    column = 1,
    padx = 0,
    pady = 15,
    sticky = 'nsew'
)

app.mainloop()
