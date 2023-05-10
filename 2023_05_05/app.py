from flask import Flask,render_template
import datasource


app = Flask(__name__)
@app.route("/")
def index():
    stock_data = datasource.get_stock_data(stockid=1513) # roberthsu 2330 (自己用1513中興電)
    return render_template("index.jinja.html",data=stock_data)


@app.route("/features/")
def features():
    
    return render_template("features.jinja.html")

@app.route("/priceing/")
def priceing():
    
    return render_template("priceing.jinja.html")

@app.route("/about/")
def about():
    return render_template("about.jinja.html")





    
