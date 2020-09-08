window.onscroll = function () {
    scrollFunction();
};

/**
 * Hides navbar when user scrolls down.*/
 
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

/** event_category selection */

  $(document).ready(function(){
    $('select').formSelect();
  })

  
    //modal button trigger 
$('#attender').on('shown.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var recipient = button.data('whatever') // Extract info from data-* attributes 
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.modal-title').text('New message to ' + recipient)
  modal.find('.modal-body input').val(recipient)
})


 $(window).on('load',function(){
        $('#eventKey').modal('show');
    });

   document.getElementById('gotoevent{{id|safe}}').addEventListener("click",
   function (event){
       console.log('I am working')
       event.preventDefault();
       const id1 = document.getElementById('id_no').value;
       const id2 = document.getElementById('idcheck').value;
       if ( id1 != id2){
           
           const result = document.getElementById('errorMessage').innerHTML = 'Id you enter is wrong. Please try again';  
           return   result;   
       }
       else
         {
             const result = document.getElementById('myform').submit;
            return result;
        }
   });