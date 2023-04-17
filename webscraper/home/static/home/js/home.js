$( document ).ready(function() {

    setTimeout(() => {
        $('.banner-text').attr('style', 'border: 3px solid white');
    }, 1000);

    setTimeout(() => {
        $('.banner-text').fadeOut(2000);
    }, 2000);

});