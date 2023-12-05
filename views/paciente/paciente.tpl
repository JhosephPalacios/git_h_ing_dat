<title>Lista de Pacientes</title>

% include('_style_menu.tpl')

% include('_header_entity.tpl')

<body>

  % include('_menu.tpl')

  <h1>Listado de pacientes</h1>

  <p>{{mensaje}}</p>
  <a href="/paciente/new" class="btn"> Agregar Registro </a><br><br>
  <table>
    <thead>
      <th>id</th>
      <th>Tipo_seguro</th>
      <th>Direccion</th>
      <th>Celular</th>
      <th>Estado_civil</th>
      <th>Nombre_paciente</th>
      <th>DNI_paciente</th>
      <th>Fecha_nacimiento</th>

    </thead>
    <tbody>
      % for s in contenido:
      <tr>
        <td>{{s[0]}}</td>
        <td>{{s[1]}}</td>
        <td>{{s[2]}}</td>
        <td>{{s[3]}}</td>
        <td>{{s[4]}}</td>
        <td>{{s[5]}}</td>
        <td>{{s[6]}}</td>
        <td>{{s[7]}}</td>
        <td>
          <a href="/paciente/edit?id={{s[0]}}" class="btn">Editar</a>
          <a href="/paciente/delete?id={{s[0]}}" class="btn">Eliminar</a>
        </td>
      </tr>
      % end
    </tbody>
  </table>
  % include('_footer.tpl')
</body>
</html>