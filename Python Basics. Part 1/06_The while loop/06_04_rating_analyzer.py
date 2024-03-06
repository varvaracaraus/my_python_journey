# Rating Analyzer
# This script collects a specified number of reviews (ratings) and categorizes them into 
# positive, negative, and zero ratings. It then outputs the count of each category.

# Input for the number of reviews
total_reviews = int(input('Enter the number of reviews: '))

# Initialize counters for each rating category
positive_ratings_count = 0
negative_ratings_count = 0
zero_ratings_count = 0

# Collect and categorize each review
for _ in range(total_reviews):
    rating = int(input('Enter a rating from -100 to 100: '))
    if rating > 0:
        positive_ratings_count += 1
    elif rating < 0:
        negative_ratings_count += 1
    else:
        zero_ratings_count += 1

# Print the counts of each rating category
print('Number of positive ratings:', positive_ratings_count)
print('Number of negative ratings:', negative_ratings_count)
print('Number of zero ratings:', zero_ratings_count)
