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

.directive 'appPager', ->
    scope:
        pageList: '=appPager'
        urlTemplate: '@pagerUrlTemplate'
    template:
        """
        <ul class="pagination">
            <li ng-class="{disabled: !links.previous.enable}">
                <a ng-href="{{ links.previous.url }}">&laquo;</a>
            </li>

            <li ng-repeat='item in links.numbers'
                ng-if='item.show'
                ng-class='{active: item.isCurrent}'>
                <a ng-href="{{ item.url }}">{{ item.pageNumber }}</a>
            </li>

            <li ng-class="{disabled: !links.next.enable}">
                <a ng-href="{{ links.next.url }}">&raquo;</a>
            </li>
        </ul>
        """
    link: (scope) ->
        scope.links =
            previous:
                enable: scope.pageList.has_previous_page
                url: scope.urlTemplate.replace '#{index}', scope.pageList.index - 1
            numbers: []
            next:
                enable: scope.pageList.has_next_page
                url: scope.urlTemplate.replace '#{index}', scope.pageList.index + 1

        for index in [(scope.pageList.index - 3)..(scope.pageList.index + 3)] by 1
            scope.links.numbers.push
                show: index is scope.pageList.index or index >= 0 and index <= scope.pageList.max_index
                isCurrent: index is scope.pageList.index
                pageNumber: index + 1
                url: scope.urlTemplate.replace '#{index}', index
