
app.secret_key = '123456789'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assuming the form has 'username' field, retrieve the username
        username = request.form['username']
        # Set the username in the session
        session['username'] = username
        return redirect(url_for('user_profile'))

    return render_template('login.html')


@app.route('/user_profile')
def user_profile():
    # Retrieve the username from the session
    username = session.get('username')

    if username:
        return render_template('user_profile.html', username=username)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # Clear the session
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5004)