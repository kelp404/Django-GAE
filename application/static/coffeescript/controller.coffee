angular.module 'app.controller', []

.controller 'NavigationController', ['$scope', '$injector', ($scope, $injector) ->
    # providers
    $app = $injector.get '$app'

    $scope.user = $app.user
    $scope.showCreatePostModal = ($event) ->
        $event.preventDefault()
        $app.modal.post.showCreate
            submitCallback: (model) ->
                $app.store.createPost model.title, model.content
                .success ->
                    $app.modal.post.hideCreate()
]

.controller 'PostsController', ['$scope', 'posts', ($scope, posts) ->

]
