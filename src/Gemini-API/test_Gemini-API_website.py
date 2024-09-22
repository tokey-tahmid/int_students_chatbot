import os
import gradio
import google.generativeai as genai

has_started_chat = False
chat = None

def gemini_chat_service_call(input_prompt):
    global has_started_chat, chat
    genai.configure(api_key="#") 
    model = genai.GenerativeModel('gemini-pro')
    training_prompt = "Hello, I'm an international student going to University of Tennessee at Knoxville having trouble understanding the information on this website: https://utkisss.atlassian.net/wiki/spaces/IPFP/pages/20774918/Guides+for+Students. I'll ask specific questions about the content in separate prompts. Can you help me interpret the information and answer my questions?"
    
    if not has_started_chat:
        chat = model.start_chat()
        has_started_chat = True  # Set flag after starting chat

    if len(chat.history) < 2:
        train_response = chat.send_message(training_prompt)
        print(train_response.text)
        response = chat.send_message(input_prompt)
        return response.text

    else:
        response = chat.send_message(input_prompt)
        return response.text
        
    

demo = gradio.Interface(fn=gemini_chat_service_call, inputs="text", outputs="text", title="Chatbot for International Students", description="This is a helpful assistant for international students. You can ask any visa application related questions.")
demo.launch(share=True)