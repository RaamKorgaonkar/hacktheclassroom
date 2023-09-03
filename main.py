import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# List of subjects
subjects = [
    "English Grammar", "English Literature", "2nd Language",
    "Math", "Physics", "Chemistry", "Biology",
    "History", "Geography", "Optional"
]

# Function to calculate the total marks for a subject
def calculate_total_marks(assignments, unit_test, term_exam):
    total_marks = assignments + unit_test + term_exam
    return total_marks

# Function to input marks for a subject with sliders
def input_subject_marks(subject_name):
    st.subheader(f"Enter marks for {subject_name}:")

    # Input validation for assignments
    assignments = st.slider(f"Marks for Assignments (out of 30) for {subject_name}:", 0, 30, 0)

    # Input validation for unit test
    unit_test = st.slider(f"Marks for Unit Test (out of 40) for {subject_name}:", 0, 40, 0)

    # Input validation for term exam
    term_exam = st.slider(f"Marks for Term Exam (out of 80) for {subject_name}:", 0, 80, 0)

    return {
"Assignments": assignments,
"Unit Test": unit_test,
"Term Exam": term_exam,
"Marks Scored": calculate_total_marks(assignments, unit_test, term_exam),
"Maximum Marks": 150  # Assuming maximum marks for each component are constant
}

# Function to calculate the percentage for one subject
def calculate_subject_percentage(subject_marks):
    return (subject_marks["Marks Scored"] / subject_marks["Maximum Marks"]) * 100

# Initialize a dictionary to store subject-wise marks
report_card = {}

# Create a single form to submit all the subject marks
with st.form("subject_marks_form"):
    for subject in subjects:
        report_card[subject] = input_subject_marks(subject)

    # Center-align the submit button
    st.write("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.form_submit_button(label="Submit Marks", help="Click to submit the marks")
    st.write("</div>", unsafe_allow_html=True)

# Calculate the percentage for each subject
for subject in subjects:
    report_card[subject]["Percentage"] = calculate_subject_percentage(report_card[subject])

# Input remarks within the Streamlit app
st.subheader("Enter Remarks:")
remarks = st.text_area("", key="remarks")

# Generate the report card on a new page
if st.button("Generate Report Card"):
    st.title("Report Card")
    st.markdown("---")

    # Create a DataFrame for the report card table
    report_card_df = pd.DataFrame(report_card)
    report_card_df = report_card_df.T.reset_index()
    report_card_df.columns = ["Subject", "Assignments", "Unit Test", "Term Exam", "Marks Scored", "Maximum Marks", "Percentage"]

    # Display the student information and report card table

    st.markdown("---")

    st.subheader("")
    st.dataframe(report_card_df.style.format({"Percentage": "{:.2f}%"}), height=400)
    st.markdown("---")

    # Create bar charts for marks scored in each subject
    plt.figure(figsize=(10, 6))
    plt.barh(report_card_df["Subject"], report_card_df["Marks Scored"], color='skyblue')
    plt.xlabel('Marks Scored')
    plt.ylabel('Subjects')
    plt.title('Marks Scored in Each Subject')
    plt.gca().invert_yaxis()  # Reverse the order of subjects
    plt.tight_layout()

    # Save the bar chart as an image
    plt.savefig('marks_chart.png')

    # Display the graph below the table
    st.pyplot(plt)

    # Display total marks and percentage
    st.subheader("Total Marks and Percentage")
    total_marks = report_card_df["Marks Scored"].sum()
    percentage = (total_marks / (1500 * len(subjects))) * 100
    st.write(f"Total Marks: {total_marks} / 1500")
    st.write(f"Percentage: {total_marks/15}%")
    st.markdown("---")

    # Display Remarks
    st.subheader("Remarks")
    st.write(remarks)
    