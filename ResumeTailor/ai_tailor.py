import openai
import os
from dotenv import load_dotenv

#SOURCE 1 Had issue with credit limit to pay $5: https://www.youtube.com/watch?v=rv6iMSw5uSQ
#Source 2 Toke Issue : https://community.openai.com/t/struggling-with-max-tokens-and-getting-responses-within-a-given-limit-please-help/456314
#Source 3 Imports: https://stackoverflow.com/questions/75774873/openai-api-error-this-is-a-chat-model-and-not-supported-in-the-v1-completions

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY") #from the file .env 
def generate_tailored_resume(resume_text, job_desc):
    try:
        prompt = (
            "You are a professional resume editor. You will NOT invent or hallucinate any new jobs, projects, or qualifications. "
            "Your job is to reword, reorganize, or emphasize the existing content in the resume to better align with the job description. "
            "Do not add companies, positions, dates, or technologies not present in the original resume. "
            "Do not add any hypothetical experience or courses. "
            "Do not repeat the entire resume in a 'Tailored Resume:' heading or duplicate content. "
            "Output only the improved resume. Begin with the person's name and contact info, then proceed with tailored sections.\n\n"
            f"Job Description:\n{job_desc}\n\n"
            f"Original Resume:\n{resume_text}\n\n"
            "Output:"
        )


      #Source 4: Setting Up this section of the project I used openAI platforms
                #https://platform.openai.com/docs/guides/text?api-mode=responses

        response = openai.ChatCompletion.create(
            model="gpt-4",  
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4, 
            max_tokens=1500,
        )

        return response['choices'][0]['message']['content'].strip()

    except Exception:
        print("ERROR  is from ai_tailor.py file:")
        import traceback
        traceback.print_exc()
        return "There was an error tailoring the resume."
