from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def converter():
    if request.method == 'POST':
        conversion_type = request.form.get('conversionType')
        amount = float(request.form.get('amount'))
        if conversion_type == 'kmToMiles':
            result = amount * 0.621371
            result_message = f"{amount} kilometers is {result} miles."
        else:
            result = amount * 1.60934
            result_message = f"{amount} miles is {result} kilometers."
        return render_template('index.html', result=result_message)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)