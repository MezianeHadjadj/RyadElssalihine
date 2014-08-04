
app.controller('sidebarController', ['$scope','User', function($scope,User){
      
        User.get($scope)
    	User.tabs($scope);
    	User.footers($scope);


}]); 