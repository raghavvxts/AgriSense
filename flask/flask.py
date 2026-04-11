# app.py
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sensors')
def sensors():
    data = {
        'temperature': round(random.uniform(20, 35), 2),
        'humidity': round(random.uniform(30, 70), 2),
        'pressure': round(random.uniform(900, 1100), 2)
    }
    return render_template('sensors.html', data=data)

@app.route('/live')
def live():
    return render_template('live_data.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)


# templates/index.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Dashboard</h1>
    <ul>
        <li><a href="/sensors">Sensors</a></li>
        <li><a href="/live">Live Data</a></li>
        <li><a href="/settings">Settings</a></li>
    </ul>
</body>
</html>
"""

# templates/sensors.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Sensors</title>
</head>
<body>
    <h1>Sensor Data</h1>
    <p>Temperature: {{ data.temperature }} °C</p>
    <p>Humidity: {{ data.humidity }} %</p>
    <p>Pressure: {{ data.pressure }} hPa</p>
    <a href="/">Back</a>
</body>
</html>
"""

# templates/live_data.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Live Data</title>
    <script>
        function updateData() {
            document.getElementById("live").innerText = Math.random().toFixed(3);
        }
        setInterval(updateData, 1000);
    </script>
</head>
<body>
    <h1>Live Data</h1>
    <p>Value: <span id="live">0</span></p>
    <a href="/">Back</a>
</body>
</html>
"""

# templates/settings.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Settings</title>
</head>
<body>
    <h1>Settings</h1>
    <form>
        <label>Device Name:</label>
        <input type="text" placeholder="My Device"><br><br>
        <label>Update Interval:</label>
        <input type="number" value="1"> sec<br><br>
        <button type="submit">Save</button>
    </form>
    <a href="/">Back</a>
</body>
</html>
"""