$ = require 'jquery'
_ = require 'underscore'
backbone = require 'backbone'
marionette = require 'backbone.marionette'


class ProductModalView extends marionette.ItemView
  template: require './templates/product_modal'


class ProductItemView extends marionette.ItemView
  events:
    'click': 'onClick'
  onClick: =>
    id = @$el.data 'id'
    $.ajax
      url: "/api/product/#{id}/"
      success: (data) =>
        @trigger 'modal', data
  initialize: =>
    console.log 'init'


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