import tkinter as tk
from tkinter import ttk, messagebox
from math import sqrt, pi

class VolumeCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Shape Volume Calculator")
        self.root.geometry("500x650")
        self.root.resizable(True, True)
        
        # Shape information WITHOUT dictionary
        self.shapes = [
            "Cuboid (Rectangular Prism)",
            "Pyramid (Right Rectangular)", 
            "Cylinder",
            "Sphere",
            "Cone",
            "Ellipsoid",
            "Torus (Donut)",
            "Hexagonal Prism"
        ]
        
        self.setup_styles()
        self.create_widgets()
    
    def setup_styles(self):
        """Configure ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Title.TLabel", font=("Arial", 16, "bold"))
        style.configure("Result.TLabel", font=("Arial", 12, "bold"), foreground="blue")
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Title
        title_label = ttk.Label(main_frame, text="3D Shape Volume Calculator",
                                style="Title.TLabel")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Shape selection
        ttk.Label(main_frame, text="Select Shape:", font=("Arial", 11)).grid(
            row=1, column=0, sticky=tk.W, pady=5)

        self.shape_var = tk.StringVar()
        
        self.shape_combo = ttk.Combobox(main_frame, textvariable=self.shape_var,
                                        values=self.shapes, state="readonly", width=25)
        self.shape_combo.grid(row=1, column=1, pady=5, padx=(10, 0))
        self.shape_combo.current(0)
        self.shape_combo.bind("<<ComboboxSelected>>", self.update_input_fields)

        # Unit selection
        ttk.Label(main_frame, text="Unit:", font=("Arial", 11)).grid(
            row=2, column=0, sticky=tk.W, pady=5)

        self.unit_var = tk.StringVar(value="cm")
        units = ["cm", "m", "mm", "inches", "feet", "yards", "km", "miles"]
        self.unit_combo = ttk.Combobox(main_frame, textvariable=self.unit_var,
                                       values=units, state="readonly", width=10)
        self.unit_combo.grid(row=2, column=1, sticky=tk.W, pady=5, padx=(10, 0))

        # Input fields frame
        self.input_frame = ttk.LabelFrame(main_frame, text="Dimensions", padding="10")
        self.input_frame.grid(row=3, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))

        # Initialize input fields
        self.input_entries = {}
        self.create_input_fields()

        # Calculate button
        self.calc_button = ttk.Button(main_frame, text="Calculate Volume",
                                      command=self.calculate_volume)
        self.calc_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Result display
        result_frame = ttk.LabelFrame(main_frame, text="Result", padding="15")
        result_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)

        self.result_var = tk.StringVar(value="Volume will be displayed here")
        self.result_label = ttk.Label(result_frame, textvariable=self.result_var,
                                      style="Result.TLabel", wraplength=400)
        self.result_label.pack()

        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)

        # Clear button
        ttk.Button(button_frame, text="Clear All",
                   command=self.clear_fields).pack(side=tk.LEFT, padx=5)

        # Exit button
        ttk.Button(button_frame, text="Exit",
                   command=self.root.quit).pack(side=tk.LEFT, padx=5)

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        self.input_frame.columnconfigure(1, weight=1)
    
    def create_input_fields(self):
        """Create input fields based on selected shape"""
        shape = self.shape_var.get() or self.shapes[0]
        
        # Clear existing fields
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        
        self.input_entries = {}
        row = 0
        
        # Create fields based on shape
        if shape == "Cuboid (Rectangular Prism)":
            ttk.Label(self.input_frame, text="Length:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["length"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["length"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            row += 1
            
            ttk.Label(self.input_frame, text="Width:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["width"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["width"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            row += 1
            
            ttk.Label(self.input_frame, text="Height:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["height"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["height"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            
        elif shape == "Pyramid (Right Rectangular)":
            ttk.Label(self.input_frame, text="Base Length:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["length"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["length"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            row += 1
            
            ttk.Label(self.input_frame, text="Base Width:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["width"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["width"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            row += 1
            
            ttk.Label(self.input_frame, text="Height:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["height"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["height"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            
        elif shape == "Cylinder":
            ttk.Label(self.input_frame, text="Radius:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["radius"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["radius"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            row += 1
            
            ttk.Label(self.input_frame, text="Height:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["height"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["height"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            
        elif shape == "Sphere":
            ttk.Label(self.input_frame, text="Radius:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["radius"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["radius"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            
        elif shape == "Cone":
            ttk.Label(self.input_frame, text="Radius:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["radius"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["radius"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            row += 1
            
            ttk.Label(self.input_frame, text="Height:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["height"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["height"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            
        elif shape == "Ellipsoid":
            ttk.Label(self.input_frame, text="a axis:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["a"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["a"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            row += 1
            
            ttk.Label(self.input_frame, text="b axis:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["b"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["b"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            row += 1
            
            ttk.Label(self.input_frame, text="c axis:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["c"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["c"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            
        elif shape == "Torus (Donut)":
            ttk.Label(self.input_frame, text="Major Radius:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["major"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["major"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            row += 1
            
            ttk.Label(self.input_frame, text="Minor Radius:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["minor"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["minor"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            
        elif shape == "Hexagonal Prism":
            ttk.Label(self.input_frame, text="Base Edge:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["edge"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["edge"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
            row += 1
            
            ttk.Label(self.input_frame, text="Height:").grid(row=row, column=0, sticky=tk.W, pady=5)
            self.input_entries["height"] = ttk.Entry(self.input_frame, width=20)
            self.input_entries["height"].grid(row=row, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
    
    def update_input_fields(self, event=None):
        """Update input fields when shape changes"""
        self.create_input_fields()
    
    def clear_fields(self):
        """Clear all input fields and reset"""
        for entry in self.input_entries.values():
            entry.delete(0, tk.END)
        self.result_var.set("Volume will be displayed here")
    
    def calculate_volume(self):
        """Calculate and display volume"""
        try:
            shape = self.shape_var.get()
            unit = self.unit_var.get()
            volume = 0
            
            if shape == "Cuboid (Rectangular Prism)":
                length = float(self.input_entries["length"].get())
                width = float(self.input_entries["width"].get())
                height = float(self.input_entries["height"].get())
                volume = length * width * height
                
            elif shape == "Pyramid (Right Rectangular)":
                length = float(self.input_entries["length"].get())
                width = float(self.input_entries["width"].get())
                height = float(self.input_entries["height"].get())
                volume = (length * width * height) / 3
                
            elif shape == "Cylinder":
                radius = float(self.input_entries["radius"].get())
                height = float(self.input_entries["height"].get())
                volume = pi * (radius ** 2) * height
                
            elif shape == "Sphere":
                radius = float(self.input_entries["radius"].get())
                volume = (4 / 3) * pi * (radius ** 3)
                
            elif shape == "Cone":
                radius = float(self.input_entries["radius"].get())
                height = float(self.input_entries["height"].get())
                volume = (pi * (radius ** 2) * height) / 3
                
            elif shape == "Ellipsoid":
                a = float(self.input_entries["a"].get())
                b = float(self.input_entries["b"].get())
                c = float(self.input_entries["c"].get())
                volume = (4 / 3) * pi * a * b * c
                
            elif shape == "Torus (Donut)":
                major = float(self.input_entries["major"].get())
                minor = float(self.input_entries["minor"].get())
                if minor >= major:
                    messagebox.showwarning("Input Error", "Minor radius must be smaller than Major radius!")
                    return
                volume = (2 * pi * major) * (pi * minor ** 2)
                
            elif shape == "Hexagonal Prism":
                edge = float(self.input_entries["edge"].get())
                height = float(self.input_entries["height"].get())
                volume = (3 * sqrt(3) / 2) * (edge ** 2) * height
            
            # Display result
            result_text = f"Volume of {shape}: {volume:.4f} {unit}³"
            self.result_var.set(result_text)
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers in all fields!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def run_gui():
    """Run the Tkinter GUI"""
    root = tk.Tk()
    app = VolumeCalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
