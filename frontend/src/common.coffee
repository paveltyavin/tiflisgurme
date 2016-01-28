$ = require 'jquery'
_ = require 'underscore'
backbone = require 'backbone'
marionette = require 'backbone.marionette'
bus = require './bus'


class Cart extends backbone.Model
  url: '/api/cart/'

declOfNum = (number, titles...) ->
# канал, канала, каналов
  cases = [2, 0, 1, 1, 1, 2]
  result = titles[if number % 100 > 4 and number % 100 < 20 then 2 else cases[if number % 10 < 5 then number % 10 else 5]]
  return result

class CartView extends marionette.ItemView
  className: 'cart_view'
  template: require './templates/cart'
  events:
    'click .order': 'onClickOrder'
    'click .close': 'onClickClose'
  onClickOrder: =>
    null
  onClickClose: =>
    $.ajax
      url: '/api/cart/'
      method: 'delete'
      dataType: 'json'
      contentType: 'application/json'
      data: JSON.stringify
        all: true
      success: (data)=>
        bus.vent.trigger 'cart:delete'
  serializeData: =>
    result = super
    lang = $('html').attr 'lang'
    if lang is 'en'
      result = _.defaults result,
        currency_text: "rub"
        order_text: "order"
        choose_text: "you choose"
        with_text: "price:"
      result['quantity_text'] = declOfNum(result.total_quantity, 'dish', 'dishes', 'dishes')
    if lang is 'ru'
      result = _.defaults result,
        currency_text: "руб"
        order_text: "Хочу заказать"
        choose_text: "вы выбрали"
        with_text: "на"
      result['quantity_text'] = declOfNum(result.total_quantity, 'блюдо', 'блюда', 'блюд')

    result
  onRender: =>
    cart_popover_template = require './templates/cart_popover'
    cart_popover_html = cart_popover_template()
    lang = $('html').attr 'lang'
    if lang is 'en'
      content_text = 'Unfortunately, the online service is temporarily unavailable. You can place your order over the phone!'
    if lang is 'ru'
      content_text = 'К сожалению, онлайн доставка временно не доступна. Вы можете оформить заказ по телефону!'
    @$('.container_order').popover
      placement: 'top'
      html: true
      template: cart_popover_html
      content: content_text
    @footer_height = $('footer').outerHeight(true) + 1

  onShow: =>
    @$el.affix
      offset:
        bottom: @footer_height

    @$('.container_order').popover('show')

navbarSerializeData = ->
  lang = $('html').attr('lang')
  path = window.location.pathname
  path = path.replace("/#{lang}/", '')
  result = {
    lang: lang
    path: path
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
    width = $(window).width()
    if width < 768
      @$el.addClass 'affix'
    else
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

    if not _.contains(['', '/ru/home/', '/en/home/'], pathname)
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
      total_quantity = cart.get 'total_quantity'
      if total_quantity
        cart_view = new CartView({model: cart})
        @region_cart.show(cart_view)
        @listenTo bus.vent, 'cart:delete', =>
          @region_cart.empty()
      else
        @region_cart.empty()
    cart.fetch()

    @listenTo bus.vent, 'product:add product:remove', =>
      cart.fetch()

module.exports = ->
  new CommonView({model: new backbone.Model()})