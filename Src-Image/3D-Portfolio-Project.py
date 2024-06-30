from flask import Flask, render_template, request, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-gmail-adress' # Email recipient
app.config['MAIL_PASSWORD'] = 'your-gmail-password'  # You must create an application password in Gmail

mail = Mail(app)        

@app.route('/')
def home():
    return render_template('3D-Portfolio-Project.html')

@app.route('/send-email', methods=['POST'])             
def send_email():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        message = request.form['message']

        # Email sending process
        try:
            msg = Message(subject='New Contact Form Submission',
                          sender=app.config['MAIL_USERNAME'],
                          recipients=['your-gmail-adress'])  # Email recipient

            msg.body = f"Name: {full_name}\nEmail: {email}\nMessage:\n{message}"

            mail.send(msg)
            return 'The e-mail was sent successfully!'
        except Exception as e:
            return f'Error occurred: {str(e)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)