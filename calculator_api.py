from flask import Flask, request, render_template
from calculator import compute_calculation
app = Flask(__name__)


@app.route('/')
def calculator():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form.get('expression')
    print('expression', expression)

    try:
        result = compute_calculation(expression)
        if result is None:
            return render_template('index.html', error='Please type an expression.')
        return render_template('index.html', result=expression + ' = ' + str(result))
    except AssertionError as err:
        return render_template('index.html', error=err)
    except IndexError as err:
        return render_template('index.html', error='Please type a prefix or an infix expression.')
    except ValueError as err:
        return render_template('index.html', error='Please type a prefix or an infix expression.')
    except ZeroDivisionError as err:
        return render_template('index.html', error=err)
    except Exception as err:
        return render_template('index.html', error=err)


if __name__ == '__main__':
    app.run()
