document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('photo').addEventListener('change', previewPhoto);
});

function previewPhoto(event) {
    console.log("Функция previewPhoto вызвана");
    const file = event.target.files[0];
    console.log("Загруженный файл:", file); // Логируем загруженный файл

    if (!file) {
        console.log("Нет файла для отображения.");
        return; // Если файла нет, выходим из функции
    }

    const reader = new FileReader();

    reader.onload = function(e) {
        const imgElement = document.getElementById('myapp-user-photo');
        if (imgElement) { // Проверьте существование элемента
            imgElement.src = e.target.result;

            imgElement.style.display = 'block'; // Показываем изображение
            imgElement.style.width = '100%';
            imgElement.style.height = '100%';
            imgElement.style.objectFit = 'cover'; // Подгоняем изображение по размеру контейнера
            console.log("Изображение загружено и отображается.");
        } else {
            console.error("Элемент изображения не найден.");
        }
    }

    reader.readAsDataURL(file);
}