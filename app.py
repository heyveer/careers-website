#from flask module import Flask class
from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs.10,00,000',
        'experience': '1-3 Years'
    },
    {
        'id': 2,
        'title': 'Java Developer',
        'location': 'Pune, India',
        'salary': 'Rs.12,00,000',
        'experience': '2-5 Years'
    },
    {
        'id': 3,
        'title': 'Cloud Engineer',
        'location': 'Hyderabad, India',
        'salary': 'Rs.15,00,000',
        'experience': '2-4 Years'
    },
    {
        'id': 4,
        'title': 'AI/ML Engineer',
        'location': 'Bengaluru, India',
        'salary': 'Rs.18,00,000',
        'experience': '3-6 Years'
    },
    {
        'id': 5,
        'title': 'Data Scientist',
        'location': 'Mumbai, India',
        'salary': 'Rs.20,00,000',
        'experience': '3-7 Years'
    },
    {
        'id': 6,
        'title': 'DevOps Engineer',
        'location': 'Chennai, India',
        'salary': 'Rs.14,00,000',
        'experience': '2-5 Years'
    },
    {
        'id': 7,
        'title': 'Full Stack Developer',
        'location': 'Gurugram, India',
        'salary': 'Rs.16,00,000',
        'experience': '2-6 Years'
    },
    {
        'id': 8,
        'title': 'Cybersecurity Analyst',
        'location': 'Noida, India',
        'salary': 'Rs.13,50,000',
        'experience': '2-4 Years'
    },
    {
        'id': 9,
        'title': 'Product Manager',
        'location': 'Mumbai, India',
        'salary': 'Rs.25,00,000',
        'experience': '5-8 Years'
    },
    {
        'id': 10,
        'title': 'Site Reliability Engineer',
        'location': 'Bengaluru, India',
        'salary': 'Rs.22,00,000',
        'experience': '4-7 Years'
    },
    {
        'id': 11,
        'title': 'Business Analyst',
        'location': 'Pune, India',
        'salary': 'Rs.11,00,000',
        'experience': '1-4 Years'
    },
    {
        'id': 12,
        'title': 'Frontend Developer',
        'location': 'Hyderabad, India',
        'salary': 'Rs.12,50,000',
        'experience': '2-5 Years'
    },
    {
        'id': 13,
        'title': 'Backend Developer',
        'location': 'Bengaluru, India',
        'salary': 'Rs.14,50,000',
        'experience': '2-6 Years'
    },
    {
        'id': 14,
        'title': 'Software Development Engineer',
        'location': 'Chennai, India',
        'salary': 'Rs.17,00,000',
        'experience': '3-6 Years'
    },
    {
        'id': 15,
        'title': 'Solutions Architect',
        'location': 'Mumbai, India',
        'salary': 'Rs.30,00,000',
        'experience': '6-10 Years'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)