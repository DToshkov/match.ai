# Re-import necessary modules after code execution environment reset
import pandas as pd

# Sample data for mentors and mentees
mentors_data = {
    'name': ['Alice Johnson', 'Bob Smith', 'Carol White'],
    'university': ['UCLA', 'MIT', 'Harvard'],
    'hobbies': ['hiking', 'reading', 'photography'],
    'outside_role': ['DEI committee member', 'Toastmasters lead', 'CSR volunteer'],
    'home_hub': ['Chicago', 'New York', 'Boston'],
    'current_function': ['Engineering', 'Marketing', 'Data Science']
}

mentees_data = {
    'name': ['Dan Lee', 'Eva Brown', 'Frank Moore'],
    'university': ['MIT', 'UCLA', 'Stanford'],
    'hobbies': ['reading', 'hiking', 'gaming'],
    'outside_role': ['Toastmasters member', 'DEI participant', 'Open source contributor'],
    'home_hub': ['New York', 'Chicago', 'Boston'],
    'current_function': ['Marketing', 'Engineering', 'Product Management']
}

# Convert to DataFrames
mentors_df = pd.DataFrame(mentors_data)
mentees_df = pd.DataFrame(mentees_data)

# Save to Excel
mentors_path = "/mnt/data/mentors_sample.xlsx"
mentees_path = "/mnt/data/mentees_sample.xlsx"

mentors_df.to_excel(mentors_path, index=False)
mentees_df.to_excel(mentees_path, index=False)

mentors_path, mentees_path
