
from typing import List, Dict
import process
import visual
from tui import (welcome_message, error_message, progress_message, main_menu, 
                 process_data_menu, visualize_data_menu, export_data_menu, total_reviews, review_summary)

FILE_PATH = 'reviews.csv'  # Global variable for file path

def main():
    welcome_message()
    reviews_data = []

    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            try:
                progress_message("Loading reviews data from file...", 0)
                reviews_data = process.load_reviews(FILE_PATH)
                progress_message("Loading reviews data completed", 100)
            except FileNotFoundError as e:
                error_message(f"File not found: {e}")
            except Exception as e:
                error_message(str(e))

        elif choice == '2' and reviews_data:
            process_data(reviews_data)

        elif choice == '3' and reviews_data:
            visualize_data(reviews_data)

        elif choice == '4' and reviews_data:
            export_data(reviews_data)

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

def process_data(reviews_data):
    process_data_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        total = len(reviews_data)  # Directly getting the total number of reviews
        print(f"Total number of reviews: {total}")
    elif choice in ['2', '3', '4', '5']:
        user_input = input("Please enter the required input: ")
        result = process.process_data(reviews_data, choice, user_input)
        # Display the result or handle it as needed
        print(result)
    elif choice == '6':
        return
    else:
        print("Invalid choice.")

def visualize_data(reviews_data):
    visualize_data_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        hotel_name = input("Enter hotel name for pie chart: ")
        visual.show_pie_chart(reviews_data, hotel_name)
    elif choice == '2':
        visual.show_reviews_by_nationality(reviews_data)
    elif choice == '3':
        visual.animate_reviews_trend(reviews_data)
    elif choice == '4':
        return
    else:
        print("Invalid choice.")

import json

def export_data(reviews_data):
    export_data_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        with open('all_reviews.json', 'w') as f:
            json.dump(reviews_data, f)
        print("All reviews exported.")
    elif choice == '2':
        hotel_name = input("Enter hotel name for export: ")
        filtered_data = [review for review in reviews_data if review['Hotel_Name'] == hotel_name]
        with open(f'{hotel_name}_reviews.json', 'w') as f:
            json.dump(filtered_data, f)
        print("Hotel reviews exported.")
    elif choice == '3':
        return
    else:
        print("Invalid choice.")
        
if __name__ == "__main__":
    main()
