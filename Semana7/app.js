//Se guardan los elementos en un array con información adicional
const Productos = [
    {nombre: "Laptop", precio: 800, descripcion: "Una laptop potente para todas tus necesidades."},
    {nombre: "Smartphone", precio: 500, descripcion: "Un smartphone con excelente cámara y batería."},
    {nombre: "Tablet", precio: 300, descripcion: "Una tablet ligera y versátil para el trabajo y el ocio."},
    {nombre: "Auriculares", precio: 150, descripcion: "Auriculares con cancelación de ruido y sonido de alta calidad."},
];

//Referencia al elemento HTML donde se mostrarán los productos
const listaHTML = document.getElementById("lista-productos");

function renderizarProductos() {
    listaHTML.innerHTML = ""; 
    //Se recorre el array y se crea un elemento HTML para cada producto
    Productos.forEach(producto => {
                const elemento = `
            <li>
                <strong>${producto.nombre}</strong> - $${producto.precio}
                <br>
                <small>${producto.descripcion}</small>
            </li>
            <hr> 
        `;     
        listaHTML.innerHTML += elemento;
    });
}
renderizarProductos();

//Agregar funcionalidad al botón para agregar un nuevo producto
const botonAgregar = document.getElementById("btn-agregarprod");

// Referencias a los inputs
const inputNombre = document.getElementById("input-nombre");
const inputPrecio = document.getElementById("input-precio");
const inputDescripcion = document.getElementById("input-descripcion");

botonAgregar.addEventListener("click", function() {
    
    // Capturamos los datos de los inputs
    const nombreUsuario = inputNombre.value;
    const precioUsuario = inputPrecio.value;
    const descripcionUsuario = inputDescripcion.value;

    // Validación simple: Si está vacío, no hacemos nada (alerta)
    if(nombreUsuario === "" || precioUsuario === "" || descripcionUsuario === "") {
        alert("¡Por favor escribe un nombre, un precio y una descripción!");
        return; // Salimos de la función si no hay datos
    }

    // 2. Usamos los datos reales del usuario
    const nuevoProducto = {
        nombre: nombreUsuario,
        precio: precioUsuario,
        descripcion: descripcionUsuario
    };

    // Agregamos el nuevo producto al array y re-renderizamos la lista
    Productos.push(nuevoProducto);
    renderizarProductos();

    // Limpiamos los inputs después de agregar
    inputNombre.value = "";
    inputPrecio.value = "";
    inputDescripcion.value = "";
});