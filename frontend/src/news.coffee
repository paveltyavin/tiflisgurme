$ = require 'jquery'
_ = require 'underscore'
backbone = require 'backbone'
marionette = require 'backbone.marionette'

class NewsItemView extends marionette.ItemView
  events:
    'click': 'onClick'
  onClick: (event) =>
    event.preventDefault()
    @trigger 'click', @


class MiddleView extends marionette.ItemView
  className: 'middle_view'
  template: require './templates/news_middle'
  events:
    'click .close>img': 'onClickClose'
  onClickClose: (event)=>
    @$el.slideUp
      success: =>
        console.log 'slideUp success'


class LayoutView extends marionette.LayoutView
  el: 'body'
  initialize: =>
    $('.container_newsitem').each (counter, el) =>
      view = new NewsItemView({el: el})
      @listenTo view, 'click', (view) =>
        @$('.middle_view').slideUp()
        model = new backbone.Model
          title: view.$el.data 'title'
          date: view.$el.data 'date'
          thumbnail: view.$el.data 'thumbnail'
          text: view.$el.data 'text'
        middle_view = new MiddleView({model: model})
        middle_view.render()
        middle_view.$el.hide()

        $afterEl = $('.container_newsitem').eq(counter - counter % 3 + 2)
        width = $(window).width()
        if $afterEl.length > 0 and width >= 992
          $afterEl.after(middle_view.$el)
        else
          view.$el.after(middle_view.$el)
        middle_view.$el.slideDown()


module.exports = ->
  new LayoutView