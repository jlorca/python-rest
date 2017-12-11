from eve import Eve
from flask import jsonify

app = Eve()

@app.route('/ejemplos/<ejemplo>')
def devuelvetexto(ejemplo):
    return jsonify({ejemplo:'hola'})

@app.route('/ejemplos/')
def devuelvetextos():
    return jsonify([{'a': 'hola1'},{'b': 'hola2'},{'c': 'hola3'}])

if __name__ == '__main__':
    app.run()


