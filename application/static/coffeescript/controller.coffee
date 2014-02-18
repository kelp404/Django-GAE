angular.module 'app.controller', []

.controller 'NavigationController', ['$scope', '$injector', ($scope, $injector) ->
    # providers
    $app = $injector.get '$app'
    $state = $injector.get '$state'

    $scope.user = $app.user
    $scope.showCreatePostModal = ($event) ->
        $event.preventDefault()
        $app.modal.post.showCreate
            submitCallback: (model) ->
                $app.store.addPost model.title, model.content
                .success ->
                    $state.go $state.$current, null, reload: yes
                    $app.modal.post.hideCreate()
]

.controller 'PostsController', ['$scope', 'posts', ($scope, posts) ->
    $scope.posts = posts
]
