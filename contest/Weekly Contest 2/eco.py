import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Sample product data
product_data = {
    'product_id': [1, 2, 3, 4, 5],
    'name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'description': ['Description A', 'Description B', 'Description C', 'Description D', 'Description E']
}

# Sample user purchase history
user_history = {
    'user_id': [1, 1, 2, 2, 3],
    'product_id': [1, 2, 3, 4, 5]
}

# Create dataframes
products_df = pd.DataFrame(product_data)
user_history_df = pd.DataFrame(user_history)

# Initialize CountVectorizer to convert text data to vectors
vectorizer = CountVectorizer()

# Fit and transform product descriptions
product_descriptions = vectorizer.fit_transform(products_df['description'])

# Compute similarity matrix based on product descriptions
similarity_matrix = cosine_similarity(product_descriptions)

# Function to recommend products to a user
def recommend_products(user_id, num_recommendations=3):
    user_products = user_history_df[user_history_df['user_id'] == user_id]['product_id'].values
    recommended_products = []

    for product_id in user_products:
        similar_products = similarity_matrix[product_id - 1].argsort()[::-1][1:]  # Exclude itself
        for similar_product_id in similar_products:
            if similar_product_id + 1 not in user_products and similar_product_id + 1 not in recommended_products:
                recommended_products.append(similar_product_id + 1)
            if len(recommended_products) >= num_recommendations:
                break
        if len(recommended_products) >= num_recommendations:
            break

    return recommended_products

# Example usage
user_id = 1
recommendations = recommend_products(user_id)
print("Recommended products for user", user_id, ":", recommendations)
