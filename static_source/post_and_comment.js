import { ajax_post } from './helpers';
window.$ = window.jQuery = require('jquery')

$('#post_submit_form').on('submit', (e) => {
    e.preventDefault();
    const form = e.currentTarget;
    console.log($(form));
    const url = $(form).attr("action");
    const form_data = new FormData(form);
    ajax_post(url, form_data, (req) => {
        append_post(req.post);
    }, false);
});

$('.comment_submit_form').on('submit', (e) => {
    e.preventDefault();
    const form = e.currentTarget;
    const url = $(form).attr("action");
    const form_data = new FormData(form);
    ajax_post(url, form_data, (req) => {
        append_comment(req.comment, req.post_id);
    }, false);
});

const append_post = (post_data) => {
    const posts = $('#post_block').html();
    $('#post_block').empty()
        .append(post_data)
        .append(posts);
}

const append_comment = (comment_data, post_id) => {
    console.log(`#post_comments_${post_id}`)
    $(`#post_comments_${post_id}`)
        .append(comment_data);
}