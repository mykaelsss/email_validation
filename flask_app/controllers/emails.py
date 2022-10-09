from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.email import Email


@app.route('/')
def email():
    return render_template("email.html")


@app.route('/create/email', methods=['POST'])
def create_email():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.create_email(request.form)
    return redirect('/results')


@app.route('/results')
def results():
    return render_template("results.html", emails=Email.all_emails())

@app.route('/delete/email/<int:id>')
def delete(id):
    data = {
        "id":id
    }
    Email.delete(data)
    return redirect('/results')
