import streamlit as st

# Title of the app
st.title("Semester GPA/CGPA Calculator")
# Sidebar for user input
with st.sidebar:
    st.write("Select the calculation method.")
    calculation_method = st.radio("Calculation Method", ["GPA", "CGPA"])

    if calculation_method == "GPA":
        st.write("Select the semester for which you want to calculate GPA.")
        semester = st.selectbox("Semester", ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5"])

        if semester == "Semester 1":
            st.write("You have selected Semester 1.")
            #st.write("Use the following scale:")
            #st.write("O = 10, A+ = 9, A = 8, B+ = 7, B = 6, U = 0")
            #st.write("Credits are fixed for each subject as per the description.")
            st.write("Please enter your grades for each subject.")

            # Create input fields for each subject
            subjects = [
                ("BS3171-PHYSICS AND CHEMISTRY LABORATORY", 2),
                ("CY3151-ENGINEERING CHEMISTRY", 3),
                ("GE3151-PROBLEM SOLVING AND PYTHON PROGRAMMING", 3),
                ("GE3171-PROBLEM SOLVING AND PYTHON PROGRAMMING LABORATORY", 2),
                ("HS3151-PROFESSIONAL ENGLISH -1", 3),
                ("MA3151-MATRICES AND CALCULUS", 4),
                ("PH3151-ENGINEERING PHYSICS", 3),
            ]
            grades = []
            for subject, credits in subjects:
                grade = st.text_input(f"{subject} Grade")
                grades.append((grade, credits))

        elif semester == "Semester 2":
            st.write("You have selected Semester 2.")
            st.write("Please enter your grades for each subject.")

            # Create input fields for each subject
            subjects = [
                ("BS3251-BEEE", 3),
                ("CS3251-PROGRAMMING IN C", 3),
                ("CS3271-PROGRAMMING IN C LABORATORY", 2),
                ("GE3251-ENGINEERING GRAPHICS", 4),
                ("GE3271-ENGINEERING PRACTICES LABORATORY", 2),
                ("HS3251-PROFESSIONAL ENGLISH -II", 2),
                ("MA3251-SNM", 4),
                ("PH3256-PHYSICS FOR INFORMATION SCIENCE", 3),
            ]
            grades = []
            for subject, credits in subjects:
                grade = st.text_input(f"{subject} Grade")
                grades.append((grade, credits))

        elif semester == "Semester 3":
            st.write("You have selected Semester 3.")
            st.write("Please enter your grades for each subject.")

            # Create input fields for each subject
            subjects = [
                ("MA3354-Discrete Mathematics", 4),
                ("CS3351-Digital Principles and Computer Organization", 4),
                ("CS3352-Foundations of Data Science", 3),
                ("CS3301-Data Structures", 3),
                ("CS3391-Object Oriented Programming", 3),
                ("CS3311-Data Structures Laboratory", 1.5),
                ("CS3381-Object Oriented Programming Laboratory", 1.5),
                ("CS3361-Data Science Laboratory", 2),
                ("GE3361-Professional Development", 1),
            ]
            grades = []
            for subject, credits in subjects:
                grade = st.text_input(f"{subject} Grade")
                grades.append((grade, credits))

        elif semester == "Semester 4":
            st.write("You have selected Semester 4.")
            st.write("Please enter your grades for each subject.")

            # Create input fields for each subject
            subjects = [
                ("CS3452-Theory of Computation", 3),
                ("CS3491-Artificial Intelligence and Machine Learning", 4),
                ("CS3492-Database Management Systems", 3),
                ("CS3401-Algorithms", 4),
                ("CS3451-Introduction to Operating Systems", 3),
                ("GE3451-Environmental Sciences and Sustainability", 2),
                ("CS3461-Operating Systems Laboratory", 1.5),
                ("CS3481-Database Management Systems Laboratory", 1.5),
                ("SB8021-Professional Development-II", 1),
            ]
            grades = []
            for subject, credits in subjects:
                grade = st.text_input(f"{subject} Grade")
                grades.append((grade, credits))

        elif semester == "Semester 5":
            st.write("You have selected Semester 5.")
            st.write("Please enter your grades for each subject.")

            # Create input fields for each subject
            subjects = [
                ("Compiler Design", 3),
                ("Computer Network", 4),
                ("Distributed Systems", 3),
                ("Cryptography", 4),
                ("Cloud Computing/Web/BDA", 3),
                ("Virtualization/UIUX/EDA", 3),
                ("Project Based Learning", 2),
            ]
            grades = []
            for subject, credits in subjects:
                grade = st.text_input(f"{subject} Grade")
                grades.append((grade, credits))

        # Add a submit button
        if st.button("Submit"):
            # Calculate GPA
            total_credits = 0
            total_grade_points = 0
            for grade, credits in grades:
                if grade.upper() == "O":
                    grade_points = 10.0
                elif grade.upper() == "A+":
                    grade_points = 9.0
                elif grade.upper() == "A":
                    grade_points = 8.0
                elif grade.upper() == "B+":
                    grade_points = 7.0
                elif grade.upper() == "B":
                    grade_points = 6.0
                elif grade.upper() == "U":
                    grade_points = 0.0
                else:
                    try:
                        grade_points = float(grade)  # Convert the grade to a float
                    except ValueError:
                        grade_points = 0.0

                total_credits += credits
                total_grade_points += grade_points * credits

            if total_credits > 0:
                gpa = total_grade_points / total_credits
                st.write(f"Your GPA for {semester} is {gpa:.2f}")
            else:
                st.write(f"Please enter your grades for each subject in {semester}.")

    elif calculation_method == "CGPA":
        st.write("You have selected CGPA.")
        st.write("Please enter your GPA for each semester.")

        # Create input fields for each semester
        semesters = ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5"]
        gpas = []
        for semester in semesters:
            gpa = st.text_input(f"GPA for {semester}")
            try:
                gpas.append(float(gpa))
            except ValueError:
                pass

        # Check if the list of GPAs is empty
        if len(gpas) == 0:
            st.write("Please enter at least one GPA for calculation.")
        else:
            # Add a submit button
            if st.button("Submit"):
                # Calculate CGPA
                total_gpa = sum(gpas)
                cgpa = total_gpa / len(gpas)
                st.write(f"Your CGPA is {cgpa:.2f}")

