import google.generativeai as genai
import os

def gemini_text_service_call(input_prompt):
    genai.configure(api_key="#") 
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content(input_prompt)
    return response.text


input_prompt = "Write a story about a magic backpack."
output_text = gemini_text_service_call(input_prompt)
print(output_text)