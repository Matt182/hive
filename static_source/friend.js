// Bootstrap dependencies
window.$ = window.jQuery = require('jquery') // required for bootstrap
window.Popper = require('popper.js') // required for tooltip, popup...
require('bootstrap')

import './index.scss' // include bootstrap css file with own modifications
import { ajax_post } from './helpers'


$(function (){
    $(document).on("click", "#action-unfriend", () => {
        const params = new URLSearchParams()
        params.set('person_id', person_id)
        ajax_post('/user/delete_friend/', params, friend_action_cb)
    });

    $(document).on("click", "#action-decline-send", () => {
         const params = new URLSearchParams()
         params.set('person_id', person_id)
         ajax_post('/user/decline_send_friend_request/', params, friend_action_cb)
    });

    $(document).on("click", "#action-accept", () => {
         const params = new URLSearchParams()
         params.set('person_id', person_id)
         ajax_post('/user/accept_friend_request/', params, friend_action_cb)
    });

    $(document).on("click", "#action-decline-received", () => {
         const params = new URLSearchParams()
         params.set('person_id', person_id)
         ajax_post('/user/decline_received_friend_request/', params, friend_action_cb)
    });

    $(document).on("click", "#action-send", () => {
         const params = new URLSearchParams()
         params.set('person_id', person_id)
         ajax_post('/user/send_friend_request/', params, friend_action_cb)
    });
})

const friend_action_cb = (req) => {
    update_status_block(req.status)
}

const update_status_block = (status) => {
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
    .html(button);
}

console.log('Hello World')
