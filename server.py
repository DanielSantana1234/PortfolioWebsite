from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a', newline='\n') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            #print(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to the databasee'
    else:
        return 'Something went wrong. Try again!'



# @app.route('/works.html')
# def my_works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def my_contact():
#     return render_template('contact.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')

# @app.route('/favicon.ico')
# def blog():
#     return send_from_directory(os.path.join(app.root_path, 'static'), 'Lambda_logo.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/blog/2024/dogs')
def blog2():
    return 'This is my dog'