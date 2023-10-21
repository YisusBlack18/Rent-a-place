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
    var tituloSubirInfo = document.getElementById("tituloSubirInfo");
    var explicaionSubirInfo = document.getElementById("explicaionSubirInfo");
    var precioSubirInfo = document.getElementById("precioSubirInfo");
    var tipoSubirInfo = document.getElementById("tipoSubirInfo");
    var habitacionesSubirInfo = document.getElementById("habitacionesSubirInfo");
    var salasSubirInfo = document.getElementById("salasSubirInfo");
    var bañosSubirInfo = document.getElementById("bañosSubirInfo");
    var metrosSubirInfo = document.getElementById("metrosSubirInfo");
    var aireAcondicionadoSubirInfo = document.getElementById("aireAcondicionadoSubirInfo");
    var edadCasaSubirInfo = document.getElementById("edadCasaSubirInfo");
    var patioTraseroSubirInfo = document.getElementById("patioTraseroSubirInfo");
    var wifiSubirInfo = document.getElementById("wifiSubirInfo");
    var amuebladaSubirInfo = document.getElementById("amuebladaSubirInfo");
    var estadoSubirInfo = document.getElementById("estadoSubirInfo");
    var personasSubirInfo = document.getElementById("personasSubirInfo");
    var zonaSubirInfo = document.getElementById("zonaSubirInfo");
    var coloniaSubirInfo = document.getElementById("coloniaSubirInfo");
    var calleSubirInfo = document.getElementById("calleSubirInfo");

    // Variables de Valores
    var tituloSubirInfoValue = tituloSubirInfo.value;
    var explicaionSubirInfoValue = explicaionSubirInfo.value;
    var precioSubirInfoValue = precioSubirInfo.value;
    var tipoSubirInfoValue = tipoSubirInfo.value;
    var habitacionesSubirInfoValue = habitacionesSubirInfo.value;
    var salasSubirInfoValue = salasSubirInfo.value;
    var bañosSubirInfoValue = bañosSubirInfo.value;
    var metrosSubirInfoValue = metrosSubirInfo.value;
    var aireAcondicionadoSubirInfoValue = aireAcondicionadoSubirInfo.value;
    var edadCasaSubirInfoValue = edadCasaSubirInfo.value;
    var patioTraseroSubirInfoValue = patioTraseroSubirInfo.value;
    var wifiSubirInfoValue = wifiSubirInfo.value;
    var amuebladaSubirInfoValue = amuebladaSubirInfo.value;
    var estadoSubirInfoValue = estadoSubirInfo.value;
    var personasSubirInfoValue = personasSubirInfo.value;
    var zonaSubirInfoValue = zonaSubirInfo.value;
    var coloniaSubirInfoValue = coloniaSubirInfo.value;
    var calleSubirInfoValue = calleSubirInfo.value;

    // Impresion en Consola
    console.log('El titulo es: '+tituloSubirInfoValue)
    console.log('La explicaion es: '+explicaionSubirInfoValue)
    console.log('El precio es: '+precioSubirInfoValue)
    console.log('El tipo es: '+tipoSubirInfoValue)
    console.log('Las habitaciones son: '+habitacionesSubirInfoValue)
    console.log('Las salas son: '+salasSubirInfoValue)
    console.log('Los baños son: '+bañosSubirInfoValue)
    console.log('Los metros son: '+metrosSubirInfoValue)
    console.log('El aire acondicionado es: '+aireAcondicionadoSubirInfoValue)
    console.log('La edad de la casa es: '+edadCasaSubirInfoValue)
    console.log('El patio trasero es: '+patioTraseroSubirInfoValue)
    console.log('El wifi es: '+wifiSubirInfoValue)
    console.log('La casa esta amueblada: '+amuebladaSubirInfoValue)
    console.log('El estado es: '+estadoSubirInfoValue)
    console.log('Las personas son: '+personasSubirInfoValue)
    console.log('La zona es: '+zonaSubirInfoValue)
    console.log('La colonia es: '+coloniaSubirInfoValue)
    console.log('La calle es: '+calleSubirInfoValue)
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

    // Impresion en Consola
    console.log('El nombre es: '+nombreContactoValue)
    console.log('El email es: '+emailContactoValue)
    console.log('El celular es: '+celularContactoValue)
    console.log('El telefono es: '+telefonoContactoValue)
    console.log('La red social es: '+redSocialContactoValue)
}