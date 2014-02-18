(function() {
  angular.module('app.controller', []).controller('NavigationController', [
    '$scope', '$injector', function($scope, $injector) {
      var $app, $state;
      $app = $injector.get('$app');
      $state = $injector.get('$state');
      $scope.user = $app.user;
      return $scope.showCreatePostModal = function($event) {
        $event.preventDefault();
        return $app.modal.post.showCreate({
          submitCallback: function(model) {
            return $app.store.addPost(model.title, model.content).success(function() {
              $state.go($state.$current, null, {
                reload: true
              });
              return $app.modal.post.hideCreate();
            });
          }
        });
      };
    }
  ]).controller('PostsController', [
    '$scope', 'posts', function($scope, posts) {
      return $scope.posts = posts;
    }
  ]);

}).call(this);

(function() {
  angular.module('app.directive', ['app.controller']).directive('appNavigation', function() {
    return {
      controller: 'NavigationController'
    };
  }).directive('appModalPost', [
    '$injector', function($injector) {
      return {
        scope: true,
        link: function(scope, element) {
          var $app;
          $app = $injector.get('$app');
          scope.$on($app.broadcastChannel.showCreatePost, function(self, object) {
            scope.title = object.title;
            scope.content = object.content;
            scope.submit = function($event) {
              $event.preventDefault();
              return object != null ? object.submitCallback({
                title: scope.title,
                content: scope.content
              }) : void 0;
            };
            return $(element).modal('show');
          });
          scope.$on($app.broadcastChannel.hideCreatePost, function() {
            return $(element).modal('hide');
          });
          return $(element).on('shown.bs.modal', function() {
            return $(element).find('input:first').select();
          });
        }
      };
    }
  ]).directive('appPager', function() {
    return {
      scope: {
        pageList: '=appPager',
        urlTemplate: '@pagerUrlTemplate'
      },
      template: "<ul ng-if=\"pageList.total > 0\" class=\"pagination\">\n    <li ng-class=\"{disabled: !links.previous.enable}\">\n        <a ng-href=\"{{ links.previous.url }}\">&laquo;</a>\n    </li>\n\n    <li ng-repeat='item in links.numbers'\n        ng-if='item.show'\n        ng-class='{active: item.isCurrent}'>\n        <a ng-href=\"{{ item.url }}\">{{ item.pageNumber }}</a>\n    </li>\n\n    <li ng-class=\"{disabled: !links.next.enable}\">\n        <a ng-href=\"{{ links.next.url }}\">&raquo;</a>\n    </li>\n</ul>",
      link: function(scope) {
        var index, _i, _ref, _ref1, _results;
        scope.links = {
          previous: {
            enable: scope.pageList.has_previous_page,
            url: scope.urlTemplate.replace('#{index}', scope.pageList.index - 1)
          },
          numbers: [],
          next: {
            enable: scope.pageList.has_next_page,
            url: scope.urlTemplate.replace('#{index}', scope.pageList.index + 1)
          }
        };
        _results = [];
        for (index = _i = _ref = scope.pageList.index - 3, _ref1 = scope.pageList.index + 3; _i <= _ref1; index = _i += 1) {
          _results.push(scope.links.numbers.push({
            show: index >= 0 && index <= scope.pageList.max_index,
            isCurrent: index === scope.pageList.index,
            pageNumber: index + 1,
            url: scope.urlTemplate.replace('#{index}', index)
          }));
        }
        return _results;
      }
    };
  });

}).call(this);

(function() {
  angular.module('app', ['app.router', 'app.directive']);

}).call(this);

(function() {
  angular.module('app.provider', []).provider('$app', function() {
    var $http, $injector, $rootScope;
    $injector = null;
    $http = null;
    $rootScope = null;
    this.setupProviders = function(injector) {

      /*
      Setup providers.
      @param injector: The $injector.
       */
      $injector = injector;
      $http = $injector.get('$http');
      return $rootScope = $injector.get('$rootScope');
    };
    this.broadcastChannel = {
      showCreatePost: '$showCreatePost',
      hideCreatePost: '$hideCreatePost'
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
    this.modal = {
      post: {

        /*
        Modals about post functions.
         */
        showCreate: (function(_this) {
          return function(object) {
            if (object == null) {
              object = {};
            }

            /*
            @params object:
                title: ''
                content: ''
                submitCallback: ({title: '', content: ''})->
             */
            return $rootScope.$broadcast(_this.broadcastChannel.showCreatePost, object);
          };
        })(this),
        hideCreate: (function(_this) {
          return function() {
            return $rootScope.$broadcast(_this.broadcastChannel.hideCreatePost);
          };
        })(this)
      }
    };
    this.http = (function(_this) {
      return function(model) {
        return $http(model).error(function(data, status) {
          return _this.popMessage.error(status);
        });
      };
    })(this);
    this.store = {

      /*
      The data sotre provider.
       */
      getPosts: (function(_this) {
        return function(index) {
          if (index == null) {
            index = 0;
          }
          return _this.http({
            method: 'get',
            url: '/posts',
            params: {
              index: index
            }
          }).then(function(data) {
            return data.data;
          });
        };
      })(this),
      addPost: (function(_this) {
        return function(title, content) {
          return _this.http({
            method: 'post',
            url: '/posts',
            data: {
              title: title,
              content: content
            }
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
            broadcastChannel: _this.broadcastChannel,
            user: _this.user,
            modal: _this.modal,
            http: _this.http,
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
      $stateProvider.state('index', {
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
      return $stateProvider.state('posts', {
        url: '/posts?index',
        resolve: {
          posts: [
            '$app', '$stateParams', function($app, $stateParams) {
              return $app.store.getPosts($stateParams.index);
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
  ]).run([
    '$injector', function($injector) {
      var $rootScope;
      $rootScope = $injector.get('$rootScope');
      NProgress.configure({
        showSpinner: false
      });
      $rootScope.$on('$stateChangeStart', function(event, toState, toParams, fromState) {
        return NProgress.start();
      });
      $rootScope.$on('$stateChangeSuccess', function() {
        return NProgress.done();
      });
      return $rootScope.$on('$stateChangeError', function() {
        return NProgress.done();
      });
    }
  ]);

}).call(this);
