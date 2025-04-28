from flask import Flask, render_template, request
import csv, json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
        items = data.get('items', [])
        return render_template('items.html', items = items)
    except FileNotFoundError:
        return "Items file not found", 404
    except json.JSONDecodeError:
        return "Error decoding JSON", 500

def read_csv(path):
    data = []
    with open(path) as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            data.append(row)
        return data

def read_json(path):
    with open(path, 'r') as file:
        data = json.load(file)
        return data

@app.route('/products')
def products():
    source = request.args.get('source')
    pro_id = request.args.get('id')
        
    if source == "json":
        data = read_json('products.json')
    elif source == "csv":
        data = read_csv('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source")
    
    if pro_id:
        pro_id = int(pro_id)
        data = [p for p in data if p['id'] == pro_id]
        if not data:
            return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', data=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)