// static/myapp/js/scripts.js

let isGojo = false;
let snowInterval;
let isSnowing = false;

function changeAvatar() {
    const avatar = document.getElementById('avatarImage');
    if (isGojo) {
        avatar.src = avatar.dataset.originalSrc;
    } else {
        avatar.src = avatar.dataset.alternateSrc;
    }
    isGojo = !isGojo;
}

function createSnowflake() {
    if (!isSnowing) return;

    const snowflake = document.createElement('div');
    snowflake.className = 'snowflake';
    snowflake.innerHTML = '❄';
    snowflake.style.left = Math.random() * 100 + 'vw';
    snowflake.style.opacity = Math.random() * 0.7 + 0.3;
    snowflake.style.fontSize = (Math.random() * 8 + 6) + 'px';
    snowflake.style.animationDuration = (Math.random() * 5 + 5) + 's';

    document.body.appendChild(snowflake);

    setTimeout(() => {
        snowflake.remove();
    }, 10000);
}

function toggleSnow() {
    const toggleButton = document.getElementById('snowToggle');
    isSnowing = !isSnowing;

    if (isSnowing) {
        toggleButton.textContent = '❄️ Выкл';
        toggleButton.style.background = 'rgba(173, 216, 230, 0.9)';
        snowInterval = setInterval(createSnowflake, 100);
    } else {
        toggleButton.textContent = '❄️ Снег';
        toggleButton.style.background = 'rgba(255, 255, 255, 0.9)';
        clearInterval(snowInterval);
        document.querySelectorAll('.snowflake').forEach(snowflake => {
            snowflake.remove();
        });
    }
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    // Инициализация аватара
    const avatar = document.getElementById('avatarImage');
    if (avatar) {
        avatar.dataset.originalSrc = "{% static 'myapp/images/avatar.png' %}";
        avatar.dataset.alternateSrc = "{% static 'myapp/images/Gojo.jpeg' %}";
    }
});