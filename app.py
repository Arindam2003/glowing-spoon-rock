from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Correct file paths for game images
game_images = {
    'rock': 'static/rock.png',
    'paper': 'static/paper.png.webp',
    'scissors': 'static/scissor.png'
}

@app.route('/')
def index():
    return render_template('index.html')

# Game result route
@app.route('/play', methods=['POST'])
def play():
    # Get user choice from the form
    user_choice = request.form['choice']
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    # Determine the result
    result = ''
    if user_choice == computer_choice:
        result = 'Draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice == 'scissors' and computer_choice == 'paper'):
        result = 'You Win!'
    else:
        result = 'You Lose!'

    return render_template(
        'result.html',
        user_choice=user_choice,
        computer_choice=computer_choice,
        result=result,
        user_image=game_images[user_choice],
        computer_image=game_images[computer_choice]
    )


