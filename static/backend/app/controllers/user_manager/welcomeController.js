
app.controller('welcomeController', ['$scope','User', function($scope,User){
    $scope.register_form=false ;


$("#id_username").addClass("form-control");
$("#id_password").addClass("form-control");

$scope.login= function(user){
	
	User.login(user);
}


$scope.showRegisterForm= function(){

	$scope.register_form= true ;
}

$scope.register=function(user){
	
}




}]); 