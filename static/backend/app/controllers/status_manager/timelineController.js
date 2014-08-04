
app.controller('timelineController', ['$scope','User','Status',function($scope,User,Status){
	

    // get list status by user !
          Status.list($scope)
      $scope.status_it_comes= false ;  
		  $scope.fileProgress=false;
	
   $scope.showProgressing= function(){
   	$scope.fileProgress=true;
   }
   
    $scope.shareStatus= function(status_object){
          Status.add($scope,status_object);  
    }






}]); 