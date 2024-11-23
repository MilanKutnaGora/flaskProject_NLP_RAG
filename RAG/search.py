import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from flask import Flask, request, jsonify


app = Flask(__name__)

# Загрузка данных из файла (например, reviews.csv)
data = pd.read_csv('../reviews.csv')
reviews = data['review'].tolist()

# Создание TF-IDF векторайзера и преобразование текстов в векторы
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(reviews)


@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '')
    query_vec = vectorizer.transform([query])

    # Вычисление косинусного сходства
    cosine_similarities = linear_kernel(query_vec, tfidf_matrix).flatten()

    # Получение индексов трех наиболее релевантных отзывов
    top_indices = cosine_similarities.argsort()[-3:][::-1]

    # Возвращаем топ-3 результата
    top_reviews = [reviews[i] for i in top_indices]

    return jsonify(top_reviews)


if __name__ == '__main__':
    app.run(port=5001, debug=True)