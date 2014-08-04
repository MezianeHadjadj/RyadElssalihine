var app = angular.module('frontend',['user_manager.userservices']);

app.config(function($interpolateProvider){
  $interpolateProvider.startSymbol('<%');
  $interpolateProvider.endSymbol('%>');
});

app.config(['$routeProvider', function($routeProvider) {
     $routeProvider.
     when('/', {
        controller: 'welcomeController',        
        templateUrl:'/welcome'
      })
    
     ;

 }]) ;
