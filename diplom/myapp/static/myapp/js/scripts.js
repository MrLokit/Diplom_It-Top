document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('photo').addEventListener('change', previewPhoto);
});

function previewPhoto(event) {
    console.log("Функция previewPhoto вызвана");
    const file = event.target.files[0];
    console.log("Загруженный файл:", file);

    if (!file) {
        console.log("Нет файла для отображения.");
        return;
    }

    const reader = new FileReader();

    reader.onload = function(e) {
        const imgElement = document.getElementById('myapp-user-photo');
        if (imgElement) {
            imgElement.src = e.target.result;

            imgElement.style.display = 'block';
            imgElement.style.width = '100%';
            imgElement.style.height = '100%';
            imgElement.style.objectFit = 'cover';
            console.log("Изображение загружено и отображается.");
        } else {
            console.error("Элемент изображения не найден.");
        }
    }

    reader.readAsDataURL(file);
}