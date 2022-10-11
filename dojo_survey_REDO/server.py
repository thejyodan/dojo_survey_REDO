from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'secretKey'

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/return', methods=['POST'])
def gohome():
    return render_template('index.html')


@app.route('/users', methods=['POST'])
def user_data():
    print ('received the post data!')

    if len(request.form['fname']) < 1:
        flash('Name cannot be empty!')
        return redirect('/')
    else:
        fname = request.form['fname']
        
    location = request.form['location']
    language = request.form['language']
    
    if len(request.form['desc']) < 1:
        flash('Comment cannot be empty!')
        return redirect('/')
    elif len(request.form['desc']) > 120:
        flash('Comment cannot be more than 120 characters!')
        return redirect('/')
    else:
        comment = request.form['desc']

    print (fname , location, language, comment)

    return render_template('showData.html', name = fname, location = location, language = language, comment = comment)

app.run(debug=True)