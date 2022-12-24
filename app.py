from flask import Flask, render_template, request, send_file
import requests

app = Flask(__name__)

blueDollar = requests.get('https://api.bluelytics.com.ar/v2/latest').json()['blue']

blue_dollar_purchase = blueDollar.get('value_buy')

blue_dollar_sales = blueDollar.get('value_sell')

intermediate_price = blueDollar.get('value_buy')

@app.route('/')
def index():
    return render_template("index.html", blue_dollar_sales=blue_dollar_sales, blue_dollar_purchase=blue_dollar_purchase, intermediate_price=intermediate_price)

@app.route('/dollar_to_peso_converter.html', methods=['GET', 'POST'])
def dollar_to_peso_converter():
    if request.method == 'POST':
        dollar = request.form['dollar']
        peso = request.form['peso']

        dollar_x = float(dollar)
        result = dollar_x * blue_dollar_sales
        
        return render_template("dollar_to_peso_converter.html", result=result, dollar=dollar)

    return render_template("dollar_to_peso_converter.html")

@app.route('/peso_to_dollar_converter.html', methods=['GET', 'POST'])
def peso_to_dollar_converter():
    if request.method == 'POST':
        dollar = request.form['dollar']
        peso = request.form['peso']

        peso_x = float(peso)
        result = peso_x / blue_dollar_sales

        return render_template("peso_to_dollar_converter.html", result=result, peso=peso)

    return render_template("peso_to_dollar_converter.html")

if __name__=="__main__":
    app.run(debug=True)
