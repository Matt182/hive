// Bootstrap dependencies
window.$ = window.jQuery = require('jquery') // required for bootstrap
window.Popper = require('popper.js') // required for tooltip, popup...
require('bootstrap')

import './index.scss' // include bootstrap css file with own modifications
//import { setup_ajax_csrf } from './helpers'
import Cookies from 'js-cookie'


const setup_ajax_csrf = () => {
  const csrftoken = Cookies.get('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
}

// tooltip and popover require javascript side modification to enable them (new in Bootstrap 4)
// use tooltip and popover components everywhere
$(function (){
   $('[data-toggle="tooltip"]').tooltip()
   $('[data-toggle="popover"]').popover()

   setup_ajax_csrf()

   $('#action-unfriend').click(function () {
       $.post('/user/delete_friend/', {
           person_id: person_id,
       }, function(data) {
           update_status_block(data.status)
       })
   })

   $('#action-decline-send').click(function () {
       $.post('/user/decline_send_friend_request/', {
           person_id: person_id,
       }, function(data) {
           update_status_block(data.status)
       })
   })

   $('#action-accept').click(function () {
       $.post('/user/accept_friend_request/', {
           person_id: person_id,
       }, function(data) {
           update_status_block(data.status)
       })
   })

   $('#action-decline-received').click(function () {
       $.post('/user/decline_received_friend_request/', {
           person_id: person_id,
       }, function(data) {
           update_status_block(data.status)
       })
   })

   $('#action-send').click(function () {
       const params = new URLSearchParams()
       params.set('person_id', person_id)
       fetch('/user/send_friend_request/', {
           method: 'post',
           credentials: "same-origin",
           headers: {
               "X-CSRFToken": Cookies.get('csrftoken'),
               'X-Requested-With': 'XMLHttpRequest',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Accept': 'application/json, application/xml, text/plain, text/html, *.*',
           },
           body: params
       }).then((resp) => {
           return resp.json()
       }).then((resp) => {
           if (resp.result == 'success') {
               update_status_block(resp.status)
           }
           console.log("Error", resp);
       }).catch(function(ex) {
           console.log("parsing failed", ex);
       });
//       $.post('/user/send_friend_request/', {
//           person_id: person_id,
//       }, function(data) {
//           update_status_block(data.status)
//       })
   })
})

function update_status_block(status) {
   let button = ''

   switch (status) {
       case STATUS_FRIEND:
           button = '<div>Send <button id="action-unfriend">Unfriend<button/><div/>'
           break;
       case STATUS_REQUEST_SEND:
           button = '<div>Send <button id="action-decline-send">Decline<button/><div/>'
           break;
       case STATUS_REQUEST_RECEIVED:
           button = '<div>Received <button id="action-accept">Accept<button/> <button id="action-decline-received">Decline<button/><div/>'
           break;
       case STATUS_UNRELATED:
           button = '<div><button id="action-send">Send request<button/><div/>'
           break;
   }
   $('#status-block')
       .empty()
       .html(button)
}

console.log('Hello World')
