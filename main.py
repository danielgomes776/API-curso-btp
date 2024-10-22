from flask import Flask
from configuration import configure_all

app = Flask(__name__)

configure_all(app)

# Descomentar o código para testar localmente na máquina
# app.run(debug=True)
