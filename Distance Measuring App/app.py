import tkinter as tk
from tkinter import simpledialog, Entry

class DistanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Distance App")
        self.distances = {}  # Dictionary to store distances

        self.label = tk.Label(root, text= input("Enter a name and distance:"))
        self.label.pack()

        self.name_entry = Entry(root, width=20)
        self.name_entry.pack()

        self.distance_entry = Entry(root, width=20)
        self.distance_entry.pack()

        self.add_button = tk.Button(root, text="Add Name", command=self.add_Name)
        self.add_button.pack()

        self.show_button = tk.Button(root, text="Show Distances", command=self.show_distances)
        self.show_button.pack()

        self.competition_button = tk.Button(root, text="Competition Mode", command=self.competition_mode)
        self.competition_button.pack()

    def add_Name(self):
        name = self.name_entry.get()
        distance_str = self.distance_entry.get()
        if name and distance_str:
            distance = float(distance_str)
            self.distances[name] = distance
            self.name_entry.delete(0, tk.END)
            self.distance_entry.delete(0, tk.END)

    def show_distances(self):
        distances_str = "\n".join(f"{name}: {distance} feet" for name, distance in self.distances.items())
        tk.messagebox.showinfo("Distances", distances_str)

    def competition_mode(self):
        sorted_distances = sorted(self.distances.items(), key=lambda x: x[1], reverse=True)
        sorted_distances_str = "\n".join(f"{name}: {distance} meters" for name, distance in sorted_distances)
        tk.messagebox.showinfo("Competition Mode", sorted_distances_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = DistanceApp(root)
    root.mainloop()

