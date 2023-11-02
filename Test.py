@app.route('/get_filtered_data')
def get_filtered_data():
    workbook = load_workbook('static/data.xlsx')
    sheet = workbook.active

    start_date_str = request.args.get('startDate')
    end_date_str = request.args.get('endDate')

    start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else None

    dates = []
    values = []

    for row in sheet.iter_rows(values_only=True):
        date = row[0]
        date_str = date.strftime('%m/%d/%Y')  # Format changed here

        if (not start_date or date >= start_date) and (not end_date or date <= end_date):
            dates.append(date_str)
            values.append(row[1:])

    return jsonify(dates=dates, values=values)
