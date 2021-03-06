from flask import Flask, render_template, request, url_for, session, redirect, flash, Markup, jsonify, make_response
#from flask_cors import CORS
from model import *
from logic import * 

import pyrebase
import os
import sys
import logging

application = Flask(__name__)

application.logger.addHandler(logging.StreamHandler(sys.stdout))
application.logger.setLevel(logging.ERROR)

#CORS(application)
application.secret_key = "lets_judge"

# Home form load
@application.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


############################ Ajax experimenting #########################
from numpy.random import rand

@application.route('/update_work', methods=['POST'])
def update_work():
    data1 = request.json['work1_up']
    data2 = request.json['work1_down']
    
    
    print(data1,data2)
    
    if data1 != None:
        updated_page = int(data1) + 1
    else:
        updated_page = 35
    
    return jsonify(updated_page)





########################################################################

# CJ compare form load
@application.route('/compare/', methods=['GET','POST'])
def compare():
                
    if request.method == 'GET':
        try:
            if "user" in session:
                #pass #delete this later!
                exam_details = read_config_json(session["user"])
                #print(f'Exam details: {exam_details}')
                #print(type(exam_details))
                #round_number       = get_round_num(session['user'])
                #percent            = int(round(((round_number - 1) / 5) * 100, 0))
                #total_combinations = get_total_combinations(session['user'])
                #if round_number != total_combinations:
                #    combo_id       = get_combinations(round_number,session['user'])
                #    tweet1_content = get_tweet_content(combo_id['tweet_1'])
                #    tweet2_content = get_tweet_content(combo_id['tweet_2'])

                #    tweet1_content = Markup(tweet1_content.replace('_b', '<br><br>'))
                #    tweet2_content = Markup(tweet2_content.replace('_b', '<br><br>'))
                    
                #    tweet1, tweet2, tweet1_id, tweet2_id = tweet1_content, tweet2_content, combo_id['tweet_1'], combo_id['tweet_2']
                #else:
                #    msg = "You have complaed all the comparisons, please provide feedback on your experience."
                #    flash(msg, 'info')
                #    return redirect(url_for('feedback'))
                #print("Get request on the compare.")
            else:
                return redirect(url_for('signup'))
        except:
            return redirect(url_for('logout'))
            
    
    if request.method == 'POST':
        exam_details     = read_config_json(session["user"])
        radio_selections = []#request.form.get("AO1")#request.form.getlist('options')#request.form.get('option')
        
        for key in exam_details:
            radio_button = request.form.get(key)
            radio_selections.append(radio_button)
        
        justification = request.form.get('content')
        
        print(f"radio_1: {radio_selections}")

        if radio_selections[0] == None:
            message = "You have missed some required information. Please try again"
            flash(message, "info")
            return redirect(url_for('compare'))
        else:
            exam_details = read_config_json(session["user"])
            round_number = get_round_num(session['user'])
            print(f"round number: {round_number}")
            #percent = round_number / 5 # in future change the 5 to a denominator that is generated at the sign up space of total combinations.
            #update_result(round_number,radio_1,session['user'])
            #record_justification(round_number,session['user'],justification)
            update_round_number(session['user'])
            #update_cj_score()

            #return redirect(url_for('compare'))
             
    return render_template('compare.html', exam_details=exam_details, tweet1=1, 
                           tweet2=url_for( 'static', filename='images/car.jpeg' ), 
                           work1_id=1, work2_id=2, percent=int(1), tweet_count=1) #,exam_details=exam_details, tweet1 = tweet1, tweet2 = tweet2, tweet1_id = tweet1_id, tweet2_id = tweet2_id, percent = int(percent), tweet_count = round_number


# CJ Explination form load.
@application.route('/explination/')
def explination():
    return render_template('explination.html')


# CJ Results form load.
@application.route('/results/', methods=['GET','POST'])
def results():
    if request.method == 'GET':
        rank, content = display_ranking()

        elo_rank, elo_content = display_elo_ranking()

    if request.method == 'POST':
        pass
    
    return render_template('results.html', rank=rank, content=content, 
                            elo_rank=elo_rank, elo_content=elo_content)
                           

# Feedback form load
@application.route('/feedback/', methods=['GET','POST'])
def feedback():
    if request.method == 'GET':
        if "user" in session:
            return render_template('feedback.html')
        else:
            return redirect(url_for('login'))
    
    if request.method == 'POST':
        name     = request.form.get('name')
        contact  = request.form.get('contact')
        feedback = request.form.get('comments')
        rating   = request.form.get('experience')
        
        create_feedback(name, feedback, rating, session, contact)
        msg = "thank you for the feedback!"
        flash(msg, 'info')
        return redirect(url_for('index'))


# Loging form load
@application.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        try:
            if "user" in session:
                return redirect(url_for('logout'))
            else:
                return render_template('login.html')
        except:
            msg = "An issue happened. Please try again."
            flash("You have been signed up successfully.", "info")
            return redirect('index')

    if request.method == 'POST':
        try:
            email    = request.form.get('email')
            password = request.form.get('password')
            user     = login_user(email,password)
            
            if user == None:
                msg = "This email address or password mightbe wrong, please try again. Additionally, You might need to sign up instead."
                flash(msg, 'info')
                return redirect(url_for('login'))
            else:
                session['user']  = user
                session['email'] = email
                flash("You have been logged in successfully.", "info")
                res = make_response(redirect(url_for('index')))
                res.set_cookie("logged_in", "True")
                return res
        except:
            flash("Email address does not exist, please sign up.", "info")
            return redirect(url_for('signup'))


# Signup form load
@application.route('/signup/', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    
    if request.method == 'POST':
        email          = request.form.get('email')
        password       = request.form.get('password')
        exam_board     = request.form.get('examboard')
        subject        = request.form.get('subject')
        password_check = request.form.get('password_check')
        data_confirm   = request.form.get('confirm')

        print(data_confirm)

        if data_confirm == 'on':
            if password == password_check:
                success, user_id = signup_user(email,password,exam_board,subject)
                session['user']  = user_id
                session['email'] = email

                if success == True:
                    flash("You have been signed up successfully.", "info")
                    res = make_response(redirect(url_for('index')))
                    res.set_cookie("logged_in", "True")
                    return res
                else:
                    flash("Email address already exists, please try logging in instead.", "info")
                    return redirect(url_for('signup'))
            else:
                flash("Invalid email and/or passwords do not match.", "info")
                return redirect(url_for('signup'))
        else:
            flash("Please confirm you are happy with how we use your data.", "info")
            return redirect(url_for('signup'))


# Password reset form load
@application.route('/reset_password/', methods=['GET','POST'])
def reset_password():
    if request.method == 'GET':
        return render_template('forgotten_password.html')
    
    if request.method == 'POST':
        auth  = init_auth()
        email = request.form.get('email')

        print(email)
        auth.send_password_reset_email(email)

        return redirect(url_for('login'))


# Log out form load
@application.route('/logout/')
def logout():
    if "user" in session:
        user    = session["user"]
        message = "You have been logged out succesfully"
        flash(message, "info")

    session.pop("user", None)
    res = make_response(redirect(url_for('index')))
    res.set_cookie("logged_in", "False")
    return res
    
#return redirect(url_for("index"))

#if __name__ == '__main__':
#     application.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))