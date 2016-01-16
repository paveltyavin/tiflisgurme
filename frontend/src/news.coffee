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
  className: 'newsitem_detail'
  template: require './templates/news_middle'


class LayoutView extends marionette.LayoutView
  el: 'body'
  initialize: =>
    view_list = []
    middle_region_array = []

    $('.region_middle').each (index, el) =>
      region = new marionette.Region({el: el})
      counter = parseInt($(el).data 'counter')
      middle_region_array.push([counter, region])

    $('.container_newsitem').each (index, el) =>
      view = new NewsItemView({el: el})
      view_list.push view
      @listenTo view, 'click', (view) =>
        view_counter = parseInt(view.$el.data 'counter')
        rendered = false
        for ar in middle_region_array
          middle_region_counter = ar[0]
          middle_region = ar[1]
          middle_region.empty()
          if !rendered and middle_region_counter >= view_counter
            rendered = true
            model = new backbone.Model
              title: view.$el.data 'title'
              date: view.$el.data 'date'
              thumbnail: view.$el.data 'thumbnail'
              text: view.$el.data 'text'
            middle_view = new MiddleView({model: model})
            middle_view.render()
            middle_view.$el.hide()
            middle_region.show(middle_view)
            middle_view.$el.fadeIn()


module.exports = ->
  new LayoutView