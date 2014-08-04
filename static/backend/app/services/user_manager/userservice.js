
var userservices = angular.module('user_manager.userservices',[]);

userservices.factory('User', function($http) {
  

  var User = function(data) {
    angular.extend(this, data);
  }

User.login=function(user){

  
 $http.post('user/login',user).success(function(data, status, headers, config) {

         console.log(data);
}).error(function(data, status, headers, config) {
// Handle the error
console.log(status);
});

};
User.get=function($scope){
 $http.get('/user/user/').success(function(data, status, headers, config) {
            $scope.user=data
        
}).error(function(data, status, headers, config) {
// Handle the error
  
});	

}


User.tabs= function($scope){
	$http.get('/user/tabs').success(function(data, status, headers, config) {

         $scope.tabs=data;
         
}).error(function(data, status, headers, config) {
// Handle the error
console.log(status);
});

};

User.footers= function($scope){
	$http.get('/user/footers').success(function(data, status, headers, config) {

         $scope.footers=data;
         console.log(data)
}).error(function(data, status, headers, config) {
// Handle the error
console.log(status);
});

};
return User ;

});