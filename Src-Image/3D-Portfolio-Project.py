from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('3D-Portfolio-Project.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/menu')
# def menu():
#     return render_template('menu.html')

# @app.route('/products')
# def products():
#     return render_template('products.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


