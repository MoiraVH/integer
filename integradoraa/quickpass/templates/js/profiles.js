// Seleccionar elementos
const fileInput = document.getElementById('fileInput');
const uploadBtn = document.getElementById('uploadBtn');
const fileName = document.getElementById('fileName');
const preview = document.getElementById('preview');
const menuItems = document.querySelectorAll('.menu-item');
const initialsElement = document.getElementById('initials');
const usernameElement = document.getElementById('username');

// Evento para cambiar menú activo
menuItems.forEach(item => {
    item.addEventListener('click', () => {
        menuItems.forEach(i => i.classList.remove('active'));
        item.classList.add('active');
    });
});

// Evento para abrir el selector de archivos
uploadBtn.addEventListener('click', () => {
    fileInput.click();
});

// Evento cuando se selecciona un archivo
fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    
    if (file) {
        fileName.textContent = file.name;
        
        // Crear una vista previa de la imagen
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.innerHTML = `<img src="${e.target.result}" alt="Vista previa" style="max-width: 100%; max-height: 100%;">`;
            
            // Actualizar también la imagen del avatar en la barra lateral
            const avatar = document.querySelector('.avatar');
            avatar.innerHTML = `<img src="${e.target.result}" alt="Avatar" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;">`;
        };
        reader.readAsDataURL(file);
    }
});

// Función para actualizar nombre e iniciales
function updateProfile(name) {
    usernameElement.textContent = name;
    
    // Obtener iniciales
    const nameParts = name.split(' ');
    let initials = '';
    nameParts.forEach(part => {
        if (part.length > 0) {
            initials += part[0].toUpperCase();
        }
    });
    
    initialsElement.textContent = initials;
}

// Ejemplo para cambiar el nombre (podría ser parte de otra funcionalidad)
// updateProfile('Moira Villalobos');