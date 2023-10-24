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

function nextMirarInfo() {
    contacto();
}

function nextContacto() {
    // Variables para los inputs
    var nombreContacto = document.getElementById("nombreContacto");
    var emailContacto = document.getElementById("emailContacto");
    var telefonoContacto = document.getElementById("telefonoContacto");
    var redSocialContacto = document.getElementById("redSocialContacto");

    // Variables de Valores
    var nombreContactoValue = nombreContacto.value;
    var emailContactoValue = emailContacto.value;
    var telefonoContactoValue = telefonoContacto.value;
    var redSocialContactoValue = redSocialContacto.value;

}

function sendData() {
    var alojamientoSubirInfoValue = document.getElementById("alojamientoSubirInfo").value;
    var tituloSubirInfoValue = document.getElementById("tituloSubirInfo").value;
    var explicacionSubirInfoValue = document.getElementById("explicacionSubirInfo").value;
    var precioSubirInfoValue = document.getElementById("precioSubirInfo").value;
    var habitacionesSubirInfoValue = document.getElementById("habitacionesSubirInfo").value;
    var salasSubirInfoValue = document.getElementById("salasSubirInfo").value;
    var bañosSubirInfoValue = document.getElementById("bañosSubirInfo").value;
    var metrosSubirInfoValue = document.getElementById("metrosSubirInfo").value;
    var edadCasaSubirInfoValue = document.getElementById("edadCasaSubirInfo").value;
    var cocheraSubirInfoValue = document.getElementById("cocheraSubirInfo").value;
    var wifiSubirInfoValue = document.getElementById("wifiSubirInfo").value;
    var televisionSubirInfoValue = document.getElementById("televisionSubirInfo").value;
    var amuebladaSubirInfoValue = document.getElementById("amuebladaSubirInfo").value;
    var aireAcondicionadoSubirInfoValue = document.getElementById("aireAcondicionadoSubirInfo").value;
    var estadoSubirInfoValue = document.getElementById("estadoSubirInfo").value;
    var personasSubirInfoValue = document.getElementById("personasSubirInfo").value;
    var zonaSubirInfoValue = document.getElementById("zonaSubirInfo").value;
    var coloniaSubirInfoValue = document.getElementById("coloniaSubirInfo").value;
    var calleSubirInfoValue = document.getElementById("calleSubirInfo").value;
    var mapaUbicacionValue = document.getElementById("mapaUbicacion").getAttribute("src");
    var imagenPropiedadValue = document.getElementById("imagenPropiedad").files[0];
    var imalength = imagenPropiedadValue.length;

    var nombreContactoValue = document.getElementById("nombreContacto").value;
    var emailContactoValue = document.getElementById("emailContacto").value;
    var telefonoContactoValue = document.getElementById("telefonoContacto").value;
    var redSocialContactoValue = document.getElementById("redSocialContacto").value;

    var fotoContactoValue = document.getElementById("fotoContacto").files[0];
    var documentosContactoValue = document.getElementById("documentosContacto").files[0];
    var doclength = documentosContactoValue.length;

    // var data = {
    //     alojamiento: alojamientoSubirInfoValue,
    //     titulo: tituloSubirInfoValue,
    //     explicacion: explicacionSubirInfoValue,
    //     precio: precioSubirInfoValue,
    //     habitaciones: habitacionesSubirInfoValue,
    //     salas: salasSubirInfoValue,
    //     banos: bañosSubirInfoValue,
    //     metros: metrosSubirInfoValue,
    //     edadCasa: edadCasaSubirInfoValue,
    //     cochera: cocheraSubirInfoValue,
    //     wifi: wifiSubirInfoValue,
    //     television: televisionSubirInfoValue,
    //     amueblada: amuebladaSubirInfoValue,
    //     aireAcondicionado: aireAcondicionadoSubirInfoValue,
    //     estado: estadoSubirInfoValue,
    //     personas: personasSubirInfoValue,
    //     zona: zonaSubirInfoValue,
    //     colonia: coloniaSubirInfoValue,
    //     calle: calleSubirInfoValue,
    //     mapaUbicacion: mapaUbicacionValue,
    //     imagenPropiedad: imagenPropiedadValue,
    //     nombreContacto: nombreContactoValue,
    //     emailContacto: emailContactoValue,
    //     telefonoContacto: telefonoContactoValue,
    //     redSocialContacto: redSocialContactoValue,
    //     fotoContacto: fotoContactoValue,
    //     documentosContacto: documentosContactoValue
    // };

    var data = new FormData();
    data.append('alojamiento', alojamientoSubirInfoValue);
    data.append('titulo', tituloSubirInfoValue);
    data.append('explicacion', explicacionSubirInfoValue);
    data.append('precio', precioSubirInfoValue);
    data.append('habitaciones', habitacionesSubirInfoValue);
    data.append('salas', salasSubirInfoValue);
    data.append('banos', bañosSubirInfoValue);
    data.append('metros', metrosSubirInfoValue);
    data.append('edadCasa', edadCasaSubirInfoValue);
    data.append('cochera', cocheraSubirInfoValue);
    data.append('wifi', wifiSubirInfoValue);
    data.append('television', televisionSubirInfoValue);
    data.append('amueblada', amuebladaSubirInfoValue);
    data.append('aireAcondicionado', aireAcondicionadoSubirInfoValue);
    data.append('estado', estadoSubirInfoValue);
    data.append('personas', personasSubirInfoValue);
    data.append('zona', zonaSubirInfoValue);
    data.append('colonia', coloniaSubirInfoValue);
    data.append('calle', calleSubirInfoValue);
    data.append('mapaUbicacion', mapaUbicacionValue);
    data.append('imagenPropiedad', imagenPropiedadValue);
    data.append('nombreContacto', nombreContactoValue);
    data.append('emailContacto', emailContactoValue);
    data.append('telefonoContacto', telefonoContactoValue);
    data.append('redSocialContacto', redSocialContactoValue);
    data.append('fotoContacto', fotoContactoValue);
    data.append('documentosContacto', documentosContactoValue);

    // Realiza una solicitud AJAX (POST) para enviar los datos a tu aplicación Flask
    fetch('/anunciar', {
        method: 'POST',
        body: data
    })
    .then(response => response.json())
    .then(data => {
        // Maneja la respuesta de tu aplicación Flask aquí
        console.log(data);
    })
    .catch(error => {
        console.error('Error al enviar datos:', error);
    });

    // $.ajax({
    //     url: '/anunciar',
    //     type: 'POST',
    //     data: data,
    //     processData: false,
    //     contentType: false,
    //     success: function(response) {
    //         console.log(response);
    //     },
    //     error: function(error) {
    //         console.log(error);
    //     }
    // });

    anuncioExitoso();
}

