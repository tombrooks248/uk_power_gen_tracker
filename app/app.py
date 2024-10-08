from get_current_gen_data import get_current_gen_data
import pandas

from flask import Flask, render_template
app = Flask(__name__)



gen_data = get_current_gen_data()


@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    print(gen_data)
