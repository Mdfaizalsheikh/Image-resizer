import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageResizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer")

        
        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.grid(row=0, column=0, padx=10, pady=10)

        
        self.width_label = tk.Label(root, text="Width")
        self.width_label.grid(row=1, column=0, padx=10, pady=5)
        self.width_entry = tk.Entry(root)
        self.width_entry.grid(row=1, column=1, padx=10, pady=5)

        self.height_label = tk.Label(root, text="Height")
        self.height_label.grid(row=2, column=0, padx=10, pady=5)
        self.height_entry = tk.Entry(root)
        self.height_entry.grid(row=2, column=1, padx=10, pady=5)

        
        self.resize_button = tk.Button(root, text="Resize Image", command=self.resize_image)
        self.resize_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        
        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        
        self.image_label = tk.Label(root)
        self.image_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        self.loaded_image = None
        self.resized_image = None

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.loaded_image = Image.open(file_path)
            img = ImageTk.PhotoImage(self.loaded_image)
            self.image_label.config(image=img)
            self.image_label.image = img

    def resize_image(self):
        if self.loaded_image:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            self.resized_image = self.loaded_image.resize((width, height), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(self.resized_image)
            self.image_label.config(image=img)
            self.image_label.image = img

    def save_image(self):
        if self.resized_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                self.resized_image.save(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageResizer(root)
    root.mainloop()
