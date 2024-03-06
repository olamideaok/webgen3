from flask import Flask, render_template, request
import openai

app = Flask(__name__)

def generate_website(description):
    # This function should use the OpenAI API to generate a website based on the description
    OPENAI_API_KEY = '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'
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output HTML only, with no comment."},
            {"role": "user", "content": description}
        ]
    )

    return response.choices[0].message.content

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_html = ""
    description = ""  # Initialize the variable to avoid the referenced before assignment error

    if request.method == 'POST':
        description = request.form.get('description', '')
        generated_html = generate_website(description)

    return render_template('index.html', description=description, generated_html=generated_html)

if __name__ == '__main__':
    app.run(debug=True)
