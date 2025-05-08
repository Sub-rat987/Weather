# Weather App

A simple Flask-based web application that lets you look up current weather conditions for any city. This project provides:

* A clean, responsive HTML/CSS frontend (in `/templates` + `/static/styles`)
* A lightweight Flask server (`server.py`)
* A reusable weather-lookup module (`weather.py`)
* Live demo: [https://weather-bq2n.onrender.com/](https://weather-bq2n.onrender.com/)

---

## Features

* ✅ Search by city name
* ✅ Displays temperature, humidity, wind speed, weather description, and an icon
* ✅ Graceful error handling for invalid city names or API failures
* ✅ Mobile-friendly design

---

## Tech Stack

* **Backend**: Python 3.x, Flask
* **HTTP requests**: `requests` (to talk to the Weather API)
* **Templates**: Jinja2 (built into Flask)
* **Styling**: plain CSS (in `static/styles`)

---

## Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/Sub-rat987/Weather.git
   cd Weather
   ```

2. **Create & activate a virtual environment** (recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Linux / macOS
   venv\Scripts\activate.bat     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

This app uses an external weather-data provider (e.g. OpenWeatherMap). You’ll need your own API key:

1. Sign up at your chosen provider (e.g. [https://openweathermap.org/](https://openweathermap.org/))
2. Create a file named `.env` in the project root with:

   ```bash
   WEATHER_API_KEY=your_api_key_here
   ```
3. (Alternatively) export the key directly in your shell:

   ```bash
   export WEATHER_API_KEY=your_api_key_here
   ```

---

## Usage

1. **Start the server**

   ```bash
   python server.py
   ```

   or, if you prefer Flask’s CLI:

   ```bash
   export FLASK_APP=server.py
   flask run
   ```

2. **Open your browser**
   Visit `http://localhost:5000`, enter a city name, and click “Get Weather.”

---

## Project Structure

```
Weather/
├── artifacts/                 # (if present) saved models or data
├── static/
│   └── styles/                # CSS files
├── templates/
│   └── index.html             # Main HTML template
├── server.py                  # Flask app & route definitions
├── weather.py                 # Module for fetching/parsing weather data
├── requirements.txt           # Python dependencies
└── .gitignore
```

---

## Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes & push: `git push origin feature/YourFeature`
4. Open a pull request!

Please ensure your code is PEP 8 formatted and includes doc-strings where appropriate.

---

## License

This project is released under the MIT License. See `LICENSE` for details.

---

*Happy weather-watching!*
