var container = document.querySelector('.movies-container');
var sliderOne = document.querySelector('.slider');
// the scroll width is 95% of the container width
var scrollWidth = container.offsetWidth * 0.95;
function scrollToLeft() {
    container.scrollBy({
        left: -scrollWidth,
        behavior: 'smooth'
    });
}
function scrollToRight() {
    container.scrollBy({
        left: scrollWidth,
        behavior: 'smooth'
    });
}