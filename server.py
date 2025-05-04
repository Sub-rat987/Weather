from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/', methods=["GET"]) #this is the homepage, routes we access on the web
@app.route('/index', methods=["GET"]) #access the homepage from index
def index():
    
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    if not bool(city.strip()):
        city = "Rourkela"
    
    weather_data = get_current_weather(city)

    #check for valid server connection, here cod value
    if not weather_data['cod'] == 200:
        return render_template(
            "citynotfound.html"
        )

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )
if __name__=="__main__":
    serve(app,host="0.0.0.0", port=8000) #to run on local host







