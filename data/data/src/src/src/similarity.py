from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_vectors, jd_vector):
    scores = cosine_similarity(resume_vectors, jd_vector)
    return scores.flatten()
