# COSC540: Advanced Software Engineering Project Description

## Chatbot for International Students

The Immigration Advisor ChatBot offers around-the-clock assistance to international students, addressing common challenges they face such as visa processes, university policies, and cultural adjustments. This ChatBot ensures that all responses are not only timely but also accurate and tailored to the individual's needs. 

## Key Features

- **24/7 Availability**: Ensures that students can get help whenever they need it, regardless of time zones or local working hours.

## Implementation

- **Gemini API**: Employs Google’s Gemini API and utilises fine-tuning to enhance the ChatBot's ability to generate contextually relevant answers.

## Getting Started

To set up the ChatBot locally or contribute to its development, follow these steps:

- Fork the repository. 

```bash
git clone [Clone using the web URL OR Use a password-protected SSH key.]
```

```bash
cd Chatbot_International-Students
```

```bash
pip install -r requirements.txt
```

Make sure that you use your own Gemini API key in src/Gemini-API/test_Gemini-API.py and /Users//src/Gemini-API/test_Gemini-API_website.py.

References:

1.) [CiSA: An Inclusive Chatbot Service for International Students and Academics](https://www.researchgate.net/publication/335519974_CiSA_An_Inclusive_Chatbot_Service_for_International_Students_and_Academics) \
2.) [Get started with the Gemini API: Python](https://ai.google.dev/gemini-api/docs/get-started/python) \
3.) [google.generativeai.ChatSession](https://ai.google.dev/api/python/google/generativeai/ChatSession) 
