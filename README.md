# Switching Hybrid Recommender System

This project implements a hybrid movie recommendation system that combines content-based filtering using Naive Bayes with item-based collaborative filtering. A dynamic switching strategy selects the best method based on model confidence.

## Project Overview

The system is designed to replicate and extend the methodology from the paper  
**"An Improved Switching Hybrid Recommender System Using Naive Bayes Classifier and Collaborative Filtering"**.

### Content-Based Filtering
- Applies TF-IDF to movie metadata and user tags
- Uses a Multinomial Naive Bayes classifier to predict user-item ratings

### Collaborative Filtering
- Item-based filtering using cosine similarity
- Significance weighting is applied to improve prediction quality

### Switching Strategy
- Chooses the method (Naive Bayes or CF) based on prediction confidence
- Includes logic for handling ties and fallback cases

## Evaluation Results

| Metric                | Value    |
|-----------------------|----------|
| Mean Absolute Error   | 0.8213   |
| ROC AUC Score         | 0.8285   |
| Coverage              | 100%     |

## Files Included

- `algorithm.ipynb`: Full implementation of the hybrid recommendation pipeline
- `ratings.csv`, `ratings_pre.csv`: Collaborative filtering input data
- `items_post.csv`, `tags.csv`: Content and tag metadata
- `setup.py`: Installs all necessary Python dependencies and downloads NLTK stopwords

## Requirements

- Python 3.8+
- Required packages: `pandas`, `numpy`, `scikit-learn`, `nltk`, `tqdm`

To install all dependencies automatically:
```bash
python setup.py
