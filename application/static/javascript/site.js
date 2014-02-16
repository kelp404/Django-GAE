(function() {
  angular.module('app.controller', []).controller('NavigationController', [
    '$scope', '$injector', function($scope, $injector) {
      var $app;
      $app = $injector.get('$app');
      return $scope.user = $app.user;
    }
  ]).controller('PostsController', ['$scope', 'posts', function($scope, posts) {}]);

}).call(this);

(function() {
  angular.module('app.directive', ['app.controller']).directive('appNavigation', function() {
    return {
      controller: 'NavigationController'
    };
  });

}).call(this);

(function() {
  angular.module('app', ['app.router', 'app.directive']);

}).call(this);

(function() {
  angular.module('app.provider', []).provider('$app', function() {
    var $http, $injector;
    $injector = null;
    $http = null;
    this.setupProviders = function(injector) {

      /*
      Setup providers.
      @param injector: The $injector.
       */
      $injector = injector;
      return $http = $injector.get('$http');
    };

    /*
    is_login: yes / no
    id: 0
    permission: 0: anonymous, 1: root, 2: normal
    name: 'Guest'
    email: 'user@email.com'
    login_url: 'url'
    logout_url: 'url'
     */
    this.user = window.user;
    this.store = {

      /*
      The data sotre provider.
       */
      getPosts: (function(_this) {
        return function(index, size) {
          if (index == null) {
            index = 0;
          }
          if (size == null) {
            size = 20;
          }
          return $http({
            method: 'get',
            url: '/'
          });
        };
      })(this)
    };
    this.popMessage = {
      error: function(status) {

        /*
        pop error message.
         */
        switch (status) {
          case 400:
            return $.av.pop({
              title: 'Input Failed',
              message: 'Please check input values.',
              template: 'error'
            });
          case 403:
            return $.av.pop({
              title: 'Permission denied',
              message: 'Please check your permission.',
              template: 'error'
            });
          default:
            return $.av.pop({
              title: 'Error',
              message: 'Loading failed, please try again later.',
              template: 'error'
            });
        }
      }
    };
    this.$get = [
      '$injector', (function(_this) {
        return function($injector) {
          _this.setupProviders($injector);
          return {
            user: _this.user,
            store: _this.store,
            popMessage: _this.popMessage
          };
        };
      })(this)
    ];
  });

}).call(this);

(function() {
  angular.module('app.router', ['app.provider', 'app.controller', 'ui.router']).config([
    '$stateProvider', '$urlRouterProvider', '$locationProvider', function($stateProvider, $urlRouterProvider, $locationProvider) {
      $locationProvider.html5Mode(true);
      $urlRouterProvider.otherwise('/');
      return $stateProvider.state('index', {
        url: '/',
        resolve: {
          posts: [
            '$app', function($app) {
              return $app.store.getPosts();
            }
          ]
        },
        views: {
          content: {
            templateUrl: '/views/content/posts.html',
            controller: 'PostsController'
          }
        }
      });
    }
  ]);

}).call(this);
