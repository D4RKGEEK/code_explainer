import openai

openai.api_key = ""

def code_explain(code):
    try:
        prompt = f"Expain Below Code To A Layman In Steps within 250 words \n"+ code
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        text = response['choices'][0]['text']
        return text
    except Exception as error:
        print(error)
