$(document).ready(
    function(){
        $("#form-agregar").click(
            function (e) {
                e.preventDefault();

                let mensaje = '';

                if ($("#nombre").val() == '') {
                    mensaje += 'Falta El Nombre <br>'
                }
                if ($("#capitulo").val() == '') {
                    mensaje += 'Faltan los Capitulos <br>'
                }
                if ($("#imagen").val() == '') {
                    mensaje += 'Falta la Imagen <br>'
                }

                if(mensaje.length > 0){
                    $("#mensaje").html(mensaje);
                }else{
                    $("#form-agregar").submit()
                }
            }
        )
    }
);