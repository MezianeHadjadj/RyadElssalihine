
var userservices = angular.module('user_manager.userservices',[]);

userservices.factory('User', function($http) {
  

  var User = function(data) {
    angular.extend(this, data);
  }

User.login=function(user){
  console.log("here it is !")
  console.log(user)
  
 $http.post('user/login',user).success(function(data, status, headers, config) {

         console.log(data);
}).error(function(data, status, headers, config) {
// Handle the error
console.log(status);
});

};


return User ;

});