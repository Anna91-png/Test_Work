from collections import defaultdict

def generate(data):
    brand_ratings = defaultdict(list)
    for row in data:
        brand = row['brand'].strip().lower()
        try:
            rating = float(row['rating'])
            brand_ratings[brand].append(rating)
        except ValueError:
            continue

    result = []
    for brand, ratings in brand_ratings.items():
        avg = round(sum(ratings) / len(ratings), 2)
        result.append({'brand': brand, 'average_rating': avg})

    return sorted(result, key=lambda x: x['average_rating'], reverse=True)
