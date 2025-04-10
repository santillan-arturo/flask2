from flask import Flask, render_template, request, redirect, url_for

lista = ["ciao", "ciao2"]

app = Flask(__name__)

x = "ciao"

@app.route('/')
def home():
    return render_template("index.html", paperino = x, lista=lista)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista.append(elemento)
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista):
        lista.pop(indice)
    return redirect(url_for('home'))

@app.route('/svuota', methods=['POST'])
def svuota():
    lista.clear() 
    return redirect(url_for('home'))


@app.route("/inserisci", methods=["GET", "POST"])
def inserisci():
    if request.method == "POST":
        nome = request.form["nome"]
        return f"Hai inserito: {nome}"
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)