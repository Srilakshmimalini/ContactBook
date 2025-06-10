import tkinter as tk
from tkinter import messagebox, ttk

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x600")
        self.root.config(bg="#2c3e50")

        self.contacts = {}

        # Title Frame
        title_frame = tk.Frame(root, bg="#fffff", pady=20)
        title_frame.pack(fill="x")

        title_label = tk.Label(title_frame, text="ContactBook", font=("Helvetica", 24, "bold"), fg="white", bg="#2980b9")
        title_label.pack()

        # Input Frame
        input_frame = tk.Frame(root, bg="#34495e", padx=20, pady=20)
        input_frame.pack(fill="x", pady=20)

        # Name Input
        self.name_label = tk.Label(input_frame, text="Name :", font=("Arial", 14), bg="#34495e", fg="white")
        self.name_label.grid(row=0, column=0, sticky="e", pady=5)
        self.name_entry = tk.Entry(input_frame, font=("Arial", 14), width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Phone Number Input
        self.phone_label = tk.Label(input_frame, text="Phone Number:", font=("Arial", 14), bg="#34495e", fg="white")
        self.phone_label.grid(row=1, column=0, sticky="e", pady=5)
        self.phone_entry = tk.Entry(input_frame, font=("Arial", 14), width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons Frame
        button_frame = tk.Frame(root, bg="#2c3e50", pady=20)
        button_frame.pack()

        self.add_button = tk.Button(button_frame, text="Add Contact", font=("Arial", 14, "bold"), bg="#27ae60", fg="white", command=self.add_contact)
        self.add_button.grid(row=0, column=0, padx=10)

        self.edit_button = tk.Button(button_frame, text="Edit Contact", font=("Arial", 14, "bold"), bg="#2980b9", fg="white", command=self.edit_contact)
        self.edit_button.grid(row=0, column=1, padx=10)

        self.delete_button = tk.Button(button_frame, text="Delete Contact", font=("Arial", 14, "bold"), bg="#c0392b", fg="white", command=self.delete_contact)
        self.delete_button.grid(row=0, column=2, padx=10)

        # Search Frame
        search_frame = tk.Frame(root, bg="#2c3e50", pady=20)
        search_frame.pack(fill="x")

        self.search_label = tk.Label(search_frame, text="Search:", font=("Arial", 14), bg="#2c3e50", fg="white")
        self.search_label.grid(row=0, column=0, sticky="e")
        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=30)
        self.search_entry.grid(row=0, column=1, padx=10)
        self.search_button = tk.Button(search_frame, text="Search", font=("Arial", 14, "bold"), bg="#f39c12", fg="white", command=self.search_contact)
        self.search_button.grid(row=0, column=2, padx=10)

        # Listbox Frame
        listbox_frame = tk.Frame(root, bg="#2c3e50", pady=20)
        listbox_frame.pack(fill="both", expand=True)

        self.contacts_listbox = tk.Listbox(listbox_frame, font=("Arial", 14), bg="#ecf0f1", borderwidth=2, relief=tk.SUNKEN)
        self.contacts_listbox.pack(side="left", fill="both", expand=True, padx=20, pady=10)

        scrollbar = tk.Scrollbar(listbox_frame, command=self.contacts_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.contacts_listbox.config(yscrollcommand=scrollbar.set)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name or not phone:
            messagebox.showerror("Error", "Both name and phone number are required.")
            return

        if name in self.contacts:
            messagebox.showerror("Error", "Contact already exists.")
            return

        self.contacts[name] = phone
        self.update_contact_list()
        self.clear_entries()

    def edit_contact(self):
        selected_contact = self.contacts_listbox.curselection()
        if not selected_contact:
            messagebox.showerror("Error", "Select a contact to edit.")
            return

        old_name = self.contacts_listbox.get(selected_contact).split(":")[0].strip()
        new_name = self.name_entry.get().strip()
        new_phone = self.phone_entry.get().strip()

        if not new_name or not new_phone:
            messagebox.showerror("Error", "Both name and phone number are required.")
            return

        if new_name in self.contacts and new_name != old_name:
            messagebox.showerror("Error", "A contact with this name already exists.")
            return

        del self.contacts[old_name]
        self.contacts[new_name] = new_phone
        self.update_contact_list()
        self.clear_entries()

    def delete_contact(self):
        selected_contact = self.contacts_listbox.curselection()
        if not selected_contact:
            messagebox.showerror("Error", "Select a contact to delete.")
            return

        name = self.contacts_listbox.get(selected_contact).split(":")[0].strip()
        del self.contacts[name]
        self.update_contact_list()
        self.clear_entries()

    def search_contact(self):
        search_term = self.search_entry.get().strip().lower()
        filtered_contacts = {name: phone for name, phone in self.contacts.items() if search_term in name.lower() or search_term in phone}
        self.update_contact_list(filtered_contacts)

    def update_contact_list(self, contacts=None):
        if contacts is None:
            contacts = self.contacts

        self.contacts_listbox.delete(0, tk.END)
        for name, phone in contacts.items():
            self.contacts_listbox.insert(tk.END, f"{name}: {phone}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
