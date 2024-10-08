from get_current_gen_data import get_current_gen_data
import pandas

from flask import Flask
app = Flask(__name__)



gen_data = get_current_gen_data()


@app.route('/')
def home():
    return "Hello world!"


if __name__ == "__main__":
    print(gen_data)
