from get_current_gen_data import get_current_gen_data
import pandas as pd
import plotly.express as px
import plotly
import json

from flask import Flask, render_template
app = Flask(__name__)


current_gen_df = get_current_gen_data()

print(current_gen_df)

current_gen_display_df = pd.melt(current_gen_df[["BIOMASS", "CCGT", "SOLAR", "WIND", "NUCLEAR"]])
current_gen_display_df.rename(columns={'variable': 'Generation', 'value': 'Power (GW)'}, inplace=True)

print(current_gen_display_df.head())

@app.route('/')
def home():
    # Create Bar chart
    fig = px.bar(current_gen_display_df, x='Generation', y='Power (GW)')

    # Create graphJSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # Use render_template to pass graphJSON to html
    return render_template('bar.html', graphJSON=graphJSON)

    # return render_template('home.html')

if __name__ == "__main__":
    print(gen_data)
