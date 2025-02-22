import tkinter as tk
import requests
import threading

def fetch_data():
    def api_call():
        try:
            response = requests.get("http://127.0.0.1:5000/data")
            data = response.json()
            label.config(text=data["message"])
        except Exception as e:
            label.config(text=f"Error: {e}")

    threading.Thread(target=api_call, daemon=True).start()  # Run API call in a thread

# Tkinter UI
root = tk.Tk()
root.title("Tkinter + Flask API")

label = tk.Label(root, text="Click to Fetch Data", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Fetch from Flask", command=fetch_data)
button.pack()

root.mainloop()
