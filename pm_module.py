from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/h')
def pm_module():

    return render_template('pm_module.html')

@app.route('/process_task_form', methods=['POST'])
def process_task_form():
    task = request.form['task']
    description = request.form['description']
    frequency = request.form['frequency']
    man_hour = request.form['manHour']
    
    # Process the form data (e.g., store in a database)
    
    return "Task added successfully!"

if __name__ == '__main__':
    app.run(debug=True)

