from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

movies = [
        {"id": 1, "title": "Salaar", "seats": 50, "image_path": "images/movie1.jpg"},
        {"id": 2, "title": "Jawan", "seats": 50, "image_path": "images/movie2.jpg"},
]
booked_seats = {}

@app.route('/')
def index():
    return render_template('index.html', movies=movies)

@app.route('/book/<int:movie_id>', methods=['GET', 'POST'])
def book(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie is None:
        return redirect(url_for('index'))

    if request.method == 'POST':
        num_seats = int(request.form.get('num_seats'))
        if num_seats > movie['seats']:
             return "Not enough seats available"
        movie['seats'] -= num_seats
        for _ in range(num_seats):
            booked_seats[f"{movie_id}-{len(booked_seats) + 1}"] = True
        return "Booking Successful!"

    return render_template('booking.html', movie=movie)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)