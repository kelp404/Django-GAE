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
                $validator.validate model.scope
                .success ->
                    $app.store.addPost model.title, model.content
                    .success ->
                        $state.go $state.$current, null, reload: yes
                        $app.modal.post.hideCreate()
]

.controller 'PostsController', ['$scope', '$injector', 'posts', ($scope, $injector, posts) ->
    # providers
    $app = $injector.get '$app'
    $state = $injector.get '$state'

    # scope
    $scope.posts = posts
    $scope.deletePost = ($event, id) ->
        $event.preventDefault()
        $app.store.deletePost id
        .success ->
            $state.go $state.$current, null, reload: yes
            $app.modal.post.hideCreate()
]
