import tkinter as tk
from tkinter import messagebox
import mido
import json

class MIDIMaestro:
    def __init__(self, root):
        self.root = root
        self.root.title("MidiM MIDIMaestro - MIDI Controller Interface")
        self.root.geometry("600x400")

        # MIDI setup
        self.output = mido.open_output()  # Opens default MIDI output
        self.midi_mappings = {}

        # GUI elements
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Save Layout", command=self.save_layout)
        self.file_menu.add_command(label="Load Layout", command=self.load_layout)

        # Draggable controls
        self.controls = []
        self.selected = None

        # Add some example controls (slider, button, knob)
        self.add_control("Slider", 50, 50)
        self.add_control("Button", 150, 50)
        self.add_control("Knob", 250, 50)

        # Bind mouse events for dragging
        self.canvas.bind("<Button-1>", self.select_control)
        self.canvas.bind("<B1-Motion>", self.drag_control)
        self.canvas.bind("<ButtonRelease-1>", self.release_control)

        # MIDI mapping button
        tk.Button(self.root, text="Map MIDI", command=self.map_midi).pack(pady=10)

    def add_control(self, control_type, x, y):
        """Add a draggable control to the canvas."""
        color = {"Slider": "blue", "Button": "red", "Knob": "green"}[control_type]
        control_id = self.canvas.create_rectangle(x, y, x+50, y+50, fill=color, tags=control_type)
        self.controls.append({"id": control_id, "type": control_type, "midi": None})
        self.canvas.tag_bind(control_id, "<Button-1>", lambda e: self.select_control(e))

    def select_control(self, event):
        """Select a control to drag or map."""
        self.selected = self.canvas.find_closest(event.x, event.y)[0]

    def drag_control(self, event):
        """Drag the selected control."""
        if self.selected:
            self.canvas.coords(self.selected, event.x-25, event.y-25, event.x+25, event.y+25)

    def release_control(self, event):
        """Release the dragged control."""
        self.selected = None

    def map_midi(self):
        """Map a MIDI command to the selected control."""
        if not self.selected:
            messagebox.showwarning("Warning", "Select a control first!")
            return

        # Example MIDI message (CC message, channel 0, control 1, value 127)
        midi_msg = mido.Message('control_change', channel=0, control=1, value=127)
        for control in self.controls:
            if control["id"] == self.selected:
                control["midi"] = midi_msg
                messagebox.showinfo("Success", f"Mapped {control['type']} to {midi_msg}")
                self.output.send(midi_msg)  # Test the MIDI output
                break

    def save_layout(self):
        """Save the current layout to a JSON file."""
        layout = []
        for control in self.controls:
            coords = self.canvas.coords(control["id"])
            layout.append({
                "type": control["type"],
                "x": coords[0],
                "y": coords[1],
                "midi": str(control["midi"]) if control["midi"] else None
            })
        with open("layout.json", "w") as f:
            json.dump(layout, f)
        messagebox.showinfo("Saved", "Layout saved to layout.json")

    def load_layout(self):
        """Load a layout from a JSON file."""
        try:
            with open("layout.json", "r") as f:
                layout = json.load(f)
            self.canvas.delete("all")
            self.controls = []
            for item in layout:
                self.add_control(item["type"], item["x"], item["y"])
            messagebox.showinfo("Loaded", "Layout loaded from layout.json")
        except FileNotFoundError:
            messagebox.showerror("Error", "No saved layout found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MIDIMaestro(root)
    root.mainloop()