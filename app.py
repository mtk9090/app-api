from flask import Flask,render_template,request
import requests


app = Flask(__name__, static_folder='static')

@app.route('/',methods=['GET', 'POST'])
def index():
    search = request.form.get('nome_digitado')
    print(search)
    try:
        url = f'http://ip-api.com/json/{search}'
        req = requests.get(url)
        resp = req.json()

    except:
        return render_template('onfline.html')


    else:
        return render_template('ip.html', resp=resp)


if __name__ == '__main__':
    import os

    os.getenv(
    app.run(host='0.0.0.0',port=5000)
    )
