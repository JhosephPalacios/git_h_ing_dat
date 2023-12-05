% include('_header_edit_new.tpl')

<body>

  <h1>Crear una Citas {{id}}</h1>
  <form action="/citas/save" method="post">
    <input type="hidden" name="id" value="{{citas[0]}}"><br>
    <table>
      <tr>
        <td>DNI paciente:</td>
        <td><input type="text" id="id" name="DNI_paciente" value="{{citas[1]}}"></td>
      </tr>
      <tr>
        <td>Nombre paciente:</td>
        <td><input type="text" id="id" name="Nombre_paciente" value="{{citas[2]}}"></td>
      </tr>
      <tr>
        <td>Tipo seguro:</td>
        <td><input type="text" id="id" name="Tipo_seguro" value="{{citas[3]}}"></td>
      </tr>
      <tr>
        <td>Indicar fecha:</td>
        <td><input type="date" id="id" name="indicar_fecha" value="{{citas[4]}}"></td>
      </tr>

       <tr>
        <td>Indicar doctor:</td>
        <td><input type="text" id="id" name="nombre_id" value="{{citas[5]}}"></td>
      </tr>
    

      <tr>
        <td></td>
        <td>
          <button class="btn">Guardar Cambios</button>
        </td>
      </tr>
    </table>

    <script>
      function actualizarValor1() {
        var selectElement = document.getElementById("opcionSelect1");
        var selectedValue = selectElement.value;
  
        var valorInput = document.getElementById("valorInput1");
        valorInput.value = selectedValue;
      }
      function actualizarValor2() {
        var selectElement = document.getElementById("opcionSelect2");
        var selectedValue = selectElement.value;
  
        var valorInput = document.getElementById("valorInput2");
        valorInput.value = selectedValue;
      }
      function actualizarValor3() {
        var selectElement = document.getElementById("opcionSelect3");
        var selectedValue = selectElement.value;
  
        var valorInput = document.getElementById("valorInput3");
        valorInput.value = selectedValue;
      }
    </script>
  </form>

  <a href="/productos" class="btn">Cancelar</a>
  % include('_footer.tpl')
</body>
</html>