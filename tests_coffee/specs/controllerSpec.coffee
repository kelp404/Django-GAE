describe 'app.controller', ->
    beforeEach module('app')
    beforeEach ->
        # mock NProgress
        window.NProgress =
            configure: ->

    describe 'PostsController', ->
        $scope = null
        controller = null
        posts =
            index: 0
            size: 10
            items: []

        beforeEach inject ($rootScope, $controller, $injector) ->
            $scope = $rootScope.$new()
            controller = $controller 'PostsController',
                $scope: $scope
                $injector: $injector
                posts: posts

        describe '$scope.posts', ->
            it '$scope.posts is equal to the third argument.', ->
                expect($scope.posts).toBe posts
