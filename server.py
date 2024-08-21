from flask import Flask
import random



app = Flask(__name__)

rand_num = random.randint(0,9)


@app.route('/')
def guess_home():
    return (f'<h1><b>Guess a number between 0 and 9!</b></h1>'
            f'<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmgwOXN6bnNrZjQ1OW5hZHZ3YTlqYWk1eXVrZHd3bnpwYmd5dWtqaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FZuRP6WaW5qg/giphy.webp" width=300 </img>')

@app.route('/<int:number>')
def guess_number(number):
    if number < rand_num:
        return (f'<h1><b>Too low, try again!</b></h1>'
                f'<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzhkMWhwbTNzZXFtaGFhbWdyZGJ1YjdtNjZzMmR4NWZ3N2xpZ2MxOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HoSyEAe48WBpTCmEz4/giphy.webp" width=300 </img>')

    elif number > rand_num:
        return (f'<h1><b>Too high, try again!</b></h1>'
                f'<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzhkMWhwbTNzZXFtaGFhbWdyZGJ1YjdtNjZzMmR4NWZ3N2xpZ2MxOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HoSyEAe48WBpTCmEz4/giphy.webp" width=300 </img>')

    elif number == rand_num:
        return (f'<h1><b>You found me!</b></h1>'
                f'<img src="https://media.giphy.com/media/CAxbo8KC2A0y4/giphy.gif?cid=790b76117lukfew9qr1sulajqom3c37s22ojuc091o36axp4&ep=v1_gifs_search&rid=giphy.gif&ct=g" width=300 </img>')

if __name__ == '__main__':
    app.run(debug=True)


