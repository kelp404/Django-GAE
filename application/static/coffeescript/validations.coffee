angular.module 'app.validations', ['validator']

.config ['$validatorProvider', ($validatorProvider) ->
    $validatorProvider.register 'required',
        validator: /.+/
        error: 'This field is required.'
]
