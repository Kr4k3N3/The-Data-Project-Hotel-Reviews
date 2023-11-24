
# tui.py
import process

def welcome_message():
    title = "Hotel Reviews Analysis"
    dashes = "-" * len(title)
    print(f"\n{dashes}\n{title}\n{dashes}")

def error_message(msg):
    print(f"Error! {msg}.")

def progress_message(operation, value):
    status = ("initiated" if value == 0 else 
              f"in progress ({value}% completed)" if 0 < value < 100 else 
              "completed")
    print(f"Operation: {operation} [{status}].")

def main_menu():
    print("\nMain Menu:")
    print("[1] Load Data")
    print("[2] Process Data")
    print("[3] Visualize Data")
    print("[4] Export Data")
    print("[5] Exit")

def process_data_menu():
    print("\nProcess Data Menu:")
    print("[1] Retrieve Total Number of Reviews")
    print("[2] Retrieve Reviews by Hotel")
    print("[3] Retrieve Reviews by Date")
    print("[4] Retrieve Reviews by Nationality")
    print("[5] Retrieve Summary of Reviews")
    print("[6] Return to Main Menu")

def visualize_data_menu():
    print("\nVisualize Data Menu:")
    print("[1] Pie Chart for a Hotel")
    print("[2] Reviews by Nationality")
    print("[3] Animated Reviews Trend")
    print("[4] Return to Main Menu")

def export_data_menu():
    print("\nExport Data Menu:")
    print("[1] Export All Reviews")
    print("[2] Export Reviews for a Specific Hotel")
    print("[3] Return to Main Menu")

def total_reviews(count):
    print(f"Total Reviews Processed: {count}")

def review_summary(summary):
    print("Review Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")
