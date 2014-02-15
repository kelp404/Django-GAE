angular.module 'app.provider', []

.provider '$app', ->
    # -------------------------------------------------------------
    # providers
    # -------------------------------------------------------------
    $injector = null
    $http = null


    # -------------------------------------------------------------
    # private methods
    # -------------------------------------------------------------
    @setupProviders = (injector) ->
        ###
        Setup providers.
        @param injector: The $injector.
        ###
        $injector = injector
        $http = $injector.get '$http'


    # -------------------------------------------------------------
    # public methods
    # -------------------------------------------------------------
    @getPosts = (index=0, size=20) =>
        $http
            method: 'get'
            url: '/'


    # -------------------------------------------------------------
    # $get
    # -------------------------------------------------------------
    @$get = ['$injector', ($injector) =>
        # setup providers
        @setupProviders $injector

        # result object
        getPosts: @getPosts
    ]

    return