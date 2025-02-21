import time
import pywinctl
import psutil
import pandas as pd
#rich module is not necesssary.. it just makes CLI output... You can directly add it to a file.
from rich.console import Console 
from rich.table import Table
from rich.live import Live
import os

CSV_FILE = "time_tracking.csv"

time_spent = {}
current_app = None
start_time = time.time()

console = Console()

def get_active_window_info():
    try:
        window = pywinctl.getActiveWindow()
        if window:
            pid = window.getPID() 
            process_name = psutil.Process(pid).name()
            return process_name
        return None
    except Exception:
        return None

def generate_table():
    table = Table(title="Time Spent Tracker", show_lines=True)
    table.add_column("App", style="cyan", justify="left")
    table.add_column("Time Spent (min)", style="yellow", justify="right")

    for key, seconds in sorted(time_spent.items(), key=lambda x: -x[1]):
        table.add_row(key, f"{seconds / 60:.2f}")

    return table

def save_to_csv():
    data = [{"App": key, "Time Spent (min)": round(seconds / 60, 2)} for key, seconds in time_spent.items()]
    df = pd.DataFrame(data)
#update output filepath here guys
    if not os.path.exists(CSV_FILE):
        df.to_csv(CSV_FILE, index=False)
    else:
        df.to_csv(CSV_FILE, mode='w', index=False)

try:
    with Live(generate_table(), console=console, refresh_per_second=1) as live:
        while True:
            process = get_active_window_info()

            now = time.time()

            if process != current_app:
                elapsed_time = now - start_time
                if current_app:
                    time_spent[current_app] = time_spent.get(current_app, 0) + elapsed_time
                    save_to_csv() 

                current_app = process
                start_time = now

            live.update(generate_table())
            time.sleep(1)  #checks every second

except KeyboardInterrupt:
    console.print("\n[bold red]Tracking stopped.[/bold red] Final time summary:")

    save_to_csv()

    console.print(generate_table())
    console.print(f"\n[green]Data saved to {CSV_FILE}[/green] 📁")
