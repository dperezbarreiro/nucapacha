$(function () {
  var popupModal = $('#popupModal')

  if (popupModal.length) {
    var now = new Date()
    var popupId = popupModal.data('id')
    var displayOptions = popupModal.data('display-options')
    var cookieName = 'popup_' + popupId
    var lastDisplay = Cookies.get(cookieName)
    var shouldOpen = true

    if (displayOptions === 'daily' && lastDisplay) {
      try {
        var lastDisplayDate = new Date(lastDisplay)

        if (now.getFullYear() === lastDisplayDate.getFullYear()
          && now.getMonth() === lastDisplayDate.getMonth()
          && now.getDate() === lastDisplayDate.getDate()) {
          shouldOpen = false
        }
      } catch (e) {
        console.error(e)
      }
    } else if (displayOptions === 'once') {
      shouldOpen = !lastDisplay
    }

    if (shouldOpen) {
      popupModal.modal()
      Cookies.set(cookieName, now.toISOString())
    }
  }
})