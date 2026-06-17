import tkinter as tk
from tkinter import messagebox
import os

# --- SHOP STANDARDS ---
TOLA_BASE = 12.150
PURE_GOLD = 19.3
IMPURITY = 10.5

# --- THEME COLORS ---
DARK_BG = "#0f0f0f"        # Deep Black
CARD_BG = "#1a1a1a"        # Card Grey
ACCENT_GOLD = "#ffcc00"    # Sharp Gold
TEXT_MAIN = "#ffffff"      # Pure White
TEXT_DIM = "#888888"       # Muted Grey
PRICE_COLOR = "#00ffaa"    # Neon Mint

def convert_to_tmr(grams):
    """Converts grams to Tola-Masha-Rati display"""
    total_tola = grams / TOLA_BASE
    t = int(total_tola)
    m = int((total_tola - t) * 12)
    r = round(((total_tola - t) * 12 - m) * 8, 2)
    return f"{t}T {m}M {r}R"

def calculate():
    try:
        rate = float(entry_rate.get())
        air = float(entry_air.get())
        mode = var_mode.get()

        if mode == "Pasa":
            pasa_w = air
            karat = 24.0
            dens = 19.3
        else:
            water = float(entry_water.get())
            # Basic density check to avoid division by zero
            if air <= water:
                messagebox.showerror("Math Error", "Weight in Air must be greater than Water.")
                return
                
            dens = air / (air - water)
            # Karat formula: ((Density - 10.5) / 8.8) * 24
            karat = ((dens - IMPURITY) / (PURE_GOLD - IMPURITY)) * 24
            karat = max(0, min(24, karat))
            pasa_w = air * (karat / 24)

        price = (pasa_w / TOLA_BASE) * rate

        # Update Display Labels
        lbl_karat.config(text=f"{round(karat, 2)}K")
        lbl_pasa.config(text=f"{round(pasa_w, 3)}g")
        lbl_tmr.config(text=convert_to_tmr(pasa_w))
        lbl_price.config(text=f"{round(price, 0):,} PKR")
        lbl_dens.config(text=f"Density: {round(dens, 3)}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter numbers only.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def save_receipt():
    """Saves the current result to a text file"""
    try:
        content = (
            "---------------------------\n"
            "   SARAFA LAB RECEIPT\n"
            "---------------------------\n"
            f"Karat:      {lbl_karat.cget('text')}\n"
            f"Gross Wt:   {entry_air.get()}g\n"
            f"Net Pasa:   {lbl_pasa.cget('text')}\n"
            f"TMR:        {lbl_tmr.cget('text')}\n"
            "---------------------------\n"
            f"Total:      {lbl_price.cget('text')}\n"
            "---------------------------\n"
            "Thank you for your business."
        )
        with open("last_receipt.txt", "w") as f:
            f.write(content)
        messagebox.showinfo("Success", "Receipt saved to 'last_receipt.txt'")
    except:
        messagebox.showerror("Error", "Could not save receipt.")

# --- UI WINDOW ---
root = tk.Tk()
root.title("Sarafa Pro Ultra")
root.attributes('-fullscreen', True)
root.configure(bg=DARK_BG)

# Top Bar (Control Buttons)
top_bar = tk.Frame(root, bg=DARK_BG)
top_bar.pack(side="top", fill="x", padx=20, pady=10)

# FIXED: Changed px=10 to padx=10
btn_exit = tk.Button(top_bar, text="✕", command=root.destroy, bg="#333", fg="white", bd=0, padx=15, pady=5, cursor="hand2")
btn_exit.pack(side="right")

btn_min = tk.Button(top_bar, text="—", command=lambda: root.iconify(), bg="#333", fg="white", bd=0, padx=15, pady=5, cursor="hand2")
btn_min.pack(side="right", padx=5)

# Center Content Wrapper
center_frame = tk.Frame(root, bg=DARK_BG)
center_frame.place(relx=0.5, rely=0.5, anchor="center")

# Titles
tk.Label(center_frame, text="SARAFA LAB PRO", font=("Impact", 60), bg=DARK_BG, fg=ACCENT_GOLD).pack()
tk.Label(center_frame, text="NOWSHERA OFFICIAL EDITION", font=("Arial", 14, "bold"), bg=DARK_BG, fg=TEXT_DIM).pack(pady=(0, 40))

# --- INPUT CARD ---
card_border = tk.Frame(center_frame, bg="#333333", padx=2, pady=2) # Shadow effect
card_border.pack()

card = tk.Frame(card_border, bg=CARD_BG, padx=50, pady=40)
card.pack()

def create_styled_input(parent, label):
    tk.Label(parent, text=label, font=("Verdana", 10, "bold"), bg=CARD_BG, fg=TEXT_DIM).pack(anchor="w")
    e = tk.Entry(parent, font=("Consolas", 22), bg="#000", fg=ACCENT_GOLD, insertbackground="white", bd=0, justify="center")
    e.pack(pady=(5, 20), ipady=10, fill="x")
    return e

entry_rate = create_styled_input(card, "CURRENT GOLD RATE (PKR PER TOLA)")
entry_air = create_styled_input(card, "WEIGHT IN AIR (GRAMS)")
entry_water = create_styled_input(card, "WEIGHT IN WATER (FOR LAB TEST)")

# Mode Toggle
var_mode = tk.StringVar(value="Lab")
mode_box = tk.Frame(card, bg=CARD_BG)
mode_box.pack(pady=10)
tk.Radiobutton(mode_box, text="SONA PASA (24K)", variable=var_mode, value="Pasa", bg=CARD_BG, fg=TEXT_MAIN, selectcolor="#000", font=("Arial", 11), activebackground=CARD_BG).pack(side="left", padx=20)
tk.Radiobutton(mode_box, text="LAB TEST (PURITY)", variable=var_mode, value="Lab", bg=CARD_BG, fg=TEXT_MAIN, selectcolor="#000", font=("Arial", 11), activebackground=CARD_BG).pack(side="left", padx=20)

# Buttons Section
btn_calc = tk.Button(center_frame, text="GENERATE PURITY REPORT", command=calculate, bg=ACCENT_GOLD, fg="black", font=("Arial", 16, "bold"), width=35, bd=0, pady=10, cursor="hand2")
btn_calc.pack(pady=25)

btn_print = tk.Button(center_frame, text="💾 SAVE LAST RECEIPT", command=save_receipt, bg="#222", fg=TEXT_DIM, font=("Arial", 10, "bold"), width=25, bd=0, pady=5, cursor="hand2")
btn_print.pack()

# --- LARGE RESULTS DISPLAY ---
lbl_karat = tk.Label(center_frame, text="--K", font=("Arial", 120, "bold"), bg=DARK_BG, fg=ACCENT_GOLD)
lbl_karat.pack(pady=10)

results_sub = tk.Frame(center_frame, bg=DARK_BG)
results_sub.pack()

lbl_pasa = tk.Label(results_sub, text="0.000 g", font=("Arial", 30), bg=DARK_BG, fg=TEXT_MAIN)
lbl_pasa.pack()

lbl_tmr = tk.Label(results_sub, text="0T 0M 0R", font=("Arial", 18), bg=DARK_BG, fg=TEXT_DIM)
lbl_tmr.pack()

lbl_dens = tk.Label(results_sub, text="Density: 0.00", font=("Arial", 11), bg=DARK_BG, fg="#444")
lbl_dens.pack(pady=5)

lbl_price = tk.Label(center_frame, text="0 PKR", font=("Arial", 50, "bold"), bg=DARK_BG, fg=PRICE_COLOR)
lbl_price.pack(pady=20)

root.mainloop()