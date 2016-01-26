$ = require 'jquery'
_ = require 'underscore'
backbone = require 'backbone'
marionette = require 'backbone.marionette'
bus = require './bus'


class ProductItemView extends marionette.ItemView
  events:
    'click .container_image': 'onClickImg'
    'click .container_empty_image': 'onClickImg'
    'click .remove': 'onClickRemove'
    'click .add': 'onClickAdd'
  onClickImg: =>
    id = @$el.data 'id'
    thumb = @$el.data 'thumb'
    if thumb is 'None'
      thumb = null
    @trigger 'modal',
      id: @$el.data 'id'
      name: @$el.data 'name'
      desc: @$el.data 'desc'
      price: @$el.data 'price'
      portion: @$el.data 'portion'
      thumb: thumb
      quantity: @$('.quantity').text()
  onClickAdd: =>
    id = @$el.data 'id'
    $.ajax
      url: '/api/cart/'
      method: 'post'
      dataType: 'json'
      contentType: 'application/json'
      data: JSON.stringify
        product: id
      success: (data)=>
        bus.vent.trigger 'product:add',
          product: id
          quantity: data.quantity || 0
  onClickRemove: =>
    id = @$el.data 'id'
    $.ajax
      url: '/api/cart/'
      method: 'delete'
      dataType: 'json'
      contentType: 'application/json'
      data: JSON.stringify
        product: id
      success: (data) =>
        bus.vent.trigger 'product:remove',
          product: id
          quantity: data.quantity || 0

  initialize: =>
    id = @$el.data 'id'
    @listenTo bus.vent, 'product:remove product:add', (data) =>
      if id is data.product
        @$('.quantity').text(data.quantity)



class ProductModalView extends ProductItemView
  className: 'modal-dialog'
  template: require './templates/product_modal'
  events:
    'click .remove': 'onClickRemove'
    'click .add': 'onClickAdd'
  serializeData: =>
    res = super
    lang = $('html').attr 'lang'
    currency = ''
    if lang is 'ru'
      currency = 'руб'
    if lang is 'en'
      currency = 'rub'
    res.currency = currency
    return res
  initialize: =>
    @listenTo bus.vent, 'product:remove product:add', (data) =>
      if @model.id is data.product
        @$('.quantity').text(data.quantity)
    @$el.data 'id', @model.id



class MenuView extends marionette.LayoutView
  el: 'body'
  regions:
    region_modal: '.region_modal'

  initialize: =>
    $('.layout_table .product_list .product_item').each (index, el) =>
      view = new ProductItemView({el: el})
      @listenTo view, 'modal', (data) =>
        product = new backbone.Model(data)
        view = new ProductModalView(model: product)
        @region_modal.show(view)
        $('.region_modal').modal()


module.exports = ->
  new MenuView