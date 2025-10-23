import tkinter as tk
from tkinter import simpledialog, messagebox, Entry

class HomeScreen(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        self.label = tk.Label(self, text="Home Screen")
        self.label.pack()

        self.add_name_button = tk.Button(self, text="Add Name", command=lambda: controller.show_frame(AddNameScreen))
        self.add_name_button.pack()

        self.show_distances_button = tk.Button(self, text="Show Distances", command=lambda: controller.show_frame(DistancesScreen))
        self.show_distances_button.pack()

        self.competition_button = tk.Button(self, text="Competition Mode", command=lambda: controller.show_frame(CompetitionScreen))
        self.competition_button.pack()

class AddNameScreen(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        self.label = tk.Label(self, text="Add Name Screen")
        self.label.pack()

        self.name_entry = Entry(self, width=20)
        self.name_entry.pack()

        self.save_name_button = tk.Button(self, text="Save Name", command=self.save_name)
        self.save_name_button.pack()

        self.delete_name_button = tk.Button(self, text="Delete Name", command=self.delete_name)
        self.delete_name_button.pack()

        self.home_button = tk.Button(self, text="Home", command=lambda: controller.show_frame(HomeScreen))
        self.home_button.pack()

    def save_name(self):
        name = self.name_entry.get()
        if name:
            self.controller.add_name(name)
            messagebox.showinfo("Success", f"Name '{name}' saved!")

    def delete_name(self):
        name = self.name_entry.get()
        if name:
            self.controller.delete_name(name)
            messagebox.showinfo("Success", f"Name '{name}' deleted!")

class DistancesScreen(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        self.label = tk.Label(self, text="Distances Screen")
        self.label.pack()

        self.name_entry = Entry(self, width=20)
        self.name_entry.pack()

        self.add_distance_button = tk.Button(self, text="Add Distance", command=self.add_distance)
        self.add_distance_button.pack()

        self.remove_distance_button = tk.Button(self, text="Remove Distance", command=self.remove_distance)
        self.remove_distance_button.pack()

        self.home_button = tk.Button(self, text="Home", command=lambda: controller.show_frame(HomeScreen))
        self.home_button.pack()

    def add_distance(self):
        name = self.name_entry.get()
        distance_str = simpledialog.askstring("Distance", f"Enter the distance for {name}:")
        if name and distance_str:
            distance = float(distance_str)
            self.controller.add_distance(name, distance)
            messagebox.showinfo("Success", f"Distance for '{name}' added!")

    def remove_distance(self):
        name = self.name_entry.get()
        if name:
            self.controller.remove_distance(name)
            messagebox.showinfo("Success", f"Distances for '{name}' removed!")

class CompetitionScreen(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        self.label = tk.Label(self, text="Competition Screen")
        self.label.pack()

        self.show_competition_button = tk.Button(self, text="Show Competition", command=self.show_competition)
        self.show_competition_button.pack()

        self.home_button = tk.Button(self, text="Home", command=lambda: controller.show_frame(HomeScreen))
        self.home_button.pack()

    def show_competition(self):
        competition_data = self.controller.get_competition_data()
        messagebox.showinfo("Competition Mode", competition_data)

class DistanceApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.attributes('-fullscreen', True)  # Open in full screen

        self.frames = {}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in (HomeScreen, AddNameScreen, DistancesScreen, CompetitionScreen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomeScreen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def add_name(self, name):
        # Add the implementation to store the name
        pass

    def delete_name(self, name):
        # Add the implementation to delete the name
        pass

    def add_distance(self, name, distance):
        # Add the implementation to store the distance
        pass

    def remove_distance(self, name):
        # Add the implementation to remove distances for a name
        pass

    def get_competition_data(self):
        # Add the implementation to get competition data
        pass

if __name__ == "__main__":
    app = DistanceApp()
    app.mainloop()

