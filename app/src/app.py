import tkinter as tk
import os
import requests


def check():
    host = os.getenv('RECIPE_ADAPTER_SERVICE_HOST')
    port = os.getenv('RECIPE_ADAPTER_SERVICE_PORT')
    response = requests.get(f"http://{host}:{port}/content")
    # print(f"response: {response.status_code}, {response.json()}")
    tk.Label(root_window, text=response.json()).pack()


root_window = tk.Tk()

root_window.title("Test application")
root_window.geometry("300x100")

tk.Button(root_window, text="send", width=10, command=check).pack()
tk.Button(root_window, text='Exit', width=10, command=root_window.destroy).pack()

root_window.mainloop()
