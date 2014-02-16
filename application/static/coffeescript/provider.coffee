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
    ###
    is_login: yes / no
    id: 0
    permission: 0: anonymous, 1: root, 2: normal
    name: 'Guest'
    email: 'user@email.com'
    login_url: 'url'
    logout_url: 'url'
    ###
    @user = window.user

    @store =
        ###
        The data sotre provider.
        ###
        getPosts: (index=0, size=20) =>
            $http
                method: 'get'
                url: '/'

    @popMessage =
        error: (status) ->
            ###
            pop error message.
            ###
            switch status
                when 400
                    $.av.pop
                        title: 'Input Failed'
                        message: 'Please check input values.'
                        template: 'error'
                when 403
                    $.av.pop
                        title: 'Permission denied'
                        message: 'Please check your permission.'
                        template: 'error'
                else
                    $.av.pop
                        title: 'Error'
                        message: 'Loading failed, please try again later.'
                        template: 'error'


    # -------------------------------------------------------------
    # $get
    # -------------------------------------------------------------
    @$get = ['$injector', ($injector) =>
        # setup providers
        @setupProviders $injector

        # result object
        user: @user
        store: @store
        popMessage: @popMessage
    ]

    return