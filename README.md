# <AI-Powered Resume Tailoring Website>

## Project Description
- To get preview go to static/images 

**Goal:**  
An AI powered website that allows users to upload a resume. This will give user the ability to use AI to tailor their resume in accordance with job description

 **Key Feature:** Users will upload a resume (PDF), paste a job description, and generate a tailored resume based on AI's processing of both inputs (Resume, Description).

## Requirements

- **Hardware:**  
  No specific hardware requirements, as this will be a web-based app.
  
- **Software:**
  - **Frontend:** HTML/CSS for building the website and user interface
  -  **Backend:** Python (Flask), JavaScript (User Interface),  OpenAI (for AI processing), SQLAlchemy (storing orginal Resume)

  - **Libraries:**
    - `PyMuPDF` or `pdfminer` for PDF text extraction the input resume 
    - `OpenAI` library for AI to tailor the  resume 
    - `WeasyPrint` or `ReportLab` for PDF generation of the AI reponse
  - **Database:** Python SQLAlchemy for storing the original resumes 
  
- **Hosting:** GitHub for hosting the project.

- **API Keys:** OpenAI API key for AI services.

## Milestones

### Week 1: Resume, Description
**1. Receive Resume:**
- The HTML form provides a file input field so the user can select a file.
- When the user clicks "Submit," the form sends the file to the backend (Flask).
- Flask receives the uploaded file from the frontend to the backend.
- Flask stores the original file in SQL/Python database using SQLAlchemy.
- Flask extracts text from the PDF using pymupdf4llm.

**2. Receive Job Description:**
- Create a form with a textarea where users can paste the job description (faster than PDF).
- When the user clicks "Submit," the form sends the text to Flask.

### Week 2: AI Prompt
**3. Setting up the environment:**
- Install the OpenAI library.
- Set up OpenAI API key.

**4. Structure Prompt for AI:**
- Flask retrieves both the job description and the resume.
- Combine both the job description and resume into a single string to send to AI.

```python
def tailor_resume(resume_text, job_desc_text):
    prompt = f"""
        {job_desc_text}
        {resume_text}
        Tailor the resume to match the job description. .. more clarity 
    """
    return prompt
```
### Week 3: AI Response  
**5. AI Tailors the Resume**
- AI provides response (the tailored resume)
- Generate PDF from tailored resume using WeasyPrint or ReportLab
- Allow user to directly download the tailored resume  
  - Storing it will using great storage space because they will need to use the software multiple times

### Week 4: Website 
- Host the project on GitHub
- Ensure Frontend and Backend efficiency, Complete Appearance and Testing


