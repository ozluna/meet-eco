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
    $('.datepicker').datepicker({
        electMonths: true, // Creates a dropdown to control month
            selectYears: 15, // Creates a dropdown of 15 years to control year,
            today: 'Today',
            clear: 'Clear',
            close: 'Ok',
            closeOnSelect: false // Close upon selecting a date,

    });
  });
    
  /**Changing the date */
   $(document).ready(function(){
            event_date = Date.parse('{{event.event_date}}');
            $('#event_date').pickadate('picker').set('select', event_date, {format:'dd/mm/yyyy'}).trigger('change')
        }) 