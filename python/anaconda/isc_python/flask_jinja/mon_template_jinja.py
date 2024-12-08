from jinja2 import Environment, FileSystemLoader
from flask import Flask

# Flask app
app = Flask('ISC')

# Template
file_loader = FileSystemLoader('.')

env = Environment(loader=file_loader)

template = env.get_or_select_template('mon_template_jinja.html')

mes_voitures = [
    {'nom' : 'Camaro', 'puissance' : 450},
    {'nom' : 'Porshe', 'puissance' : 500},
    {'nom' : 'Ferrari', 'puissance' : 550}
]

# Test jinja output
#output = template.render(voitures=mes_voitures)
#print(output)

# Flask route
@app.route('/')
def mon_site():
    return template.render(voitures=mes_voitures)

# Launch flask
app.run()