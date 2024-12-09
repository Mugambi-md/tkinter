import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
from loan_app import loan_arrears, months_difference

def show_buttons():
    exit_button.pack(side="left", padx=10)
    next_button.pack(side="right", padx=10)
def exit_app():
    root.destroy() # Close the application
def next_calculation(): # Clear all inputs and reset dropdowns
    principal_entry.delete(0, tk.END)
    period_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    p_bal_entry.delete(0, tk.END)
    i_bal_entry.delete(0, tk.END)
    year_combo.set("Year")
    month_combo.set("Month")
    day_combo.set("Day")
    result_label.config(text="")
    # Hide the buttons again
    exit_button.pack_forget()
    next_button.pack_forget()

def calculate_arrears():
    try:
        principal = float(principal_entry.get())
        period = int(period_entry.get())
        rate = float(rate_entry.get())
        p_bal = float(p_bal_entry.get())
        i_bal = float(i_bal_entry.get())
        selected_year = int(year_combo.get())
        selected_month = int(month_combo.get())
        selected_day = int(day_combo.get())

        s_period = months_difference(selected_year, selected_month, selected_day)

        result = loan_arrears(principal, period, rate, s_period, p_bal, i_bal)
        result_label.config(text=result)
        show_buttons()
    except ValueError:
        result_label.config(text="Invalid Input. please enter valid numbers.")
    except Exception as e:
        result_label.config(text=f"Error: {e}")
# Define a function to move focus to the next widget
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

# Main window
root = tk.Tk()
root.title("Loan Arrears Checker")

# Input frame using grind
input_frame =tk.Frame(root)
input_frame.pack(padx=10, pady=10)
# Principal
tk.Label(input_frame, text="Initial Principal:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
principal_entry = tk.Entry(input_frame)
principal_entry.bind("<Return>", focus_next_widget)
principal_entry.grid(row=0, column=1, padx=5, pady=5)
# Period
tk.Label(input_frame, text="Repayment Period(months):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
period_entry = tk.Entry(input_frame)
period_entry.bind("<Return>", focus_next_widget)
period_entry.grid(row=1, column=1, padx=5, pady=5)
#Rate
tk.Label(input_frame, text="Monthly Interest Rate(%):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
rate_entry = tk.Entry(input_frame)
rate_entry.bind("<Return>", focus_next_widget)
rate_entry.grid(row=2, column=1, padx=5, pady=5)
#Principal Balance
tk.Label(input_frame, text="Enter Principal Balance:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
p_bal_entry = tk.Entry(input_frame)
p_bal_entry.bind("<Return>", focus_next_widget)
p_bal_entry.grid(row=3, column=1, padx=5, pady=5)
#Interest Balance
tk.Label(input_frame, text="Enter Interest Balance:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
i_bal_entry = tk.Entry(input_frame)
i_bal_entry.bind("<Return>", focus_next_widget)
i_bal_entry.grid(row=4, column=1, padx=5, pady=5)
#Date Selection
tk.Label(input_frame, text="Select Issues Date:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
date_frame = tk.Frame(input_frame)
date_frame.grid(row=5, column=1, padx=5, pady=5)
# Year Dropdown
year_combo = ttk.Combobox(date_frame, values=[str(year) for year in range(date.today().year, date.today().year-15, -1)], width=5)
year_combo.set("Year")
year_combo.bind("<Return>", focus_next_widget)
year_combo.pack(side="left", padx=2)
#Month Dropdown
month_combo = ttk.Combobox(date_frame, values=[str(month) for month in range(1, 13)], width=3)
month_combo.set("Month")
month_combo.bind("<Return>", focus_next_widget)
month_combo.pack(side="left", padx=2)
#Day dropdown
day_combo = ttk.Combobox(date_frame, values=[str(day) for day in range(1, 32)], width=3)
day_combo.set("Day")
day_combo.bind("<Return>", focus_next_widget)
day_combo.pack(side="left", padx=2)
#Calculate button and result label
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)
calculate_button = tk.Button(bottom_frame, text="Calculate", command=calculate_arrears)
calculate_button.pack(side="top", pady=5)

result_label = tk.Label(bottom_frame, text="", fg="blue", wraplength=400)
result_label.pack(side="top", pady=5)
# Exit and Next button frame
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)
exit_button = tk.Button(buttons_frame, text="Exit", command=exit_app)
next_button = tk.Button(buttons_frame, text="Next", command=next_calculation)
# Run the application
root.mainloop()