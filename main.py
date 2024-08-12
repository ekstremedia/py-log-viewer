import customtkinter
import os

GEOMETRY_FILE = "window_geometry.txt"

def save_geometry():
    with open(GEOMETRY_FILE, "w") as f:
        f.write(app.geometry())

def load_geometry():
    if os.path.exists(GEOMETRY_FILE):
        with open(GEOMETRY_FILE, "r") as f:
            geometry = f.read()
            app.geometry(geometry)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
load_geometry()
app.geometry("800x600")
app.title("CustomTkinter Example")

title = customtkinter.CTkLabel(app, text="Hello World!", font=("Arial", 20))
title.pack(padx=10, pady=10)

test_url = customtkinter.StringVar(app)
test_url.set("https://www.google.com")

link = customtkinter.CTkEntry(app, width=400, height=20, textvariable=test_url)
link.pack()

app.protocol("WM_DELETE_WINDOW", lambda: [save_geometry(), app.destroy()])

app.mainloop()