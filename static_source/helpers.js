import Cookies from 'js-cookie'

const ajax_post = (url, data, cb, ct=true) => {
    let headers = {
         "X-CSRFToken": Cookies.get('csrftoken'),
         'X-Requested-With': 'XMLHttpRequest',
         'Accept': 'application/json, application/xml, text/plain, text/html, *.*',
    }
    if (ct) {
        headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8';
    }
    fetch(url, {
         method: 'post',
         credentials: "same-origin",
         headers: headers,
        body: data
    }).then((resp) => {
         return resp.json()
    }).then((resp) => {
         if (resp.result == 'success') {
              return cb(resp)
         }
         console.error("Error", resp);
    }).catch(function(ex) {
         console.error(`fetch #{url} failed`, ex);
    });
}

export { ajax_post }