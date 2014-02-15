angular.module 'app.router', ['app.provider', 'app.controller', 'ui.router']

.config ['$stateProvider', '$urlRouterProvider', '$locationProvider',
($stateProvider, $urlRouterProvider, $locationProvider) ->

    # html5 mode
    $locationProvider.html5Mode yes

    # redirect other urls
    $urlRouterProvider.otherwise '/'

    # ----------------------------------------
    # index
    # ----------------------------------------
    $stateProvider.state 'index',
        url: '/'
        resolve:
            posts: ['$app', ($app) ->
                $app.store.getPosts()
            ]
        views:
            content:
                templateUrl: '/views/content/posts.html'
                controller: 'PostsController'
]