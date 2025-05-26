# Project: Final Presentation 
An AI-powered website that allows users to upload a resume. 

This will give users the ability to use AI to tailor their resume in accordance with the job description.

## Part 1: Receive Resume, Description

1.  The HTML form provides a file input field so the user can select a file. ✅
2.  When the user clicks "Submit," on the resume and description: ✅
	- Flask receives the uploaded file and description ✅
3.  Extracts text from the PDF (pip install pymupdf) ✅
4.  User Interface complete (website) ✅

## Part 2: Set Up AI Prompt 
1. Setting up the environment ✅
2. Install the OpenAI library → `pip install openai` ✅
3. Set up OpenAI API key ✅
4. Flask retrieves both the job description and the resume ✅

## Part 3: AI Response 
1. Structure Prompt for AI:
	-  Combine both the job description and resume into a **single string** to send to AI✅
		- Had to add credit card to use the open api
2. AI provides response (the tailored resume)✅
3. Generate PDF from tailored resume using  ReportLab✅
4. Allow user to directly download the tailored resume (Currently there is a button)✅
5. Fixed User Interface design ✅

## Summary
- Under static/images I provided images of the project to preview 
- under uploads you will see orginal resume
- under downloads you will see tailored resume 

- If you want to test give this description and use  the file under /uploads: 

  `Change the name to rayan hayle, and email to rah2236@gmail.com, and EDUCATION to Columbia College, Columbia University don't add LinkedIn and github in the top`
