from bottle import Bottle, run, template, request, redirect
from sqlalchemy import text
from database import engine

## ENTIDADES FUERTES
from routes.doctor_routes import subapp as doctor_routes
from routes.paciente_routes import subapp as paciente_routes
## ENTIDADES DEBILES

from routes.citas_routes import subapp as citas_routes
## ENTIDADES ASOCIATIVAS


app = Bottle()

############################################### INICIO Menu de entidades

@app.route('/', method='GET')
def home():

  return template('home')

############################################### FIN Menu de entidades



########################################## INICIO DE - Contacto

@app.route('/contacto', method='GET')
def contacto():
  return template('contacto')

########################################## FIN DE - Contacto

if __name__ == '__main__':
  ## ENTIDADES FUERTES

  app.mount('/doctor',doctor_routes)
  app.mount('/paciente',paciente_routes)
  ## ENNTIDADES DEBILES

  app.mount('/citas', citas_routes)
  ## ENTIDADES ASOCIATIVAS

  
  run(app, host='0.0.0.0', port=8080, debug=True, reloader=True)
