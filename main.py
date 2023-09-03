import streamlit as st

# Function to calculate marks required for each subject
def calculate_required_marks(desired_percentage, current_data):
    required_marks = {}

    total_current_marks = sum(current_data.values())
    total_required_marks = desired_percentage * 15 - total_current_marks

    if total_required_marks <= 0:
        return required_marks, total_required_marks

    num_subjects = len(current_data)
    marks_per_subject = total_required_marks / num_subjects

    for subject in current_data.keys():
        required_marks[subject] = current_data[subject] + marks_per_subject

    return required_marks, total_required_marks

# Main Streamlit app
def main():
    st.title("Marks Calculation App")

    # Input received scores
    st.header("Input Current Scores")
    current_scores = {}

    for subject in subjects:
        current_scores[subject] = st.number_input(f"Received Score for {subject} (out of 150):", min_value=0, max_value=150, value=0)

    # Input desired overall percentage
    st.header("Input Desired Overall Percentage")
    desired_percentage = st.slider("Desired Overall Percentage:", 0, 100, 0)

    # Calculate required marks and display the table
    required_marks, remaining_marks = calculate_required_marks(desired_percentage, current_scores)

    st.header("Marks Required for Desired Percentage")

    table_data = []

    for subject, current_marks in current_scores.items():
        required_mark = required_marks.get(subject, 0)
        maximum_marks = 150
        obtainable_marks = abs(current_marks - maximum_marks)
        table_data.append([subject, current_marks, obtainable_marks, required_mark, maximum_marks])

    # Create a table using Markdown formatting
    table_str = "| Subject | Current Marks | Obtainable Marks | Required Marks | Maximum Marks |\n"
    table_str += "| --- | --- | --- | --- | --- |\n"

    for row in table_data:
        table_str += f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} |\n"

    st.write(table_str, unsafe_allow_html=True)

    # Display custom error message if total marks exceed the maximum limit
    if sum(current_scores.values()) + sum(required_marks.values()) > 1500:
        st.error("What's the use of trying? All you get is pain.")

# List of subjects (used for calculations)
subjects = [
    "English Grammar", "English Literature", "2nd Language",
    "Math", "Physics", "Chemistry", "Biology",
    "History", "Geography", "Optional"
]

if __name__ == "__main__":
    main()


    