from flask import Flask
from src.line_search_algorithm import line_search
import numpy as np

app = Flask(__name__)

@app.route('/test-my-function')
def test_my_function():
    A = np.array([[2, 0], [0, 8]])
    b = np.array([-1, -4])
    c = 5
    result = line_search(A,b,c) 
    return f'Test Result: {result}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 
