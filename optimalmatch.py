import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.optimize import linear_sum_assignment

# Load Data
mentors = pd.read_excel('mentors.xlsx', engine='openpyxl')
mantees = pd.read_excel('mantees.xlsx', engine='openpyxl')

# Define Weights
WEIGHTS = {
    'university': 0.2,
    'hobbies': 0.1,
    'outside_role': 0.25,
    'proximity': 0.35,
    'key_interests': 0.1
}

# Initiate CountVectorizer globally
vectorizer = CountVectorizer(stop_words='english')

def compute_similarity(str1, str2):
    """Compute cosine similarity between two strings."""
    if pd.isna(str1) or pd.isna(str2):
        return 0.0
    str1, str2 = str(str1).strip(), str(str2).strip()
    if not str1 or not str2:
        return 0.0
    try:
        vectors = vectorizer.fit_transform([str1, str2])
        return cosine_similarity(vectors[0], vectors[1])[0][0]
    except Exception as e:
        print(f"Similarity computation failed: {e}")
        return 0.0

# Initialize the cost matrix
cost_matrix = np.zeros((len(mentors), len(mantees)))

# Populate the cost matrix with negative total scores
for j, mentor in mentors.iterrows():
    for i, mantee in mentees.iterrows():
        university_score = 1.0 if str(mantee['university']).strip().lower() == str(mentor['university']).strip().lower() else 0.0
        hobbies_score = 1.0 if str(mantee['hobbies']).strip().lower() == str(mentor['hobbies']).strip().lower() else 0.0
        proximity_score = 1.0 if str(mantee['home_hub']).strip().lower() == str(mentor['home_hub']).strip().lower() else 0.0
        key_interests_score = 1.0 if str(mantee['current_function']).strip().lower() == str(mentor['current_function']).strip().lower() else 0.0
        outside_role_score = compute_similarity(mantee['outside_role'], mentor['outside_role'])

        total_score = (
            WEIGHTS['university'] * university_score +
            WEIGHTS['hobbies'] * hobbies_score +
            WEIGHTS['proximity'] * proximity_score +
            WEIGHTS['key_interests'] * key_interests_score +
            WEIGHTS['outside_role'] * outside_role_score
        )

        cost_matrix[j, i] = -total_score  # negative for minimization

# Apply Hungarian algorithm
mentor_indices, mantee_indices = linear_sum_assignment(cost_matrix)

# Prepare the results
matches = []
for mentor_idx, mantee_idx in zip(mentor_indices, mantee_indices):
    mentor_name = mentors.iloc[mentor_idx]['name']
    mantee_name = mentees.iloc[mantee_idx]['name']
    matches.append({'Mentor': mentor_name, 'Mantee': mantee_name})

# Save results
match_df = pd.DataFrame(matches)
match_df.to_excel('optimal_mentor_mantee_matches.xlsx', index=False)

print("Optimal matching complete. Results saved to: optimal_mentor_mantee_matches.xlsx")
