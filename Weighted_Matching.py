import pandas as pd

# Load the dataset into a pandas DataFrame
df = pd.read_csv("E:\Hack\dataset_back.csv")

# Define the required skill sets with weights
required_skills = {
    'SEO': 3,
    'SQL': 2,
    'HTML': 4
}
# Create a new column to store the matching score
df['matching_score'] = 0

# Iterate over each employee
for index, row in df.iterrows():
    employee_skills = eval(row['Skill Set Needed'])
    matching_score = sum(required_skills.get(skill, 0) for skill in employee_skills)
    df.at[index, 'matching_score'] = matching_score

# Create a new DataFrame with only the matching score column
matching_score_df = df[['matching_score']]

# Save the DataFrame as a CSV file
matching_score_df.to_csv('matching_scores.csv', index=False)