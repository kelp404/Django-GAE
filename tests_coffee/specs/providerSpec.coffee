describe 'app.provider', ->
    fakeModule = null
    appProvider = null

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

    beforeEach ->
        fakeModule = angular.module 'fakeModule', ['app']
        fakeModule.config ($appProvider) ->
            appProvider = $appProvider
    beforeEach module('fakeModule')


    describe '$app.broadcastChannel', ->
        it '$app.broadcastChannel object check.', inject ($app) ->
            expect($app.broadcastChannel).toEqual
                showCreatePost: '$showCreatePost'
                hideCreatePost: '$hideCreatePost'
                showLoginRequired: '$showLoginRequired'


    describe '$app.user', ->
        it '$app.user is equal to window.user.', inject ($app) ->
            expect($app.user).toBe window.user


    describe '$app.modal.loginRequired', ->
        it '$app.modal.loginRequired.show() will call $rootScope.$broadcast().', inject ($injector) ->
            $rootScope = $injector.get '$rootScope'
            $app = $injector.get '$app'

            spyOn $rootScope, '$broadcast'
            .andCallFake (modal) ->
                expect(modal).toEqual $app.broadcastChannel.showLoginRequired
            $app.modal.loginRequired.show()
            expect($rootScope.$broadcast).toHaveBeenCalled()


    describe '$app', ->
        it '$app.broadcastChannel and $appProvider.broadcastChannel are the same object.', inject ($app) ->
            expect($app.broadcastChannel).toBe appProvider.broadcastChannel
        it '$app.user and $appProvider.user are the same object.', inject ($app) ->
            expect($app.user).toBe appProvider.user
        it '$app.modal and $appProvider.modal are the same object.', inject ($app) ->
            expect($app.modal).toBe appProvider.modal
        it '$app.http and $appProvider.http are the same object.', inject ($app) ->
            expect($app.http).toBe appProvider.http
        it '$app.store and $appProvider.store are the same object.', inject ($app) ->
            expect($app.store).toBe appProvider.store
        it '$app.popMessage and $appProvider.popMessage are the same object.', inject ($app) ->
            expect($app.popMessage).toBe appProvider.popMessage
