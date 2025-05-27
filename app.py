import random
import streamlit as st
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file_path):
    """Extract text from a PDF file using PyMuPDF."""
    """It generally define an function that opens PDF and Extracts all the texts from Every page into a single string"""
    doc = fitz.open(pdf_file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Example function to generate MCQs from PDF
def generate_mcq_questions_and_answers_from_pdf(pdf_file_path, difficulty_level, num_questions):
    """Generate MCQ questions from a PDF file."""
    text = extract_text_from_pdf(pdf_file_path)
    if not text:
        raise ValueError("No valid text extracted from the PDF.")
    
    # Process the text (Example, split by lines, you can replace with actual logic)
    possible_questions = text.split('\n')
    
    # Check if we have enough questions
    if len(possible_questions) < num_questions:
        raise ValueError(f"Not enough questions available. Available: {len(possible_questions)}, Requested: {num_questions}")
    
    # Randomly sample the questions
    selected_questions = random.sample(possible_questions, num_questions)
    
    # Generate answers (this is placeholder logic for now)
    # Make sure to generate the answers in a tuple format: (question, answer)
    questions_with_answers = [(q, "Answer") for q in selected_questions]
    
    # Now, return questions and key_answers separately as required
    questions = [q for q, _ in questions_with_answers]  # Extract just the questions
    key_answers = [answer for _, answer in questions_with_answers]  # Extract answers
    
    return questions, key_answers


# Streamlit interface
# This defines the main functions that runs your streamlit app.
# it sets up the UI and logic to generate MCQs fomr a pdf file.
def main():
    st.title("MCQ Quiz Generator from PDF") # Displays the main title of the web app on the page using Streamlit.
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    # uploaded_file.name gets the filename, this is for the below code 
    # getbuffer() reads the file content
    # It is then written to a new file locally using wb (write binary mode).
    if uploaded_file is not None:
        pdf_file_path = uploaded_file.name
        with open(pdf_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Parameters (You can make these inputs dynamic from the UI)
        difficulty_level = st.selectbox("Select difficulty", ["Easy", "Medium", "Hard"])
        num_questions = st.slider("Number of questions", 1, 10, 5)
        
        try:
            questions, key_answers = generate_mcq_questions_and_answers_from_pdf(pdf_file_path, difficulty_level, num_questions)
            st.write("Generated Questions:")
            for i, question in enumerate(questions, 1):
                st.write(f"{i}. {question}")
            st.write("Correct Answers:")
            for i, answer in enumerate(key_answers, 1):
                st.write(f"{i}. {answer}")
        
        except ValueError as e:
            st.error(str(e))


if __name__ == "__main__":
    main()
