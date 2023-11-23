function mostrarPantallaEmergente() {
    document.getElementById("miPantallaEmergente").style.display = "block";
}

function cerrarPantallaEmergente() {
    document.getElementById("miPantallaEmergente").style.display = "none";
}

function cerrarPantallaEmergente2() {
    document.getElementById("miPantallaEmergente2").style.display = "none";
}

function mostrarPantallaEmergente2() {
    if (document.getElementById("btnActivacion").textContent == "Activar propiedad") {
        document.getElementById("btnActivacion").textContent = "Desactivar propiedad";
        document.getElementById("mensajeEmergente").textContent = "¿Está seguro que quiere desactivar esta propiedad?";
        document.getElementById("mensajeEmergente2").textContent = "La propiedad ha sido activada correctamente";
        
    } else {
        document.getElementById("btnActivacion").textContent = "Activar propiedad";
        document.getElementById("mensajeEmergente").textContent = "¿Está seguro que quiere activar esta propiedad?";
        document.getElementById("mensajeEmergente2").textContent = "La propiedad ha sido desactivada correctamente";
    }

    document.getElementById("miPantallaEmergente").style.display = "none";
    document.getElementById("miPantallaEmergente2").style.display = "block";
    
}