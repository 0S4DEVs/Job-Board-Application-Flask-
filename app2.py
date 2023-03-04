from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    employer = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Job('{self.title}', '{self.employer}', '{self.location}')"

@app.route('/')
def index():
    jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)

@app.route('/add', methods=['GET', 'POST'])
def add_job():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        employer = request.form['employer']
        location = request.form['location']
        salary = request.form['salary']

        job = Job(title=title, description=description, employer=employer, location=location, salary=salary)
        db.session.add(job)
        db.session.commit()

        flash('Job posted successfully', 'success')
        return redirect(url_for('index'))

    return render_template('add_job.html')

@app.route('/search', methods=['GET', 'POST'])
def search_jobs():
    if request.method == 'POST':
        search_term = request.form['search_term']
        jobs = Job.query.filter(Job.title.like(f'%{search_term}%') | Job.description.like(f'%{search_term}%'))
        return render_template('search_results.html', jobs=jobs)

    return render_template('search_jobs.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
