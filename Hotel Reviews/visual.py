
import matplotlib.pyplot as plt
from matplotlib import animation
from collections import Counter
import json

def show_visualizations(choice, data):
    if choice == '1':
        show_pie_chart(data)
    elif choice == '2':
        show_reviews_by_nationality(data)
    elif choice == '3':
        animate_reviews_trend(data)

def show_pie_chart(data, hotel_name):
    # Filtering data for the specified hotel
    hotel_reviews = [review for review in data if review['Hotel_Name'] == hotel_name]

    # Counting positive and negative reviews
    positive = sum(review['Positive_Review'] != 'No Positive' for review in hotel_reviews)
    negative = sum(review['Negative_Review'] != 'No Negative' for review in hotel_reviews)

    # Plotting
    labels = 'Positive Reviews', 'Negative Reviews'
    sizes = [positive, negative]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle
    plt.title(f"Review Sentiment for {hotel_name}")
    plt.show()

def show_reviews_by_nationality(data):
    # Counting reviews by nationality
    nationality_counts = Counter(review['Reviewer_Nationality'] for review in data)

    # Sorting and selecting top 15 nationalities
    top_nationalities = dict(nationality_counts.most_common(15))

    # Plotting
    plt.bar(top_nationalities.keys(), top_nationalities.values())
    plt.xlabel('Nationality')
    plt.ylabel('Number of Reviews')
    plt.xticks(rotation=45)
    plt.title('Number of Reviews by Nationality')
    plt.tight_layout()
    plt.show()


def animate_reviews_trend(data):
    # Preparing data for animation
    review_dates = [review['Review_Date'] for review in data]
    date_counts = Counter(review_dates)

    dates = list(date_counts.keys())
    counts = list(date_counts.values())

    fig, ax = plt.subplots()

    def animate(i):
        ax.clear()
        ax.bar(dates[:i], counts[:i])
        ax.set_xlabel('Date')
        ax.set_ylabel('Number of Reviews')
        ax.set_title('Number of Reviews Over Time')

    ani = animation.FuncAnimation(fig, animate, frames=len(dates), repeat=False)
    plt.show()