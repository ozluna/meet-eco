window.onscroll = function () {
    scrollFunction();
};

/**
 * Hides navbar when user scrolls down.
 */
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        $(".navbar").addClass('d-none');
    } else {
        $(".navbar").removeClass('d-none');
    }
}

$('.navbar-toggler-icon').click(function() {
    $('.navbar').toggleClass('bg-white');
})

/** date picker initilazitaion  */

 $(document).ready(function(){
                $('.datepicker').datepicker();
            });