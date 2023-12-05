<title>Lista de Productos</title>

% include('_style_menu.tpl')

% include('_header_entity.tpl')

  <style>
    .hidden {
      display: none;
    }
  </style>

<body>

  % include('_menu.tpl')

  <h1>Listado de citas</h1>

  <p>{{mensaje}}</p>
  <a href="/citas/new" class="btn">Agregar Registro</a><br><br>
  <table>
    <thead>
      <th><u>Id</u></th>
      <th><u>Fecha</u></th>
      <th><u>DNI Paciente</u></th>
      <th><u>Nombre Paciente</u></th>
      <th><u>Tipo Seguro</u></th>
      <th><u>Nombre Doctor</u></th>

    </thead>
    <tbody>
      % for s in contenido:
      <tr>
        <td><b>{{s[0]}}</b></td>
        <td><b>{{s[1]}}</b></td>
        <td><b>{{s[2]}}</b></td>
        <td><b>{{s[3]}}</b></td>
        <td><b>{{s[4]}}</b></td>
        <td><b>{{s[5]}}</b></td>
        <td>
          <a href="/citas/edit?id={{s[0]}}" class="btn">Editar</a>
          <a href="/citas/delete?id={{s[0]}}" class="btn">Eliminar</a>
        </td>
      </tr>
      % end

    </tbody>
  </table>
  % include('_footer.tpl')

</body>
</html>