angular.module 'app.directive', ['app.controller']

.directive 'appNavigation', ->
    controller: 'NavigationController'

.directive 'appModalPost', ['$injector', ($injector) ->
    scope: yes
    link: (scope, element) ->
        # providers
        $app = $injector.get '$app'

        # listen
        scope.$on $app.broadcastChannel.showCreatePost, (self, object) ->
            scope.title = object.title
            scope.content = object.content
            scope.submit = ($event) ->
                $event.preventDefault()
                object?.submitCallback
                    title: scope.title
                    content: scope.content
            $(element).modal 'show'
        scope.$on $app.broadcastChannel.hideCreatePost, ->
            $(element).modal 'hide'

        # element events
        $(element).on 'shown.bs.modal', ->
            $(element).find('input:first').select()
]
