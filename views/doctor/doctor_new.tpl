% include('_header_edit_new.tpl')


<body>
  <h1>Crear doctor</h1>
  <form action="/doctor/save" method="post">
    <input type="hidden" name="id" value="{{contenido[0]}}"><br>
    <table>
      <tr>
        <td>Especialidad:</td>
        <td><input type="text" id="id" name="Especialidad" value="{{contenido[1]}}"></td>
      </tr>
      <tr>
        <td>Numero colegiado:</td>
        <td><input type="text" id="id" name="Numero_colegiado" value="{{contenido[2]}}"></td>
      </tr>
      <tr>
        <td>Horario turno:</td>
        <td><input type="text" id="id" name="Horario_turno" value="{{contenido[3]}}"></td>
      </tr>
      <tr>
        <td>Nombre:</td>
        <td><input type="text" id="id" name="Nombre" value="{{contenido[4]}}"></td>
      </tr>
      <tr>
        <td>DNI_doctor:</td>
        <td><input type="text" id="id" name="DNI_doctor" value="{{contenido[5]}}"></td>
      </tr>
      <tr>
        <td>Fecha_nacimiento:</td>
        <td><input type="text" id="id" name="Fecha_nacimiento" value="{{contenido[6]}}"></td>
      </tr>
      <tr>
      
          <button class="btn">Guardar Cambios</button>
        </td>
      </tr>
    </table>
  </form>
  
  <a href="/doctor" class="btn">Cancelar</a><br><br>
  % include('_footer.tpl')
</body>
</html>