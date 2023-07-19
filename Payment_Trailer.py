@app.route('/', methods=['GET', 'POST'])
def index():
    form = MovieForm()
    if form.validate_on_submit():
        movie_id = form.movie.data
        location_id = form.location.data
        time = form.time.data
        return redirect(url_for('booking', movie_id=movie_id, location_id=location_id, time=time))
    return render_template('index.html', form=form)

@app.route('/booking/<movie_id>/<location_id>/<time>', methods=['GET', 'POST'])
def booking(movie_id, location_id, time):
    # Perform necessary operations for the booking page
    # Get movie trailer using movie_id (using a sample URL here)
    trailer_url = 'https://www.youtube.com/embed/example'
    return render_template('booking.html', movie_id=movie_id, location_id=location_id, time=time, trailer_url=trailer_url)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        # Perform payment processing
        # Access form data using request.form['fieldname']
        # Implement payment gateway integration and transaction handling
        # Redirect to confirmation page or handle success/error cases
        return redirect(url_for('confirmation'))
    return render_template('payment.html')

