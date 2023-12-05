% include('_header_edit_new.tpl')


<body>
  <h1>Editar paciente {{id}}</h1>

  <form action="/paciente/save" method="post">
    <input type="hidden" name="id" value="{{contenido[0]}}"><br>
    <table>
      <tr>
        <td>Tipo_seguro:</td>
        <td><input type="text" id="id" name="Tipo_seguro" value="{{contenido[1]}}"></td>
      </tr>
      <tr>
        <td>Direccion:</td>
        <td><input type="text" id="id" name="Direccion" value="{{contenido[2]}}"></td>
      </tr>
      <tr>
        <td>Celular:</td>
        <td><input type="text" id="id" name="Celular" value="{{contenido[3]}}"></td>
      </tr>
      <tr>
        <td>Estado civil:</td>
        <td><input type="text" id="id" name="Estado_civil" value="{{contenido[4]}}"></td>
      </tr>
      <tr>
        <td>Nombre paciente:</td>
        <td><input type="text" id="id" name="Nombre_paciente" value="{{contenido[5]}}"></td>
      </tr>
      <tr>
        <td>DNI paciente:</td>
        <td><input type="text" id="id" name="DNI_paciente" value="{{contenido[6]}}"></td>
      </tr>
      <tr>
        <td>Fecha nacimiento:</td>
        <td><input type="text" id="id" name="Fecha_nacimiento" value="{{contenido[7]}}"></td>
      </tr>
      <tr>
        <td></td>
        <td>
          <button class="btn">Guardar Cambios</button>
        </td>
      </tr>
    </table>
  </form>

  <a href="/paciente" class="btn">Cancelar</a><br><br>
  % include('_footer.tpl')
</body>
</html>