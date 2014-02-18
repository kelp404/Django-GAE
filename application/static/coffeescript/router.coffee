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

    # ----------------------------------------
    # posts
    # ----------------------------------------
    $stateProvider.state 'posts',
        url: '/posts?index'
        resolve:
            posts: ['$app', '$stateParams', ($app, $stateParams) ->
                $app.store.getPosts($stateParams.index)
            ]
        views:
            content:
                templateUrl: '/views/content/posts.html'
                controller: 'PostsController'
]

.run ['$injector', ($injector) ->
    # providers
    $rootScope = $injector.get '$rootScope'

    # setup NProgress
    NProgress.configure
        showSpinner: no

    # ui.router state change event
    $rootScope.$on '$stateChangeStart', (event, toState, toParams, fromState) ->
        NProgress.start()

    $rootScope.$on '$stateChangeSuccess', ->
        NProgress.done()

    $rootScope.$on '$stateChangeError', ->
        NProgress.done()
]
