import os

from flask import Flask, flash, redirect, render_template, request
from helpers import currency_list, exchange


app = Flask(__name__)
app.secret_key = "^*P&Z@',fK5Uo+w-IcHE5*KdZ^N7E_1=*5j['#gUeU495tFzQQT5zO;rn7[e%="

# Checks for api key
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        # Acquires values from the form
        amount = request.form.get("amount")
        currency1 = request.form.get("currency1")
        currency2 = request.form.get("currency2")
        # Checks if value can be converted into a float or not
        try:
            float(amount)
        except:
            flash('Enter a number!')
            return redirect("/")
        # Checks for other cases that would crash the server
        if amount == '':
            flash('Enter a number!')
            return redirect("/")
        elif float(amount) <= 0:
            flash('Enter a number great than zero!')
            return redirect("/")
        elif currency1 == currency2:
            flash('Input two different currencies!')
            return redirect("/")
        # If input is usable, inputs values into the exchange function
        else:
            flash(exchange(currency1, currency2, amount))
            return redirect("/")

    else:
        # Render template that loads currency list as well
        currencies = currency_list()
        return render_template("homepage.html", currencies=currencies)


@app.route("/about")
def about():
    # Loads a simple about page
    if request.method == "GET":
        return render_template("about.html")