function validateData() {
    if (document.getElementById("tituloSubirInfo").value == "") {
        alert("Por favor, ingresa el titulo de la propiedad");
    }
    else if (document.getElementById("explicacionSubirInfo").value == "") {
        alert("Por favor, ingresa una explicacion de la propiedad");
    }
    else if (document.getElementById("precioSubirInfo").value == "") {
        alert("Por favor, ingresa el precio de la propiedad");
    }
    else if (document.getElementById("habitacionesSubirInfo").value == "") {
        alert("Por favor, ingresa el numero de habitaciones");
    }
    else if (document.getElementById("salasSubirInfo").value == "") {
        alert("Por favor, ingresa el numero de salas");
    }
    else if (document.getElementById("bañosSubirInfo").value == "") {
        alert("Por favor, ingresa el numero de baños");
    }
    else if (document.getElementById("metrosSubirInfo").value == "") {
        alert("Por favor, ingresa los metros cuadrados de la propiedad");
    }
    else if (document.getElementById("edadCasaSubirInfo").value == "") {
        alert("Por favor, ingresa la edad de la propiedad");
    }
    else if (document.getElementById("personasSubirInfo").value == "") {
        alert("Por favor, ingresa el numero de personas que pueden vivir en la propiedad");
    }
    else if (document.getElementById("zonaSubirInfo").value == "") {
        alert("Por favor, ingresa la zona de la propiedad");
    }
    else if (document.getElementById("coloniaSubirInfo").value == "") {
        alert("Por favor, ingresa la colonia de la propiedad");
    }
    else if (document.getElementById("calleSubirInfo").value == "") {
        alert("Por favor, ingresa la calle de la propiedad");
    }
    else if (document.getElementById("mapaUbicacion").getAttribute("src") == "") {
        alert("Por favor, ingresa la ubicacion de la propiedad");
    }
    else if (document.getElementById("nombreContacto").value == "") {
        alert("Por favor, ingresa el nombre del contacto");
    }
    else if (document.getElementById("emailContacto").value == "") {
        alert("Por favor, ingresa el email del contacto");
    }
    else if (document.getElementById("telefonoContacto").value == "") {
        alert("Por favor, ingresa el telefono del contacto");
    }
    else if (document.getElementById("redSocialContacto").value == "") {
        alert("Por favor, ingresa la red social del contacto");
    }
    else if (document.getElementById("fotoContacto").value == "") {
        alert("Por favor, ingresa la foto del contacto");
    }
    else if (document.getElementById("documentosContacto").value == "") {
        alert("Por favor, ingresa los documentos del contacto");
    }
    else {
        sendData();
    }
}

