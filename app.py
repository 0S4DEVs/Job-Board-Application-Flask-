from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

conn = sqlite3.connect('jobs.db')
c = conn.cursor()

# Create a jobs table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS jobs
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT NOT NULL,
              description TEXT NOT NULL,
              employer TEXT NOT NULL)''')
conn.commit()

@app.route('/')
def index():
    # Get all jobs from the database
    c.execute('SELECT * FROM jobs')
    jobs = c.fetchall()
    return render_template('index.html', jobs=jobs)

@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    if request.method == 'POST':
        # Add a new job to the database
        title = request.form['title']
        description = request.form['description']
        employer = request.form['employer']
        c.execute('INSERT INTO jobs (title, description, employer) VALUES (?, ?, ?)',
                  (title, description, employer))
        conn.commit()
        return redirect(url_for('index'))
    else:
        return render_template('add_job.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # Search for jobs that match the query
        query = request.form['query']
        c.execute('SELECT * FROM jobs WHERE title LIKE ? OR description LIKE ? OR employer LIKE ?',
                  ('%' + query + '%', '%' + query + '%', '%' + query + '%'))
        jobs = c.fetchall()
        return render_template('search_results.html', jobs=jobs)
    else:
        return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
