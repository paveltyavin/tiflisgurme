$ = require 'jquery'
_ = require 'underscore'
backbone = require 'backbone'
marionette = require 'backbone.marionette'
bus = require './bus'


class Cart extends backbone.Model
  url: '/api/cart/'


class CartView extends marionette.ItemView
  className: 'cart_view'
  template: require './templates/cart'
  events:
    'click .order': 'onClickOrder'
  onClickOrder: =>
    null
  onRender: =>
    cart_popover_template = require './templates/cart_popover'
    cart_popover_html= cart_popover_template()
    @$('.container_order').popover
      placement: 'top'
      html: true
      template: cart_popover_html
      content: 'К сожалению, онлайн доставка временно не доступна. Вы можете оформить заказ по телефону!'

navbarSerializeData = ->
  lang = $('html').attr('lang')
  result = {
    lang: lang
  }
  if lang is 'ru'
    result = _.defaults result,
      lang_text: "РУС"
      other_lang: 'en'
      other_lang_text: 'EN'
      menu: 'Меню'
      shipping: 'Доставка'
      news: 'Новости'
      contact: 'Контакты'
      vacancy: 'Вакансии'
  if lang is 'en'
    result = _.defaults result,
      lang_text: "EN"
      other_lang: 'ru'
      other_lang_text: 'РУС'
      menu: 'Menu'
      shipping: 'Shipping'
      news: 'News'
      contact: 'Contact'
      vacancy: 'Vacancies'
      other_lang: 'ru'
  return result


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

    lang = $('html').attr('lang')
  onClickExpand: (event) =>
    event.preventDefault()
    @$('.region_expand').collapse('toggle')
    @$('.expand').toggleClass 'glyphicon-menu-hamburger'
    @$('.expand').toggleClass 'glyphicon-remove'

  serializeData: navbarSerializeData


class RibbonView extends marionette.ItemView
  className: 'ribbon'
  template: require './templates/ribbon'
  onRender: =>
    lang = $('html').attr('lang')
    @$("[data-lang=#{lang}]").addClass('active').find('a').removeAttr('href')

  serializeData: =>
    path = window.location.pathname
    lang = $('html').attr('lang')
    path = path.replace("/#{lang}/", '')
    return {path: path}


class NavbarBigView extends marionette.LayoutView
  className: 'navbar_big navbar'
  template: require './templates/navbar_big'
  routing:
    home: 'home'
    shipping: 'shipping'
    menu: 'menu'
    news: 'news'
    contact: 'contact'
    '': 'home'
  serializeData: navbarSerializeData
  regions:
    region_ribbon: '.region_ribbon'

  onRender: =>
    @$el.affix
      offset:
        top: ->
          return $('.container_welcome').outerHeight(true)

    pathname = window.location.pathname
    for key in _.keys(@routing)
      do (key) =>
        r = new RegExp(key, 'i')
        if r.test pathname
          link = @routing[key]
          @$("[data-link=#{link}]").addClass 'active'

    if not _.contains(['', '/ru/home/', '/en/home/'], pathname) and $(window).width() > 1100
      @region_ribbon.show(new RibbonView)


class CommonView extends marionette.LayoutView
  el: 'body'
  regions:
    region_navbar: '.region_navbar'
    region_cart: '.region_cart'

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

    cart = new Cart
    @listenTo cart, 'sync', =>
      total_quantity =  cart.get 'total_quantity'
      if total_quantity
        cart_view = new CartView({model: cart})
        @region_cart.show(cart_view)
      else
        @region_cart.empty()
    cart.fetch()

    @listenTo bus.vent, 'product:add product:remove', =>
      cart.fetch()

module.exports = ->
  new CommonView({model: new backbone.Model()})