angular.module 'app.controller', []

.controller 'NavigationController', ['$scope', '$injector', ($scope, $injector) ->
    # providers
    $app = $injector.get '$app'
    $state = $injector.get '$state'
    $validator = $injector.get '$validator'

    $scope.user = $app.user
    $scope.showCreatePostModal = ($event) ->
        $event.preventDefault()

        if not $app.user.is_login
            $app.modal.loginRequired.show()
            return

        $app.modal.post.showCreate
            submitCallback: (model) ->
                $validator.validate $scope
                .success ->
                    $app.store.addPost model.title, model.content
                    .success ->
                        $state.go $state.$current, null, reload: yes
                        $app.modal.post.hideCreate()
]

.controller 'PostsController', ['$scope', 'posts', ($scope, posts) ->
    $scope.posts = posts
]
