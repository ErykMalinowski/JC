document.addEventListener("DOMContentLoaded", () => {

    // show/hide mobile menu & prevent scrolling body when mobile menu opened

    const hamburger = document.querySelector('.hamburger');
    const nav = document.querySelector('.page-navigation');

    const handleClick = () => {
        hamburger.classList.toggle('hamburger--active');
        nav.classList.toggle('page-navigation--visible');
        document.documentElement.classList.toggle("lock-scroll");
    }

    hamburger.addEventListener('click', handleClick);

    // click outside menu to close it

    window.addEventListener("click", e => {
        if (
            document
            .querySelector(".page-navigation")
            .classList.contains("page-navigation--visible")
        ) {
            if (!e.composedPath().includes(document.querySelector(".page-header"))) {
                document
                    .querySelector(".page-navigation")
                    .classList.remove("page-navigation--visible");
                document
                    .querySelector('.hamburger')
                    .classList.remove("hamburger--active");
                document.documentElement.classList.remove("lock-scroll");
            }
        }
    })

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

    const mySwiper = new Swiper('.swiper-container', {
        slidesPerView: 2,
        loop: true,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        a11y: {
            prevSlideMessage: 'Poprzedni slajd',
            nextSlideMessage: 'Następny slajd',
        },

        breakpoints: {
            450: {
                slidesPerView: 3,
                loop: true,
            },
            600: {
                slidesPerView: 4,
                loop: true,
            },
            700: {
                slidesPerView: 5,
                loop: true,
            },
            800: {
                slidesPerView: 6,
                loop: true,
            },
            901: {
                slidesPerView: 7,
                loop: false,
            },
        }
    })

    // STATS site
    // select round

    const select = document.querySelector('.content-select');

    if (select) {
        select.addEventListener('change', (e) => {
            document.querySelector('input[type="hidden"]').value = e.target.value;
        });
    }
});