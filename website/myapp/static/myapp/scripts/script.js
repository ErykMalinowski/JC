// show/hide page navigation

const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('.page-navigation');

const handleClick = () => {
    hamburger.classList.toggle('hamburger--active');
    nav.classList.toggle('page-navigation--visible');
}

hamburger.addEventListener('click', handleClick);