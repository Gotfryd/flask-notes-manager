from flask import *
app = Flask(__name__)

notesList = []

@app.route('/')
def index():
    return render_template('index.html', notes=notesList)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        note = request.form['note']
        if note:
            notesList.append(note)
        return redirect('/')
    return render_template('add_note.html')

if __name__ == '__main__':
    app.run(debug=True)
