$(document).ready(function(){
    $('.datepicker').datepicker();
  });

function show(id, value) {
    document.getElementById(id).style.display = value ? 'block' : 'none';
}
$(window).on("unload", function() {
    document.getElementById('loading').visibility = 'visible';
    document.getElementById('page').visibility = 'hidden';
});
