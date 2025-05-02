

from flask import *
from service import API

app = Flask(__name__, static_folder='static', template_folder='template')
api = API(id='1-w-sizFV2i0BTeEd-PzQ9oQojd3A2Y_pvm2XJ4e35z8')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/Apps/match', methods=['GET','POST'])
def match():
    if request.method == 'POST':
        data = request.form.getlist('data[]')
        api.post(0,data)
        return redirect(url_for('match'))
    
    return render_template('match.html')

@app.route('/Apps/pits', methods=['GET','POST'])
def pits():
    if request.method == 'POST':
        data = request.form.getlist('data[]')
        api.post(1,data)
        return redirect(url_for('pits'))
    
    return render_template('pits.html')

@app.route('/Apps/horarios', methods=['GET','POST'])
def horarios():
    data = api.get(3)
    return render_template('horarios.html', data=data)

if __name__ == '__main__':
    app.run(host='localhost', port=4400, debug=True)