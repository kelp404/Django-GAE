angular.module 'app.router', ['app.provider', 'app.controller', 'ui.router']

.config ['$stateProvider', '$urlRouterProvider', ($stateProvider, $urlRouterProvider) ->
    $urlRouterProvider.otherwise '/'

    # ----------------------------------------
    # index
    # ----------------------------------------
    $stateProvider.state 'index',
        url: '/'
        resolve:
            posts: ['$app', ($app) ->
                $app.getPosts()
            ]
        views:
            content:
                templateUrl: '/views/content/posts.html'
                controller: 'PostsController'
]