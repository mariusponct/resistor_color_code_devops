from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_resistance(band1, band2, band3, band4=None):
    # Color code dictionary mapping colors to their respective values
    color_codes = {
        'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
        'green': 5, 'blue': 6, 'violet': 7, 'gray': 8, 'white': 9
    }
    
    # Mapping the multiplier to its corresponding power of 10
    multipliers = {'black': 1, 'brown': 10, 'red': 100, 'orange': 1000, 'yellow': 10000,
                   'green': 100000, 'blue': 1000000, 'violet': 10000000, 'gray': 100000000, 'white': 1000000000,
                   'gold': 0.1, 'silver': 0.01}
    
    # Mapping the tolerance to its corresponding percentage value
    tolerances = {'brown': '+/- 1%', 'red': '+/- 2%', 'green': '+/- 0.5%', 'blue': '+/- 0.25%', 'violet': '+/- 0.1%',
                  'gray': '+/- 0.05%', 'gold': '+/- 5%', 'silver': '+/- 10%'}
    
    # Calculate resistance based on color bands
    resistance = (color_codes[band1] * 10 + color_codes[band2]) * multipliers[band3]
    
    # If there is a 4th band (tolerance), calculate and append the tolerance
    if band4:
        resistance_str = f"{resistance} Ohms, {tolerances[band4]}"
    else:
        resistance_str = f"{resistance} Ohms"
    
    return resistance_str

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    band1 = request.form.get('band1')
    band2 = request.form.get('band2')
    band3 = request.form.get('band3')
    band4 = request.form.get('band4')  # Optional, tolerance band
    resistance = calculate_resistance(band1, band2, band3, band4)
    return render_template('result.html', resistance=resistance)

if __name__ == '__main__':
    app.run(debug=True)
