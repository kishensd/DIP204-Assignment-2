from flask import Flask, render_template, request

app = Flask(__name__)
app.config.update({'TEMPLATES_AUTO_RELOAD': True})

@app.route('/')
def landing():
    return render_template('landing.html')


@app.route('/about_langkawi')
def about_langkawi():
    return render_template('about_langkawi.html', page = 'about_langkawi')


@app.route('/planning_a_visit')
def planning_a_visit():
    return render_template('planning_a_visit.html', page = 'planning_a_visit')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html', page = 'gallery')


@app.route('/promotions_and_packages')
def promotions_and_packages():
    return render_template('promotions_and_packages.html', page = 'promotions_and_packages')


@app.route('/attractions')
def attractions():
    return render_template('attractions.html', page = 'attractions')


@app.route('/food_and_dining')
def food_and_dining():
    return render_template('food_and_dining.html', page = 'food_and_dining')


@app.route('/hotels')
def hotels():
    return render_template('hotels.html', page = 'hotels')


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html', page = 'contact_us')


if __name__ == '__main__':
    app.run()
