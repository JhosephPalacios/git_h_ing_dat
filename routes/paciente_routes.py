from bottle import Bottle, run, template, request, redirect
from sqlalchemy import text
from database import engine

subapp=Bottle()
########################################## INICIO DE - Lista de paciente


############# variables
@subapp.route('/', method='GET')
def paciente():
  # paciente
  paciente = request.params.paciente
  # acceso a db
  conn = engine.connect()
  stmt = text(("SELECT * FROM paciente").format())
  rows = conn.execute(stmt)
  conn.close()
  locals = {'contenido': rows, 'mensaje': paciente}
  # respuesta
  return template('paciente/paciente', locals)


############ editar variable
@subapp.route('/edit', method='GET')
def paciente_edit():
  id = int(request.params.id)
  # acceso a db
  conn = engine.connect()
  stmt = text(("SELECT * FROM paciente WHERE id = {}").format(id))
  contenido = conn.execute(stmt).fetchone()
  conn.close()
  locals = {'contenido': contenido, 'id': id}
  # respuesta
  return template('paciente/paciente_edit', locals)


############# Borrar variable
@subapp.route('s/delete', method='GET')
def paciente_delete():
  id = int(request.params.id)
  # acceso a db
  conn = engine.connect()
  stmt = text(("DELETE FROM paciente WHERE id = {}").format(id))
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # respuesta
  return redirect("/paciente?mensaje=Se ha eliminado un cliente")


############# Crear variable
@subapp.route('/new', method='GET')
def paciente_new():
  # acceso a db
  contenido = (0, "", "", "", "", "", "", "")
  locals = {'contenido': contenido}
  # respuesta
  return template('paciente/paciente_new', locals)


############# Guardar variable
@subapp.route('/save', method='POST')
def paciente_save():
  Fecha_nacimiento = request.forms.get('FECHA_NACIMIENTO')
  DNI_paciente = request.forms.get('DNI_PACIENTE')
  Nombre_paciente = request.forms.get('NOMBRE_PACIENTE')
  Estado_civil = request.forms.get('ESTADO_CIVIL')  
  Celular = request.forms.get('CELULAR')
  Direccion = request.forms.get('DIRECCION')
  Tipo_seguro = request.forms.get('TIPO_SEGURO')
  id = int(request.forms.get('id'))
  # acceso a db
  conn = engine.connect()
  mensaje = ""
  if id == 0:
    # crear
    stmt = text((
      "INSERT INTO paciente (Tipo_seguro,Direccion,Celular,Estado_civil,Nombre_paciente,DNI_paciente,Fecha_nacimiento) VALUES ('{}','{}','{}')"
    ).format(Tipo_seguro,Direccion,Celular,Estado_civil,Nombre_paciente,DNI_paciente,Fecha_nacimiento))
    mensaje = "paciente creado con exito"
  else:
    stmt = text((
      "UPDATE paciente SET Tipo_seguro = '{}',Direccion = '{}',Celular = '{}',Estado_civil = '{}',Nombre_paciente = '{}',DNI_paciente = '{}',Fecha_nacimiento = '{}'"
    ).format(Tipo_seguro,Direccion,Celular,Estado_civil,Nombre_paciente,DNI_paciente,Fecha_nacimiento, id))
    mensaje = "paciente editado con exito"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  return redirect("/paciente?mensaje=" + mensaje)


########################################## FIN DE - Lista de pacientes
