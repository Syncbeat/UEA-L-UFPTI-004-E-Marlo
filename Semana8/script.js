document.addEventListener('DOMContentLoaded', () => {
    
    const btnAlerta = document.getElementById('btnAlerta');
    btnAlerta.addEventListener('click', () => {
        alert('Prueba de interacción con JavaScript y Bootstrap');
    });

    const form = document.getElementById('contactForm');

    form.addEventListener('submit', (event) => {
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        } else {
            event.preventDefault();
            alert('Los datos fueron enviados con exito. Nos contactaremos pronto.');
            form.reset();
            form.classList.remove('was-validated');
            return;
        }

        form.classList.add('was-validated');
    }, false);
});