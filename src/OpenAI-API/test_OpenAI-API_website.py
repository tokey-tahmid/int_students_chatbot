from openai import OpenAI
import gradio
client = OpenAI(api_key="#")



messages = [{"role": "system", "content": "You are a helpful assistant for international students. You can help them with their visa application related questions."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(model = "gpt-3.5-turbo",
    messages = messages)
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Chatbot for International Students", description = "This is a helpful assistant for international students. You can ask any visa application related questions.")

demo.launch(share=True)