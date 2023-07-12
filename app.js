//alerts
function alertaInicial() {
  swal({
    title: "URGENCIAS",
    text: "comunicate al 11 55258145",
    icon: "warning",
  });
}

function envioExitoso() {
    swal({
        title: "Excelente",
        text: "Mensaje Enviado",
        icon: "success",
    });


function faltandatos(){
    swal({
        title: 'DATOS ERRONEOS',
        Text: 'Esta ingresando datos erroneos o dejando casilleros vacios',
        icon: 'error'
    })
}


}

function validarFormulario(){
    let nombre = document.getElementById('nombre').value
    let correo = document.getElementById('correo').value
    let mensaje = document.getElementById('mensaje').value



    if (mensaje =='' || correo ==''|| nombre ==''){
        return faltandatos()
    }else{
        return envioExitoso()
    }

}
  // Obtener los valores de los campos



//alertaInicial()
