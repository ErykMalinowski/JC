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

    let mySwiper = new Swiper('.swiper-container', {
        slidesPerView: 1,
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

    // select round

    const select = document.querySelector('.select-round');

    select.addEventListener('change', (event) => {
        const round = document.querySelector('.round');
        round.textContent = `Wyniki kolejki ${event.target.value}`;
    });
});