angular.module 'app.controller', []

.controller 'NavigationController', ['$scope', '$injector', ($scope, $injector) ->
    # providers
    $app = $injector.get '$app'
    $scope.user = $app.user
]

.controller 'PostsController', ['$scope', 'posts', ($scope, posts) ->

]
