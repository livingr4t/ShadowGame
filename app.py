from flask import Flask, render_template
import os

app = Flask(__name__)

# Główna strona startowa gry
@app.route('/')
def index():
    return render_template('index.html')

# Trasa dla uruchomienia gry
@app.route('/game')
def game():
    from game_logic import main_game_loop
    main_game_loop()
    return "Gra została zakończona. Odśwież stronę, aby zagrać ponownie."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
