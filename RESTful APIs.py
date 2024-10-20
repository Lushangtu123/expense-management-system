@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    return jsonify([{'description': e.description, 'amount': e.amount} for e in expenses])
