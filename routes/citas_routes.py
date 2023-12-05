from bottle import Bottle, run, template, request, redirect
from sqlalchemy import text
from database import engine

subapp = Bottle()


############# variable
@subapp.route('/', method='GET')
def citas():
  # mensaje
  mensaje = request.params.mensaje
  # acceso a db
  conn = engine.connect()
  stmt = text(("""
    SELECT 
        C.id AS cita_id,
        C.indicar_fecha AS fecha,
        P.DNI_PACIENTE AS DNI_paciente_id,
        P.NOMBRE_PACIENTE AS Nombre_paciente,
        P.TIPO_SEGURO AS Tipo_seguro,
        D.NOMBRE AS Nombre_doctor
        FROM citas C
        INNER JOIN paciente P ON C.paciente_id = P.id
        INNER JOIN doctor D ON C.doctor_id = D.id;
    """).format())
  rows = conn.execute(stmt)
  conn.close()
  locals = {'contenido': rows, 'mensaje': mensaje}
  # respuesta
  return template('citas/citas', locals)


############# editar variable
@subapp.route('/edit', method='GET')
def citas_edit():
  id = int(request.params.id)
  # acceso a db
  conn = engine.connect()
  stmt = text(("SELECT * FROM citas WHERE id = {id}").format())
  citas = conn.execute(stmt).fetchone()
  stmt = text(("SELECT * FROM paciente").format())
  paciente = conn.execute(stmt)
  stmt = text(("SELECT * FROM doctor").format())
  doctor = conn.execute(stmt)

  conn.close()
  locals = {
    'citas': citas,
    'id': id,
    'paciente': paciente,
    'doctor': doctor
  }
  # respuesta
  return template('citas/citas_edit', locals)


############# Borrar variable
@subapp.route('/delete', method='GET')
def citas_delete():
  id = int(request.params.id)
  # acceso a db
  conn = engine.connect()
  stmt = text(("DELETE FROM citas WHERE id = {}").format(id))
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # respuesta
  return redirect("/citas?mensaje=Se ha eliminado un Producto")


############# Crear variable
@subapp.route('/new', method='GET')
def citas_new():
  # acceso a db
  contenido = (0, "", "", "", "", "")
  conn = engine.connect()
  stmt = text(("SELECT * FROM paciente").format())
  paciente = conn.execute(stmt)
  stmt = text(("SELECT * FROM doctor").format())
  doctor = conn.execute(stmt)

  conn.close()
  locals = {
    'citas': contenido,
    'id': 0,
    'paciente': paciente,
    'doctor': doctor
  }
  # respuesta
  return template('citas/citas_new', locals)


############# Guardar variable
@subapp.route('/save', method='POST')
def citas_save():
  paciente_id = int(request.forms.get('paciente_id'))
  indicar_fecha = int(request.forms.get('indicar_fecha'))
  doctor_id = request.forms.get('docotr_id')
  id = int(request.forms.get('id'))
  # acceso a db
  conn = engine.connect()
  mensaje = ""
  if id == 0:
    # crear
    stmt = text((
      "INSERT INTO citas (paciente_id, indicar_fecha, doctor_id) VALUES (:paciente_id, :indicar_fecha, :doctor_id)"
    ).format(paciente_id, indicar_fecha, doctor_id))
    mensaje = "citas creada con éxito"
  else:
    # editar
    stmt = text((
      "UPDATE citas SET paciente_id = '{}', indicar_fecha ='{}', doctor_id = '{}'"
    ).format(paciente_id, indicar_fecha, doctor_id))
    mensaje = "citas editado con éxito"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  return redirect("/citas?mensaje=" + mensaje)
