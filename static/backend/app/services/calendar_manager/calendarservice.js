
var calendarservices = angular.module('calendar_manager.calendarservices',[]);

calendarservices.factory('Calendar', function($http) {
  

  var Calendar = function(data) {
    angular.extend(this, data);
  }

Calendar.getSettings=function(){

 $http.get('user/user/1').success(function(data, status, headers, config) {
         console.log(data);
}).error(function(data, status, headers, config) {
// Handle the error
console.log(status);
});

};


return Calendar ;

});
