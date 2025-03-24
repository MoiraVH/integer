// Animación de entrada en el viewport
document.addEventListener("DOMContentLoaded", () => {
    const fadeElements = document.querySelectorAll('.fade-in'); // Todos los elementos con la clase fade-in

    const options = {
        root: null, // Observamos desde el viewport
        rootMargin: '0px', // Sin margen extra
        threshold: 0.1 // Se activa cuando el 10% del elemento es visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-visible'); // Agrega la clase de animación
                observer.unobserve(entry.target); // Deja de observar el elemento
            }
        });
    }, options);

    fadeElements.forEach(element => {
        observer.observe(element); // Comienza a observar cada elemento
    });
});