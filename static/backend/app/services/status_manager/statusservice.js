
var statusservice = angular.module('status_manager.statusservice',[]);

statusservice.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.common['X-CSRFToken'] = '{{ csrf_token|escapejs }}';
}]);

statusservice.factory('Status', function($http) {
  

  var Status = function(data) {
    angular.extend(this, data);
  }


Status.list= function($scope){
	$http.get('/status/status/').success(function(data, status, headers, config) {

         $scope.status_list=data;
         console.log($scope.status_list)
}).error(function(data, status, headers, config) {
// Handle the error
console.log(status);
});

};

Status.add= function($scope,status_object){

	
	console.log(status_object)
	$http.post('/status/add', status_object).success(function(data, status, headers, config) {
    $scope.new_status=data;
    $scope.status_it_comes=true ;
          
}).error(function(data, status, headers, config) {
// Handle the error
console.log(status);
});
}

return Status ;

});