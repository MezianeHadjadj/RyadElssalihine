
app.controller('calendarController', ['$scope','Calendar', function($scope,Calendar){

//Calendar.getSettings();




	$(document).ready(function() {

    // page is now ready, initialize the calendar...

    $('#calendar').fullCalendar({

    	lang:"ar",
 
    })

});


}]); 