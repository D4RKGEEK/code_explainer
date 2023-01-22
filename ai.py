import openai

openai.api_key = "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"

def code_explain(code):
    try:
        prompt = f"Expain This Code To A Layman + \n {code}"
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        text = response['choices'][0]['text']
        print(text)
        return text
    except Exception as error:
        print(error)