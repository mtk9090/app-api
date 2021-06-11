from flask import Flask,render_template,request
import requests


app = Flask(__name__, static_folder='static')

@app.route('/',methods=['GET', 'POST'])
def index():
    search = request.form.get('nome_digitado')
    #print(search)
    try:
        url = f"""http://ip-api.com/json/{search}?fields=status,
        message,continent,continentCode,country,countryCode,region,
        regionName,city,district,zip,lat,lon,timezone,offset,currency,
        isp,org,as,asname,reverse,mobile,proxy,hosting,query"""
        req = requests.get(url)
        resp = req.json()

    except:
        return render_template('onfline.html')


    else:
        return render_template('ip.html', resp=resp)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    import os

    host = '0.0.0.0'
    port  = int(os.environ.get("PORT", 5000))

    app.run(host, port)
