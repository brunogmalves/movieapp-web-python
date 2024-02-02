from app.model.movie_dao import MovieDao 

@app.route('/edit_movie', methods=['POST'])
def edit_movie():
    if request.method == 'POST':
        # Retrieve updated movie information from the form
        new_movie_name = request.form.get('movieName')
        new_movie_year = request.form.get('movieYear')
        movie_id = request.form.get('movieId')  # Assuming you have a hidden input field for the movie ID in your form

        # Retrieve the existing movie from the database
        existing_movie = MovieDao().get_by_id(movie_id)

        # Update the movie object with the new information
        existing_movie.name = new_movie_name
        existing_movie.year = new_movie_year

        # Update the movie in the database
        MovieDao().update(existing_movie)

        # Redirect to a confirmation page or back to the main page
        return redirect(url_for('index'))