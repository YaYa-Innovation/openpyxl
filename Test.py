# app.py

from flask import Flask, render_template, request
from openpyxl import load_workbook

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display_rows', methods=['POST'])
def display_rows():
    start_row = int(request.form['start_row'])
    end_row = int(request.form['end_row'])

    workbook = load_workbook(f'{app.config["UPLOAD_FOLDER"]}/sample.xlsx')
    sheet = workbook.active

    data = []
    for i in range(start_row, end_row + 1):
        if i >= 1 and i <= sheet.max_row:
            row_data = [sheet.cell(row=i, column=j).value for j in range(1, sheet.max_column + 1)]
            data.append(row_data)

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
