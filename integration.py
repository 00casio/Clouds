from flask import Flask
import math

app = Flask(__name__)

def abs_sin(x):
    return abs(math.sin(x))

def numerical_integration(lower, upper, N):
    interval = (upper - lower) / N
    integral_sum = 0.0

    for i in range(N):
        x_midpoint = lower + (i + 0.5) * interval
        integral_sum += abs_sin(x_midpoint) * interval

    return integral_sum

@app.route('/numericalintegralservice/<float:lower>/<float:upper>')
def numerical_integration_service(lower, upper):
    N_values = [10, 100, 1000, 10000, 100000, 1000000]
    results = []

    for N in N_values:
        result = numerical_integration(lower, upper, N)
        results.append((N, result))

    result_str = "<h1>Numerical Integration Results</h1>"
    result_str += f"<p>Interval: [{lower}, {upper}]</p>"
    result_str += "<table border='1'>"
    result_str += "<tr><th>N</th><th>Result</th></tr>"
    for result in results:
        result_str += f"<tr><td>{result[0]}</td><td>{result[1]:.6f}</td></tr>"
    result_str += "</table>"

    return result_str

if __name__ == '__main__':
    app.run(debug=True)

