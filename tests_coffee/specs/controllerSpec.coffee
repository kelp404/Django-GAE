describe 'app.controller', ->
    beforeEach module('app')
    beforeEach ->
        # mock NProgress
        window.NProgress =
            configure: ->

        # mock user
        window.user =
            is_login: no
            id: 0
            permission: 0 # anonymous
            name: 'Guest'
            email: 'user@email.com'
            login_url: 'url'
            logout_url: 'url'


    describe 'NavigationController', ->
        $scope = null
        $event = null
        controller = null

        beforeEach inject ($injector) ->
            $rootScope = $injector.get '$rootScope'
            $controller = $injector.get '$controller'
            $scope = $rootScope.$new()
            controller = $controller 'NavigationController',
                $scope: $scope
                $injector: $injector
            $event =
                preventDefault: jasmine.createSpy 'preventDefault'

        describe '$scope.user', ->
            it '$scope.user is equal to $app.user.', inject ($app) ->
                expect($scope.user).toBe $app.user

        describe '$scope.showCreatePostModal()', ->
            it '$scope.showCreatePostModal($event) will call $event.preventDefault().', ->
                $scope.showCreatePostModal $event
                expect($event.preventDefault).toHaveBeenCalled()

            it '$scope.showCreatePostModal() will call $app.modal.loginRequired.show() if did not login.', inject ($app) ->
                $app.user.is_login = no
                spyOn $app.modal.loginRequired, 'show'
                $scope.showCreatePostModal $event
                expect($app.modal.loginRequired.show).toHaveBeenCalled()

            it '$scope.showCreatePostModal() will call $app.modal.post.showCreate if logined.', inject ($app) ->
                $app.user.is_login = yes
                spyOn $app.modal.post, 'showCreate'
                $scope.showCreatePostModal $event
                expect($app.modal.post.showCreate).toHaveBeenCalled()


    describe 'PostsController', ->
        $scope = null
        controller = null
        posts =
            index: 0
            size: 10
            items: []

        beforeEach inject ($injector) ->
            $rootScope = $injector.get '$rootScope'
            $controller = $injector.get '$controller'
            $scope = $rootScope.$new()
            controller = $controller 'PostsController',
                $scope: $scope
                $injector: $injector
                posts: posts

        describe '$scope.posts', ->
            it '$scope.posts is equal to the third argument.', ->
                expect($scope.posts).toBe posts

        describe '$scope.deletePost()', ->
            it '$scope.deletePost($event, id) will call $app.store.deletePost().', inject ($app) ->
                $event =
                    preventDefault: jasmine.createSpy 'preventDefault'
                spyOn $app.store, 'deletePost'
                .andCallFake (id) ->
                    expect(id).toBe 10
                    success: ->

                $scope.deletePost $event, 10
                expect($event.preventDefault).toHaveBeenCalled()
                expect($app.store.deletePost).toHaveBeenCalled()
