import pandas as pd

from preprocess import clean_text
from vectorize import vectorize_text
from similarity import compute_similarity

# 1️⃣ Load resumes
df = pd.read_csv("../data/resumes.csv")

# 2️⃣ Load job description
with open("../data/job_description.txt", "r") as file:
    job_description = file.read()

# 3️⃣ Clean text
df["clean_resume"] = df["Resume"].apply(clean_text)
clean_jd = clean_text(job_description)

# 4️⃣ TF-IDF Vectorization
resume_vectors, jd_vector = vectorize_text(
    df["clean_resume"], clean_jd
)

# 5️⃣ Similarity calculation
df["match_score"] = compute_similarity(resume_vectors, jd_vector)
df["match_percentage"] = df["match_score"] * 100

# 6️⃣ Show top 5 resumes
top = df.sort_values(by="match_percentage", ascending=False).head(5)

print("\nTOP MATCHING RESUMES\n")

for i in range(len(top)):
    print(f"Candidate {i+1}")
    print("Category:", top.iloc[i]["Category"])
    print("Match Score:", round(top.iloc[i]["match_percentage"], 2), "%")
    print("-" * 40)
