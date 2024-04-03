var formLogin = document.getElementById("formLogin")

formLogin.onsubmit = function(evento) {
    //evento es el submit que estamos escuchando. Queremos prevenir el evento por default
    evento.preventDefault();
    //Obtner la info del formulario
    var formulario = new FormData(formLogin);
    /*
    formulario = {
        "email": "elena@codingdojo.com",
        "password": "1234"
    }
    */
    fetch("/login", {method: 'POST', body: formulario})
        .then(response => response.json())
        .then(data => {
            console.log(data); //print
            if(data.message == "login correcto") {
                window.location.href = "/dashboard";
            } else {
                //Crear un mensaje de error
                //Seleccionar el espacio
                var erroresLogin = document.getElementById("erroresLogin");
                erroresLogin.classList.add("alert"); //Agrego la clases que dan formato
                erroresLogin.classList.add("alert-danger");
                erroresLogin.innerText = data.message; //Ingreso el mensaje
            }
        })
}