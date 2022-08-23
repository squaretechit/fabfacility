import {
    bootstrap
} from './bootstrap/bootstrap.bundle.min.js';
import {
    owlCarosel
} from './OwlCarousel/owl.carousel.min.js';
import {
    fancyBox
} from './gallery/fancybox.min.js';

bootstrap();
jQuery();
owlCarosel();
fancyBox();

// My JS Codes
// Preloader Start
let runningAnimation = setInterval(checkAnimation, 2000);

function checkAnimation() {
    const mainPreloaderContent = document.querySelector('#animation-text'),
        preloader_id = document.querySelector('#preloader'),
        mainPreloaderText = mainPreloaderContent.getAttribute("animation-word"),
        mainIcon = mainPreloaderContent.getAttribute("favicon"),
        splitePreloaderText = mainPreloaderText.split("");

    mainPreloaderContent.innerHTML = '';

    for (let pre_i = 0; pre_i < splitePreloaderText.length; pre_i++) {
        if (splitePreloaderText[pre_i] === 's') {
            mainPreloaderContent.innerHTML += `<span class="animation-fav-logo"><img alt="Favicon Icon" src="${mainIcon}"></span>`;
            mainPreloaderContent.innerHTML += `<span class="opacity-0">a</span>`;
        } else if (splitePreloaderText[pre_i] === ' ') {
            mainPreloaderContent.innerHTML += `<span class="opacity-0">a</span>`;
        } else {
            mainPreloaderContent.innerHTML += `<span class="text-uppercase">${splitePreloaderText[pre_i]}</span>`;
        }
    };

    let countChar = 0,
        countTimer = setInterval(makeAnimation, 100);

    function makeAnimation() {
        preloader_id.classList.add('preloader_id_animation');

        const everyChar = mainPreloaderContent.querySelectorAll('span')[countChar];

        document.querySelector('#animation-text img').classList.add('fade-animation');
        everyChar.classList.add('fade-animation');
        countChar++;

        if (countChar === splitePreloaderText.length) {
            completeAnimation();
            preloader_id.classList.remove('preloader_id_animation');
            return;
        }
    };

    function completeAnimation() {
        clearInterval(countTimer);
        countTimer = null;
    };
};

// Other Js
document.addEventListener("DOMContentLoaded", () => {

    window.scrollTo({top: 0});
    // Preloaader End
    let drower = document.querySelector('#drower');
    setInterval(() => {
        clearInterval(runningAnimation);
        runningAnimation = null;
        document.querySelector('body').classList.remove('overflow-hidden');
        document.querySelector('#preloader-section').classList.add('d-none');
        drower.classList.add('open-drower');
        setInterval(() => {
            drower.classList.add('d-none');
        }, 1000);
    }, 3800);

    // Animation
    AOS.init();

    // Subscription
    const subscribe_form = document.querySelector('#subscribe'),
        csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value,
        subscrip_url = subscribe_form.getAttribute('action'),
        subscrip_email = document.querySelector('#subscription-email'),
        subscription_message = document.querySelector('#subscription-message');

    subscribe_form.addEventListener('submit', e => {
        e.preventDefault();

        if (subscrip_email.value != '' && subscrip_email.value.includes('@')) {
            fetch(subscrip_url, {
                    method: 'POST',
                    credentials: 'same-origin',
                    headers: {
                        'Accept': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': csrftoken,
                    },
                    body: JSON.stringify({
                        'email': subscrip_email.value
                    })
                })
                .then(response => {
                    return response.json()
                })
                .then(data => {
                    if (data['success']) {
                        subscription_message.innerText = data['success'];
                        subscription_message.classList.remove('alert-danger');
                        subscription_message.classList.remove('d-none');
                        subscription_message.classList.add('alert-success');
                        subscrip_email.value = '';
                    } else {
                        subscription_message.innerText = data['error'];
                        errorMessage();
                    }
                })
        } else {
            subscription_message.innerText = 'Valid Email Required.';
            errorMessage();
        }
    });

    // Error Message
    let errorMessage = () => {
        subscription_message.classList.remove('alert-success');
        subscription_message.classList.remove('d-none');
        subscription_message.classList.add('alert-danger');
    };

    // Back To Top Button
    document.addEventListener("scroll", () => {
        const back_to_top_btn = document.querySelector('#back-to-top');
        let scrollableHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight,
            GOLDEN_RATIO = 0.5;

        if ((document.documentElement.scrollTop / scrollableHeight) > GOLDEN_RATIO) {
            back_to_top_btn.style.display = "block";
        } else {
            back_to_top_btn.style.display = "none";
        }

        back_to_top_btn.addEventListener("click", () => {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });
    });

    // Sticky Header
    document.addEventListener("scroll", () => {
        const sticky_menu = document.querySelector('.main-menu-bar');
        if (window.pageYOffset > sticky_menu.offsetTop) {
            sticky_menu.classList.add('stickty-header');
        } else {
            sticky_menu.classList.remove('stickty-header');
        }
    });
});