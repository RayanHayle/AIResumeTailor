from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import textwrap


def save_tailored_text_as_pdf(text, filename="tailored_resume.pdf", folder="downloads"):

    path_to_save = os.path.join(folder, filename)

    # Source 1 for formatting and saving to downloads: https://stackoverflow.com/questions/51740145/how-can-i-write-text-to-pdf-file
    # Source 2 setting font of the pdf: https://stackoverflow.com/questions/32485353/python-reportlab-save-with-canvas-to-specified-location
    
    pdf_canvas = canvas.Canvas(path_to_save, pagesize=letter)
    page_width, page_height = letter

    page_margin = 50
    line_spacing = 12  
    current_line = page_height - page_margin 

    pdf_canvas.setFont("Times-Roman", 11)  

    # -----------------------------------------
    ## Source 3 for drawString,showPage,setFont: https://docs.reportlab.com/reportlab/userguide/ch2_graphics/
    # Source 4 for textwrap: https://note.nkmk.me/en/python-textwrap-wrap-fill-shorten/

    for paragraph in text.split("\n"):# first split the text by new line
        
        wrapped_lines = textwrap.wrap(paragraph, width=90)  #each paragraph will only have 90 chars per line

        for line in wrapped_lines:
            line = line.replace("●", "•")  # to look better and not chunky  

            if current_line - line_spacing < page_margin:
                pdf_canvas.showPage()  # move to a new page when out of space. Current issue is the new tailored will have 2 pages but best it can do

                pdf_canvas.setFont("Times-Roman", 11)  #reset the font to the next page else it set something else to be default 

                current_line = page_height - page_margin  # reset to the top of the new page

            pdf_canvas.drawString(page_margin, current_line, line) # write the chars (line) at current  position (current_line), starting from the left margin (page_margin)
            
            current_line -= line_spacing  

        current_line -= line_spacing  # adds spacing between the lines else it will be 1.0 spacing, however it'll result in more pages 
 
    pdf_canvas.save()  
    return path_to_save
