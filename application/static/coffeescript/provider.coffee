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
    @store =
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
        store: @store
        popMessage: @popMessage
    ]

    return