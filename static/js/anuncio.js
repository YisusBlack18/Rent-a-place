function subirInfo() {
    // Variables de Botones
    var barraDeProgreso = document.getElementById("barraDeProgreso");
    var botonMirarInfo = document.getElementById("botonMirarInfo");
    var botonContacto = document.getElementById("botonContacto");
    var botonAnuncioExitoso = document.getElementById("botonAnuncioExitoso");
    
    // Variables de Divs
    var subirInfo = document.getElementById("subirInfo");
    var mirarInfo = document.getElementById("mirarInfo");
    var contacto = document.getElementById("contacto");
    var anuncioExitoso = document.getElementById("anuncioExitoso");

    // Cambio de estilo de la Barra de Progreso
    barraDeProgreso.style.width = 0+"%";

    // // Cambio de estilo de la Barra de Progreso para los Botones
    botonMirarInfo.style.backgroundColor = "#b2b2b2";
    botonContacto.style.backgroundColor = "#b2b2b2";
    botonAnuncioExitoso.style.backgroundColor = "#b2b2b2";

    // Visualizacion de los Divs
    subirInfo.style.display = "block";
    mirarInfo.style.display = "none";
    contacto.style.display = "none";
    anuncioExitoso.style.display = "none";
}

function mirarInfo() {
    // Variables de Botones
    var barraDeProgreso = document.getElementById("barraDeProgreso");
    var botonMirarInfo = document.getElementById("botonMirarInfo");
    var botonContacto = document.getElementById("botonContacto");
    var botonAnuncioExitoso = document.getElementById("botonAnuncioExitoso");

    // Variables de Divs
    var subirInfo = document.getElementById("subirInfo");
    var mirarInfo = document.getElementById("mirarInfo");
    var contacto = document.getElementById("contacto");
    var anuncioExitoso = document.getElementById("anuncioExitoso");

    var ubicacion = document.getElementById("calleSubirInfo").value + ", " + document.getElementById("coloniaSubirInfo").value + ", " + document.getElementById("zonaSubirInfo").value;
    document.getElementById("ubicacionMirarInfo").innerHTML = ubicacion;

    var fechaActual = new Date();
    var fechaActual = fechaActual.getDate() + '/' + (fechaActual.getMonth() + 1) + '/' + fechaActual.getFullYear();
    document.getElementById("fechaActual").innerHTML = fechaActual;

    // Muestra de los Datos
    document.getElementById("alojamientoMirarInfo").innerHTML = document.getElementById("alojamientoSubirInfo").value;
    document.getElementById("explicacionMirarInfo").innerHTML = document.getElementById("explicacionSubirInfo").value;
    document.getElementById("precioMirarInfo").innerHTML = "$" + document.getElementById("precioSubirInfo").value;
    document.getElementById("habitacionesMirarInfo").innerHTML = document.getElementById("habitacionesSubirInfo").value;
    document.getElementById("bañosMirarInfo").innerHTML = document.getElementById("bañosSubirInfo").value;
    document.getElementById("metrosMirarInfo").innerHTML = document.getElementById("metrosSubirInfo").value;
    document.getElementById("edadCasaMirarInfo").innerHTML = document.getElementById("edadCasaSubirInfo").value;
    document.getElementById("wifiMirarInfo").innerHTML = document.getElementById("wifiSubirInfo").value;
    document.getElementById("televisionMirarInfo").innerHTML = document.getElementById("televisionSubirInfo").value;
    document.getElementById("amuebladaMirarInfo").innerHTML = document.getElementById("amuebladaSubirInfo").value;
    document.getElementById("cocheraMirarInfo").innerHTML = document.getElementById("cocheraSubirInfo").value;


    // Cambio de estilo de la Barra de Progreso
    barraDeProgreso.style.width = 33+"%";

    // // Cambio de estilo de la Barra de Progreso para los Botones
    botonMirarInfo.style.backgroundColor = "#38B6FF";
    botonContacto.style.backgroundColor = "#b2b2b2";
    botonAnuncioExitoso.style.backgroundColor = "#b2b2b2";
    
    // Visualizacion de los Divs
    subirInfo.style.display = "none";
    mirarInfo.style.display = "block";
    contacto.style.display = "none";
    anuncioExitoso.style.display = "none";
}

