// Referencias a los elementos
const form = document.getElementById('formulario');
const btnEnviar = document.getElementById('btnEnviar');
const btnReset = document.getElementById('btnReset');

// Elementos de los inputs
const nombre = document.getElementById('nombre');
const correo = document.getElementById('correo');
const pass = document.getElementById('pass');
const confirm = document.getElementById('confirm');
const edad = document.getElementById('edad');

// Función principal que valida TODO
function validar() {
    // 1. Definir las reglas (true si cumple, false si no)
    const nombreOk = nombre.value.length >= 3;
    const correoOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(correo.value);
    const passOk = /^(?=.*\d)(?=.*[\W_]).{8,}$/.test(pass.value); // minimo 8 chars, 1 número, 1 símbolo
    const confirmOk = confirm.value === pass.value && pass.value !== "";
    const edadOk = parseInt(edad.value) >= 18;

    //Mostrar u ocultar errores visuales (llamamos a una función pequeñita abajo)
    mostrarEstado(nombre, document.getElementById('msgNombre'), nombreOk, "Mínimo 3 caracteres");
    mostrarEstado(correo, document.getElementById('msgCorreo'), correoOk, "Correo inválido");
    mostrarEstado(pass, document.getElementById('msgPass'), passOk, "Faltan requisitos (8 chars, #, $)");
    mostrarEstado(confirm, document.getElementById('msgConfirm'), confirmOk, "No coinciden");
    mostrarEstado(edad, document.getElementById('msgEdad'), edadOk, "Debes tener 18+");

    //Habilitar botón solo si los campos estan completos y correctos
    if (nombreOk && correoOk && passOk && confirmOk && edadOk) {
        btnEnviar.disabled = false;
    } else {
        btnEnviar.disabled = true;
    }
}

// Auxiliar con color rojo/verde y mensajes 
function mostrarEstado(input, span, esValido, mensajeError) {
    if (esValido) {
        input.classList.remove('error');
        input.classList.add('valido');
        span.textContent = ""; // Borrar mensaje
    } else {
        input.classList.remove('valido');
        // Solo mostramos el error rojo si el usuario ya escribió algo
        if (input.value.length > 0) {
            input.classList.add('error');
            span.textContent = mensajeError;
        } else {
            input.classList.remove('error'); // Limpio si borran todo
            span.textContent = "";
        }
    }
}

// Detecta cada vez que escribes algo en cualquier campo del formulario
form.addEventListener('input', validar);

// Botón de reinicio
btnReset.addEventListener('click', () => {
    form.reset();
    // Limpiar estilos manuales
    document.querySelectorAll('input').forEach(i => i.classList.remove('valido', 'error'));
    document.querySelectorAll('.mensaje').forEach(s => s.textContent = "");
    btnEnviar.disabled = true;
});