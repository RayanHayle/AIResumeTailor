#SOURCE 1: https://pypi.org/project/pymupdf4llm/
#SOURCE 2: https://pymupdf.readthedocs.io/en/latest/tutorial.html

from flask import Flask, render_template, request,send_from_directory
import fitz # PyMuPDF package for extracting the text from PDF file
import os

from ai_tailor import generate_tailored_resume  # import ai_tailor.py 
from ai_extract_pdf import save_tailored_text_as_pdf #import ai_extract_pdf.py

#1. place uploads into this dir
UPLOAD_FOLDER = 'uploads/'
DOWNLOAD_FOLDER = 'downloads/'

server = Flask(__name__)
server.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
server.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER  

@server.route('/')
def home(): 
    #2. the home page first return
    return render_template('home.html')

@server.route('/upload', methods=['GET', 'POST'])
def upload(): 
    #3. EXTRACTION TIME
    resume_text = None
    job_desc = None
    tailored_resume = None 

    if request.method == 'POST': 
        resume = request.files.get('resume') 
        job_desc = request.form.get('jobdesc')

        #SOURCE 3: https://www.youtube.com/watch?v=w2r2Bg42UPY instead of image its pdf
        if resume and resume.filename.endswith('.pdf'): 
            #will allow only .pdf to be selected 
            filepath = os.path.join(server.config['UPLOAD_FOLDER'], resume.filename) # add to /uploads 
            resume.save(filepath) 

            # Extract text from PDF from /uploads 
            pdf = fitz.open(filepath) 
            resume_text = "" 
            for word in pdf: 
                resume_text += word.get_text()
                
        #---------PART 3: AI ------
            # 4. call the AI tailoring function from ai_tailor.py
            tailored_resume = generate_tailored_resume(resume_text, job_desc)

        #5. pass the tailored_resume to  ai_extract_pdf.py  and save it in DOWNLOAD_FOLDER
        if tailored_resume:
            save_tailored_text_as_pdf(tailored_resume, folder=server.config['DOWNLOAD_FOLDER'])
                    

    return render_template('resume_upload.html', resume_text=resume_text, job_desc=job_desc, tailored_resume=tailored_resume)


# 6. Serve the tailored resume file from the /downloads folder for download
@server.route('/download')
def download_pdf():
    return send_from_directory(directory=DOWNLOAD_FOLDER, path="tailored_resume.pdf", as_attachment=True)
    #the downloaded file will be titled tailored_resume.pdf

if __name__ == '__main__': 
    server.run(debug=True)