function contacto() {
    // Variables de Botones
    var barraDeProgreso = document.getElementById("barraDeProgreso");
    var botonMirarInfo = document.getElementById("botonMirarInfo");
    var botonContacto = document.getElementById("botonContacto");
    var botonAnuncioExitoso = document.getElementById("botonAnuncioExitoso");

    // Variables de Divs
    var subirInfo = document.getElementById("subirInfo");
    var mirarInfo = document.getElementById("mirarInfo");
    var contacto = document.getElementById("contacto");
    var anuncioExitoso = document.getElementById("anuncioExitoso");

    // Cambio de estilo de la Barra de Progreso
    barraDeProgreso.style.width = 66+"%";

    // Cambio de estilo de la Barra de Progreso para los Botones
    botonMirarInfo.style.backgroundColor = "#38B6FF";
    botonContacto.style.backgroundColor = "#38B6FF";
    botonAnuncioExitoso.style.backgroundColor = "#b2b2b2";
    
    // Visualizacion de los Divs
    subirInfo.style.display = "none";
    mirarInfo.style.display = "none";
    contacto.style.display = "block";
    contacto.style.width = 80+"%";
    anuncioExitoso.style.display = "none";
}

function anuncioExitoso() {
    // Variables de Botones
    var barraDeProgreso = document.getElementById("barraDeProgreso");
    var botonMirarInfo = document.getElementById("botonMirarInfo");
    var botonContacto = document.getElementById("botonContacto");
    var botonAnuncioExitoso = document.getElementById("botonAnuncioExitoso");

    // Variables de Divs
    var subirInfo = document.getElementById("subirInfo");
    var mirarInfo = document.getElementById("mirarInfo");
    var contacto = document.getElementById("contacto");
    var anuncioExitoso = document.getElementById("anuncioExitoso");

    // Cambio de estilo de la Barra de Progreso
    barraDeProgreso.style.width = 100+"%";

    // Cambio de estilo de la Barra de Progreso para los Botones
    botonMirarInfo.style.backgroundColor = "#38B6FF";
    botonContacto.style.backgroundColor = "#38B6FF";
    botonAnuncioExitoso.style.backgroundColor = "#38B6FF";
    
    // Visualizacion de los Divs
    subirInfo.style.display = "none";
    mirarInfo.style.display = "none";
    contacto.style.display = "none";
    anuncioExitoso.style.display = "block";
}

function nextSubirInfo() {
    // Variables para los inputs
    // var alojamientoSubirInfo = document.getElementById("alojamientoSubirInfo");
    // var tituloSubirInfo = document.getElementById("tituloSubirInfo");
    // var explicacionSubirInfo = document.getElementById("explicacionSubirInfo");
    // var precioSubirInfo = document.getElementById("precioSubirInfo");
    // // var tipoSubirInfo = document.getElementById("tipoSubirInfo");
    // var habitacionesSubirInfo = document.getElementById("habitacionesSubirInfo");
    // var salasSubirInfo = document.getElementById("salasSubirInfo");
    // var bañosSubirInfo = document.getElementById("bañosSubirInfo");
    // var metrosSubirInfo = document.getElementById("metrosSubirInfo");
    // // var aireAcondicionadoSubirInfo = document.getElementById("aireAcondicionadoSubirInfo");
    // var edadCasaSubirInfo = document.getElementById("edadCasaSubirInfo");
    // // var patioTraseroSubirInfo = document.getElementById("patioTraseroSubirInfo");
    // var wifiSubirInfo = document.getElementById("wifiSubirInfo");
    // var amuebladaSubirInfo = document.getElementById("amuebladaSubirInfo");
    // var estadoSubirInfo = document.getElementById("estadoSubirInfo");
    // var personasSubirInfo = document.getElementById("personasSubirInfo");
    // var zonaSubirInfo = document.getElementById("zonaSubirInfo");
    // var coloniaSubirInfo = document.getElementById("coloniaSubirInfo");
    // var calleSubirInfo = document.getElementById("calleSubirInfo");
    mirarInfo();
}

function nextContacto() {
    // Variables para los inputs
    var nombreContacto = document.getElementById("nombreContacto");
    var emailContacto = document.getElementById("emailContacto");
    var celularContacto = document.getElementById("celularContacto");
    var telefonoContacto = document.getElementById("telefonoContacto");
    var redSocialContacto = document.getElementById("redSocialContacto");

    // Variables de Valores
    var nombreContactoValue = nombreContacto.value;
    var emailContactoValue = emailContacto.value;
    var celularContactoValue = celularContacto.value;
    var telefonoContactoValue = telefonoContacto.value;
    var redSocialContactoValue = redSocialContacto.value;

    anuncioExitoso();
}