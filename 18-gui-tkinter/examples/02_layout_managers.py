"""
Demonstrates the three geometry managers, pack, grid and place, each in
its own Frame so they never mix inside one container.
Run: python 02_layout_managers.py
A window opens with three labelled areas. Resize it to see that pack and
grid widgets move with the window while place widgets stay fixed.
"""

import tkinter as tk

window = tk.Tk()
window.title("pack, grid and place")
window.geometry("420x360")

# --- pack: stacks widgets top to bottom (or side by side) ---------------
pack_frame = tk.LabelFrame(window, text="pack", padx=5, pady=5)
pack_frame.pack(fill="x", padx=10, pady=5)

tk.Label(pack_frame, text="Top", bg="lightblue").pack(fill="x")
tk.Label(pack_frame, text="Middle", bg="lightgreen").pack(fill="x")
tk.Button(pack_frame, text="Left", width=10).pack(side="left", padx=5, pady=5)
tk.Button(pack_frame, text="Right", width=10).pack(side="left", padx=5, pady=5)

# --- grid: rows and columns like a table ---------------------------------
grid_frame = tk.LabelFrame(window, text="grid", padx=5, pady=5)
grid_frame.pack(fill="x", padx=10, pady=5)

tk.Label(grid_frame, text="First name:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
tk.Entry(grid_frame).grid(row=0, column=1, padx=5, pady=2)
tk.Label(grid_frame, text="Last name:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
tk.Entry(grid_frame).grid(row=1, column=1, padx=5, pady=2)
# columnspan=2 lets the button sit under both columns.
tk.Button(grid_frame, text="Save").grid(row=2, column=0, columnspan=2, pady=5)

# --- place: exact pixel positions ---------------------------------------
place_frame = tk.LabelFrame(window, text="place", height=100)
place_frame.pack(fill="x", padx=10, pady=5)
# Without this the frame would shrink to fit its (placed) children.
place_frame.pack_propagate(False)

tk.Label(place_frame, text="At (20, 10)", bg="yellow").place(x=20, y=10)
tk.Label(place_frame, text="At (200, 50)", bg="orange").place(x=200, y=50)

window.mainloop()
