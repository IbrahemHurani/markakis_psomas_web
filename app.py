from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
import numpy as np
from algorithm import run_algorithm  # האלגוריתם מופרד בקובץ נפרד
import random
import string
app = Flask(__name__, static_folder='static')
app.secret_key = 'supersecretkey'

# מוסיף את המשתנה now לכל הטמפלטים
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/input', methods=['GET', 'POST'])
def input_page():
    if request.method == 'POST':
        try:
            agents = request.form.getlist('agent[]')
            items = request.form.getlist('item[]')

            if not agents or not items:
                return render_template('input.html', error="Please provide at least one agent and one item")

            valuations = {}
            for agent in agents:
                valuations[agent] = {}
                for item in items:
                    val_str = request.form.get(f"{agent}_{item}", "0")
                    try:
                        val = float(val_str)
                        if val < 0:
                            return render_template('input.html', error=f"Negative value for {agent}'s {item}")
                        valuations[agent][item] = val
                    except ValueError:
                        return render_template('input.html', error=f"Invalid number for {agent}'s {item}")

            total_values = sum(sum(vals.values()) for vals in valuations.values())
            if total_values <= 0:
                return render_template('input.html', error="Total value must be positive")

            session['valuations'] = valuations
            return redirect(url_for('result'))

        except Exception as e:
            return render_template('input.html', error=f"Error processing input: {str(e)}")

    return render_template('input.html')

@app.route('/random')
def random_example():
    num_agents = random.randint(2, 8)
    num_items = random.randint(3, 8)

    agents = [string.ascii_uppercase[i] for i in range(num_agents)]  # ['A', 'B', 'C', ...]
    items = [str(i + 1) for i in range(num_items)]                   # ['1', '2', '3', ...]

    valuations = {
        agent: {item: random.randint(1, 15) for item in items}
        for agent in agents
    }

    session['valuations'] = valuations
    return redirect(url_for('result'))

@app.route('/result')
def result():
    try:
        valuations = session.get('valuations', {
            "A": {"1": 50, "2": 30, "3": 20},
            "B": {"1": 30, "2": 40, "3": 30}
        })

        allocation, values, logs = run_algorithm(valuations)

        results = []
        for agent, items in allocation.items():
            results.append({
                'agent': agent,
                'items': items,
                'value': values[agent],
                'value_details': [(item, valuations[agent][item]) for item in items]
            })

        return render_template('result.html',
                               results=results,
                               valuations=valuations,
                               logs=logs)

    except Exception as e:
        app.logger.error(f"Error in algorithm: {str(e)}")
        return render_template('error.html', error_message=str(e))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=7777)
