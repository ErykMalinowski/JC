// show/hide page navigation

const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('.page-navigation');

const handleClick = () => {
    hamburger.classList.toggle('hamburger--active');
    nav.classList.toggle('page-navigation--visible');
}

hamburger.addEventListener('click', handleClick);

// sticky header

const header = document.querySelector(".page-header");
const topOfHeader = header.offsetTop;


const stickyHeader = () => {
    if (window.scrollY > topOfHeader) {
        document.body.style.paddingTop = header.offsetHeight + 'px';
        document.body.classList.add('fixed-header');
    } else {
        document.body.style.paddingTop = 0;
        document.body.classList.remove('fixed-header');
    }
}

window.addEventListener('scroll', stickyHeader);

// slider with results

var mySwiper = new Swiper('.swiper-container', {
    slidesPerView: 1,
    loop: true,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    breakpoints: {
        400: {
            slidesPerView: 2,
            loop: true,
        },
        550: {
            slidesPerView: 3,
            loop: true,
        },
        650: {
            slidesPerView: 4,
            loop: true,
        },
        800: {
            slidesPerView: 5,
            loop: true,
        },
        950: {
            slidesPerView: 6,
            loop: true,
        },
        1000: {
            slidesPerView: 7,
            loop: false,
        },
    }
})