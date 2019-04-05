from flask import Flask, render_template
from databases import *
from model import *

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/shop')
def shop_page():
	# name = first_prod().name
	# price = first_prod().price
	# p1 = name
	# name = first_prod(4)
	# p5 = session.query(Product).all()
	# print(p5)
	p7 =first_prod()
	print(p7)
	return render_template("shop.html", p = p7 )

if __name__ == '__main__':
   app.run(debug = True)