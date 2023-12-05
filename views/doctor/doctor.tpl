<title>Lista de Doctores</title>

% include('_style_menu.tpl')

% include('_header_entity.tpl')

<body>

  % include('_menu.tpl')

  <h1>Listado de Doctores</h1>

  <p>{{mensaje}}</p>
  <a href="/doctor/new" class="btn"> Agregar Registro </a><br><br>
  <table>
    <thead>
      <th>Id</th>
      <th>Especialidad</th>
      <th>Nr Colegiatura</th>
      <th>Horario Turno</th>
      <th>Nombre</th>
      <th>DNI doctor</th>
      <th>Fecha Nacimiento</th>

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
        <td>
          <a href="/doctor/edit?id={{s[0]}}" class="btn">Editar</a>
          <a href="/doctor/delete?id={{s[0]}}" class="btn">Eliminar</a>
        </td>
      </tr>
      % end
    </tbody>
  </table>
  % include('_footer.tpl')
</body>
</html>