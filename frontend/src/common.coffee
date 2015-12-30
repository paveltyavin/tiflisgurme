$ = require 'jquery'

module.exports = ->
  $('.navbar').affix
    offset:
      top: ->
        height = $('.container_welcome').outerHeight(true)
        return height

  container_padding = parseInt($('.content').css('padding-top').replace('px', ''))
  console.log 'container_padding', container_padding
  $('.content').css('padding-top', container_padding + 120);

  $('.ribbon').affix
    offset:
      top: ->
        height = $('.container_welcome').outerHeight(true)
        height -= 60
        return height

  $('.ribbon').on 'affix.bs.affix', =>
    $('.ribbon .social_list').hide()
  $('.ribbon').on 'affix-top.bs.affix', =>
    setTimeout ->
      if $('.ribbon').hasClass 'affix-top'
        $('.ribbon .social_list').fadeIn().css("display", "inline-block");
    , 300

  if $('.ribbon').hasClass 'affix'
    $('.ribbon .social_list').hide()
