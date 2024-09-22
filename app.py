from flask import Flask, render_template
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Define the free food locations in Lahore
locations = [
    {"name": "Edhi Foundation", "lat": 31.5497, "lng": 74.3436},
    {"name": "Saylani Welfare", "lat": 31.5204, "lng": 74.3587},
    {"name": "Jamaat-e-Islami Food Bank", "lat": 31.4750, "lng": 74.2840},
    {"name": "Shaukat Khanum Memorial Cancer Hospital", "lat": 31.4820, "lng": 74.2925},
    {"name": "Chhipa Welfare Association", "lat": 31.5247, "lng": 74.3503}
]

@app.route('/')
def home():
    return render_template('home.html', locations=locations)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
