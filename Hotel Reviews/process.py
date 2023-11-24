
import csv
from datetime import datetime
from collections import defaultdict

def load_reviews(file_path: str):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        reviews = list(reader)
    return reviews

def process_data(reviews_data, choice, user_input=None):
    if choice == '1':
        return len(reviews_data)
    elif choice == '2':
        return [review for review in reviews_data if review['Hotel_Name'] == user_input]
    elif choice == '3':
        dates = user_input.split(' - ')
        if len(dates) == 1:
            start_date = end_date = datetime.strptime(dates[0], '%m/%d/%Y')
        elif len(dates) == 2:
            start_date, end_date = map(lambda x: datetime.strptime(x, '%m/%d/%Y'), dates)
        else:
            raise ValueError("Invalid date input")
        return [review for review in reviews_data if start_date <= datetime.strptime(review['Review_Date'], '%m/%d/%Y') <= end_date]
    elif choice == '4':
        nationality_groups = defaultdict(list)
        for review in reviews_data:
            nationality_groups[review['Reviewer_Nationality']].append(review)
        return dict(nationality_groups)
    elif choice == '5':
        summary = defaultdict(lambda: {'negative': 0, 'positive': 0, 'average_rating': 0, 'count': 0})
        for review in reviews_data:
            date = review['Review_Date']
            summary[date]['negative'] += int(review['Negative_Review'] != 'No Negative')
            summary[date]['positive'] += int(review['Positive_Review'] != 'No Positive')
            summary[date]['average_rating'] += float(review['Reviewer_Score'])
            summary[date]['count'] += 1
        for date, data in summary.items():
            data['average_rating'] /= data['count']
        return dict(sorted(summary.items(), key=lambda x: datetime.strptime(x[0], '%m/%d/%Y')))
