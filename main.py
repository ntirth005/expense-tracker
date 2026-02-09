import tkinter as tk
from tkinter import filedialog
import pandas as pd
from numpy import nan
from graphs import create_transaction_balance_plot, create_credits_debits_bar_chart, create_transaction_types_pie_chart, create_cumulative_credits_debits_chart
from webTkinter2 import plotGraphs

def process_csv(file_path):
    n = 0
    while True:
        try:
            data = pd.read_csv(file_path, header=n)
            if 'Credit' in data.columns or 'credit' in data.columns:
                break
            else:
                n += 1
        except Exception:
            n += 1
            continue
    print(data.head())
    data.set_index("Sr No", inplace=True)
    data = data[data["Credit" and 'Debit'] != nan]
    data = data.iloc[:-1]
    
    # Convert 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values('Date')

    # Create plots
    plots = [
        create_transaction_balance_plot(data),
        create_credits_debits_bar_chart(data),
        create_transaction_types_pie_chart(data),
        create_cumulative_credits_debits_chart(data)
    ]
    for plot in plots:
        plotGraphs(plot)

    
def on_drop(file_path):
    if file_path.endswith('.csv') or file_path.endswith('.CSV'):
        root.destroy()
        process_csv(file_path=file_path)



root = tk.Tk()
root.title("CSV File Selection")
root.geometry("400x250")

drop_area = tk.Label(root, text="Drag and Drop CSV File Here \n (Not yet activated)", bg="lightgray", height=5)
drop_area.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

file_label = tk.Label(root, text="No file selected")
file_label.pack(pady=10)

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        on_drop(file_path)

browse_button = tk.Button(root, text="Browse Files", command=browse_file)
browse_button.pack(pady=10)

root.mainloop()