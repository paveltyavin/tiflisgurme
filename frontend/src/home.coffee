require './mousewheel'


class HomeView
  getOut: false
  resizeSlider: (height) =>
    $('.slider').height(height)
    $('.slider.item').height(height)
    $('.slider').find('img').css 'height', height
  mousewheel: (event) =>
    n = $('.navbar').innerHeight()
    w = $(window).width()
    i = 35
    sl = $('.container_slider').scrollLeft()
    st = $('.container_slider').offset().top
    sw = $('.slider').width()
    d = (event.deltaY * event.deltaFactor)
    wy = window.pageYOffset
    k = wy - st + n

    if Math.abs(k) < i
      if sl is 0 and d > 0
        window.getOut = false
        return true
      if sl + w is sw and d < 0
        window.scrollTo 0, wy + 1
        @getOut = true
        return true
      if @getOut
        if d < 0
          return true
        @getOut = false
      window.scrollTo 0, st - n
      $(".container_slider").scrollLeft(sl - d)
      return false

  init: =>
    $(window).mousewheel @mousewheel
    n = $('.navbar').innerHeight()
    height = $(window).height()
    @resizeSlider(height - n)
    $('.container_welcome').css 'height', height

    $('.arrow_bottom').on 'click', (event)=>
      event.preventDefault()
      target = $('.navbar')
      $('html, body').animate
        scrollTop: target.offset().top
      , 1000


home = new HomeView

module.exports = home.init