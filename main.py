from tkinter import * 
import customtkinter
from PIL import ImageTk, Image
from bot import Bot

root = customtkinter.CTk()

root.title('Whatsapp Message Bot')

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
root.geometry("1000x500")
root.configure(bg='black')

#Bot.message_bot()

bot = Bot()

def send_msg():
   root.destroy()
   bot.times = int(whatsapp_entry_times.get())
   bot.message = whatsapp_entry_message.get()
   bot.receiver = whatsapp_entry_receiver.get()
   bot.message_bot()
    

whatsapp_frame = customtkinter.CTkFrame(master=root,
                               width=1000,
                               height=500,
                               corner_radius=10,
                               bg='black',
                               fg_color='#FEB139',
                               border_width=2, border_color="white")

whatsapp_receiver = customtkinter.CTkLabel(root, text="Receiver:", width=130,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#FEB139')

whatsapp_times = customtkinter.CTkLabel(root, text="Times:", width=130,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#FEB139')

whatsapp_message = customtkinter.CTkLabel(root, text=f"Message:", width=140,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#FEB139')

whatsapp_entry_receiver = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                            fg_color='#0F3D3E',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#FEB139',
                               border_width=2, border_color="white"
                            )

whatsapp_entry_times = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                            fg_color='#0F3D3E',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#E2DCC8',
                               border_width=2, border_color="white"
                            )

whatsapp_entry_message = customtkinter.CTkEntry(root, width=130,
                               height=40,
                               corner_radius=10,
                            fg_color='#0F3D3E',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#FEB139',
                               border_width=2, border_color="white"
                            )

whatsapp_button = customtkinter.CTkButton(root, command=send_msg, width=195,
                                 height=40,
                                 corner_radius=8,
                                 text="Send Message",
                                 fg_color='#0F3D3E',
                                 text_font=('Times New Roman', 20),
                               bg_color='#FEB139',
                               hover_color='#3AB4F2',
                               border_width=2, border_color="white"
                                 )

#insert default text in Entry Boxes
whatsapp_entry_times.insert(0, 1)
#Packing them on the screen
whatsapp_frame.grid(row=0, column=0, columnspan=4, rowspan=6, sticky='news')
whatsapp_receiver.grid(row=0, column=0, sticky='ew', padx=10, columnspan=2)
whatsapp_times.grid(row=0, column=2, sticky='ew', padx=10, columnspan=2)
whatsapp_message.grid(row=2, column=0, sticky='ew', padx=10, columnspan=4)
whatsapp_entry_receiver.grid(row=1, column=0, padx=10, sticky='ew', columnspan=2)
whatsapp_entry_times.grid(row=1, column=2, padx=10, sticky='ew', columnspan=2)
whatsapp_entry_message.grid(row=3, column=0, padx=10, sticky='nsew', columnspan=4, rowspan=2)
whatsapp_button.grid(row=5, column=0, columnspan=4, sticky='ew', padx=10)

root.mainloop()