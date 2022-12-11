from flask import Flask, render_template, request, send_file
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__)

# Extracting the data from the website
url = 'https://dolarhoy.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Blue Dollar Purchase Price
bd_purchase = soup.find_all('div', class_='compra')

b_d_purchase = bd_purchase[0].text

for b_d_p in re.findall(r'-?\d+\.?\d*', b_d_purchase):
    b_d_p = float(b_d_p)

blue_dollar_purchase = b_d_p

# Blue Dollar Sales Price
bd_sales = soup.find_all('div', class_='venta')

b_d_sales = bd_sales[0].text

for b_d_s in re.findall(r'-?\d+\.?\d*', b_d_sales):
    b_d_s = float(b_d_s)

blue_dollar_sales = b_d_s

@app.route('/')
def index():
    return render_template("index.html", blue_dollar_sales=blue_dollar_sales, blue_dollar_purchase=blue_dollar_purchase)

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
        
        return render_template("dollar_to_peso_converter.html", result=result, peso=peso)

    return render_template("peso_to_dollar_converter.html")

if __name__=="__main__":
    app.run(debug=True)