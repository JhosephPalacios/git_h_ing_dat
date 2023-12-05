from bottle import Bottle, run, template, request, redirect
from sqlalchemy import text
from database import engine

subapp=Bottle()
########################################## INICIO DE - Lista de doctores


############# variables
@subapp.route('/', method='GET')
def doctor():
  # doctor
  doctor = request.params.doctor
  # acceso a db
  conn = engine.connect()
  stmt = text(("SELECT * FROM doctor").format())
  rows = conn.execute(stmt)
  conn.close()
  locals = {'contenido': rows, 'mensaje': doctor}
  # respuesta
  return template('doctor/doctor', locals)


############ editar variable
@subapp.route('/edit', method='GET')
def doctor_edit():
  id = int(request.params.id)
  # acceso a db
  conn = engine.connect()
  stmt = text(("SELECT * FROM doctor WHERE id = {}").format(id))
  contenido = conn.execute(stmt).fetchone()
  conn.close()
  locals = {'contenido': contenido, 'id': id}
  # respuesta
  return template('doctor/doctor_edit', locals)


############# Borrar variable
@subapp.route('s/delete', method='GET')
def doctor_delete():
  id = int(request.params.id)
  # acceso a db
  conn = engine.connect()
  stmt = text(("DELETE FROM doctor WHERE id = {}").format(id))
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # respuesta
  return redirect("/doctor?mensaje=Se ha eliminado un cliente")


############# Crear variable
@subapp.route('/new', method='GET')
def doctor_new():
  # acceso a db
  contenido = (0, "", "", "", "", "", "")
  locals = {'contenido': contenido}
  # respuesta
  return template('doctor/doctor_new', locals)


############# Guardar variable
@subapp.route('/save', method='POST')
def doctor_save():
  fecha_nacimiento = request.forms.get('FECHA_NACIMIENTO')
  dni_doctor = request.forms.get('DNI_DOCTOR')
  nombre = request.forms.get('NOMBRE')  
  horario_turno = request.forms.get('HORARIO_TURNO')
  numero_colegiado = request.forms.get('NUMERO_COLEGIADO')
  especialidad = request.forms.get('ESPECIALIDAD')
  id = int(request.forms.get('id'))
  # acceso a db
  conn = engine.connect()
  mensaje = ""
  if id == 0:
    # crear
    stmt = text((
      "INSERT INTO doctor (especialidad,numero_colegiado,horario_turno,nombre,dni_doctor,fecha_nacimiento) VALUES ('{}','{}','{}')"
    ).format(especialidad,numero_colegiado,horario_turno,nombre,dni_doctor,fecha_nacimiento))
    mensaje = "doctor creado con exito"
  else:
    stmt = text((
      "UPDATE doctor SET especialidad = '{}', numero_colegiado = '{}',horario_turno = '{}', nombre= '{}',dni_doctor= '{}',fecha_nacimiento WHERE id = {}"
    ).format(especialidad,numero_colegiado,horario_turno,nombre,dni_doctor,fecha_nacimiento, id))
    mensaje = "doctor editado con exito"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  return redirect("/doctor?mensaje=" + mensaje)


########################################## FIN DE - Lista de doctores
