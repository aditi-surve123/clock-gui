from tkinter import Label, Tk 
import time
app_window= Tk()
app_window.title("Digital clock")
app_window.geometry("430x200")
app_window.resizable(1,1)
text_font=("Boulder",68,'bold')
background="#9B59B6"
foreground="#363529"
border_width=20
label=Label(app_window,font=text_font,bg=background,fg=foreground,bd=border_width)
label.grid(row=0,column=1)

def digital_clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)
   
digital_clock()
app_window.mainloop()
