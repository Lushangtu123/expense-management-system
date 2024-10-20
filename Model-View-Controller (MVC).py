from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Example Model: Handles data for expenses
class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

# Simulate a database (list)
expenses = []

# Controller: Manages user interaction
@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    description = request.form['description']
    amount = float(request.form['amount'])
    expenses.append(Expense(description, amount))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
