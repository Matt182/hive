//const setup_ajax_csrf = () => {
//  const csrftoken = Cookies.get('csrftoken');
//
//  function csrfSafeMethod(method) {
//    // these HTTP methods do not require CSRF protection
//    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//  }
//  $.ajaxSetup({
//      beforeSend: function(xhr, settings) {
//          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//              xhr.setRequestHeader("X-CSRFToken", csrftoken);
//          }
//      }
//  });
//}
//
//export {setup_ajax_csrf}