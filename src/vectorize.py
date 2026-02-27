from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_text(resumes, job_description):
    vectorizer = TfidfVectorizer(max_features=3000)
    resume_vectors = vectorizer.fit_transform(resumes)
    jd_vector = vectorizer.transform([job_description])
    return resume_vectors, jd_vector
