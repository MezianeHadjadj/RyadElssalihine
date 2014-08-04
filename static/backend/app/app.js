var app = angular.module('backend',['calendar_manager.calendarservices','user_manager.userservices','status_manager.statusservice']);

app.config(function($interpolateProvider){
  $interpolateProvider.startSymbol('<%');
  $interpolateProvider.endSymbol('%>');
});



app.config(['$routeProvider', function($routeProvider) {
     $routeProvider.
         when('/', {
        controller: 'timelineController',        
        templateUrl:'/status/status_show'
      }). when('/calendar/', {
        controller: 'calendarController',        
        templateUrl:'/calendar/calendar_show'
      })
      
      
     ;

 }]) ;
