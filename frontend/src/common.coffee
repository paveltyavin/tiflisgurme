$ = require 'jquery'
_ = require 'underscore'
backbone = require 'backbone'
marionette = require 'backbone.marionette'

class NavbarSmallView extends marionette.ItemView
  className: 'navbar_small navbar'
  template: require './templates/navbar_small'
  events:
    'click .expand': 'onClickExpand'
  onRender: =>
    @$el.affix
      offset:
        top: ->
          return $('.container_welcome').outerHeight(true)
  onClickExpand: (event) =>
    event.preventDefault()
    @$('.region_expand').collapse('toggle')
    @$('.expand').toggleClass 'glyphicon-menu-hamburger'
    @$('.expand').toggleClass 'glyphicon-remove'


class NavbarBigView extends marionette.ItemView
  className: 'navbar_big navbar'
  template: require './templates/navbar_big'
  routing:
    home: 'home'
    shipping: 'shipping'
    menu: 'menu'
    news: 'news'
    contact: 'contact'
    '': 'home'

  onRender: =>
    @$el.affix
      offset:
        top: ->
          return $('.container_welcome').outerHeight(true)

    for key in _.keys(@routing)
      do (key) =>
        r = new RegExp(key, 'i')
        if r.test(window.location.pathname)
          link = @routing[key]
          @$("[data-link=#{link}]").addClass 'active'


class CommonView extends marionette.LayoutView
  el: 'body'
  regions:
    region_navbar: '.region_navbar'

  onResize: =>
    width = $(window).width()
    mode = if width < 768 then 'small' else 'big'
    @model.set 'mode', mode

    footer_height = $('footer').height()
    $('body').css 'margin-bottom', footer_height + 150 + 'px'

  onChangeMode: (model, value) =>
    NavbarView = null
    if value is 'big'
      NavbarView = NavbarBigView
    if value is 'small'
      NavbarView = NavbarSmallView
    if NavbarView
      view = new NavbarView
      @region_navbar.show(view)
      $(window).trigger 'scroll'


  initialize: =>
    @listenTo @model, 'change:mode', @onChangeMode
    $(window).on 'resize', @onResize
    @onResize()

module.exports = ->
  new CommonView({model: new backbone.Model()})