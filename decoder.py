import tkinter as tk
from tkinter import ttk

# Define the alphabet mapping for encryption
encryption_mapping = {
    'A': 'F', 'B': 'V', 'C': 'H', 'D': 'N', 'E': 'G', 'F': 'D', 'G': 'U', 'H': 'L',
    'I': 'T', 'J': 'A', 'K': 'M', 'L': 'O', 'M': 'K', 'N': 'P', 'O': 'B', 'P': 'R',
    'Q': 'S', 'R': 'C', 'S': 'E', 'T': 'W', 'U': 'Y', 'V': 'Z', 'W': 'X', 'X': 'J',
    'Y': 'Q', 'Z': 'I'
}

# Define the alphabet mapping for decryption
decryption_mapping = {v: k for k, v in encryption_mapping.items()}

def encrypt_message():
    input_text = encrypt_input_widget.get().upper()
    transformed_text = ''.join(encryption_mapping.get(char, char) for char in input_text)
    add_to_chat(input_text, transformed_text)

def decrypt_message():
    input_text = decrypt_input_widget.get().upper()
    transformed_text = ''.join(decryption_mapping.get(char, char) for char in input_text)
    add_to_chat(input_text, transformed_text)

def add_to_chat(original_text, transformed_text):
    original_message = f"Original: {original_text}"
    transformed_message = f"DECODED: {transformed_text}"  
    chat_text_widget.config(state=tk.NORMAL)
    chat_text_widget.insert(tk.END, original_message + "\n")
    chat_text_widget.insert(tk.END, transformed_message + "\n\n")
    chat_text_widget.config(state=tk.DISABLED)

def clear_input_output():
    encrypt_input_widget.delete(0, tk.END)
    decrypt_input_widget.delete(0, tk.END)
    chat_text_widget.config(state=tk.NORMAL)
    chat_text_widget.delete('1.0', tk.END)
    chat_text_widget.config(state=tk.DISABLED)

# Create the Tkinter window
root = tk.Tk()
root.title("DECODER")
root.geometry("800x400")
root.resizable(False, False)
root.configure(bg="black")
root.iconbitmap("decoder.ico")

# Create input frame for encryption
encryption_frame = tk.Frame(root, bg="black")
encryption_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Input text for encryption
encrypt_label = tk.Label(encryption_frame, text="Encrypt Message:", fg="#00FF00", bg="black")
encrypt_label.pack()

encrypt_input_widget = tk.Entry(encryption_frame, bg="black", fg="#00FF00", bd=2, font=("Arial", 14))
encrypt_input_widget.pack(pady=5)

# Button for encryption
encrypt_button = ttk.Button(encryption_frame, text="Encrypt", command=encrypt_message, style="Green.TButton")
encrypt_button.pack(pady=5)

# Create input frame for decryption
decryption_frame = tk.Frame(root, bg="black")
decryption_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Input text for decryption
decrypt_label = tk.Label(decryption_frame, text="Decrypt Message:", fg="#00FF00", bg="black")
decrypt_label.pack()

decrypt_input_widget = tk.Entry(decryption_frame, bg="black", fg="#00FF00", bd=2, font=("Arial", 14))
decrypt_input_widget.pack(pady=5)

# Button for decryption
decrypt_button = ttk.Button(decryption_frame, text="Decrypt", command=decrypt_message, style="Green.TButton")
decrypt_button.pack(pady=5)

# Create chat text widget with scrollbar
chat_frame = tk.Frame(root, bg="black")
chat_frame.pack(fill=tk.BOTH, expand=True)

chat_text_widget = tk.Text(chat_frame, width=60, height=20, state=tk.DISABLED, bg="black", fg="#00FF00")
chat_text_widget.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_scrollbar = ttk.Scrollbar(chat_frame, orient=tk.VERTICAL, command=chat_text_widget.yview)
chat_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_text_widget.config(yscrollcommand=chat_scrollbar.set)

# Button to clear input and output
clear_button = ttk.Button(root, text="Clear All", command=clear_input_output, style="Green.TButton")
clear_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
