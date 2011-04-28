

function validate(email) {
    var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    if (reg.test(email) == false) {
	return false;
    }
    return true;
}

function set_auto_text(el, str_cmt)
{
    el.val(str_cmt);
    el.focus(function(){
	if(this.value == str_cmt) {
	    this.value = '';
	}
    });
    el.blur(function(){
	if (this.value == '') {
	    this.value = str_cmt;
	}
    });
}


function log_me_in(user_infos){
    $('#log_me_in').click(function(){

	var el = $(this).parent().parent();

	/*el.find('#log_me_in').remove();
	el.find('#send_cmt').remove();*/
	el.find('#user_infos').html('');


	var log_in = '';
	log_in += '<div id="loggin_form">';
	log_in += '<input type="text" id="loggin_username"><br/>';
	log_in += '<input type="password" id="loggin_password"><br/>';
	log_in += '<input type="button" id="send_with_pass" value="Send">';
	log_in += '</div>';

	el.find('#user_infos').append(log_in);

	el.parent().find('.post-area').val('').unbind();

	set_auto_text(el.find('#loggin_username'), 'Username');
	set_auto_text(el.find('#loggin_password'), 'Password');
	
    });
}

function append_to_comment(el, user_infos){
    $('#user_infos').remove();
    
    var app = '<span id="user_infos">';

    if (user_infos.logged == 'false'){
	app += '<input id="user_name_cmt" type="text"><br/>';
	app += '<input id="mail_user_cmt" type="text"><br/>';

	//app += '<input id="log_me_in" type="button" value="Log me"></input>';
    }
    else {
	app += '<input id="user_name_cmt" type="hidden" value="'  + user_infos.name + '"><br/>';
	app += '<input id="mail_user_cmt" type="hidden" value="">';
    }

    app += '<input id="send_cmt" type="button" value="' + i18.send + '"></input>';    
    if (user_infos.logged == 'true')
	app += '&nbsp;&nbsp;logged as <strong>' + user_infos.name + '</strong><br/>';
    app += '</span>';
    
    el.append(app);

    
    if (user_infos.logged == 'false'){
	
	//log_me_in(user_infos);

	// Set text in inputs
	var str_user_name = i18.username;
	var str_mail = 'Mail';
	
	set_auto_text(el.find('#user_name_cmt'), str_user_name);
	set_auto_text(el.find('#mail_user_cmt'), str_mail);
    }


    // Button handling
    el.find('#send_cmt').click(function(){
	// Simple anti con verification
	var user_name_cmt = el.find('#user_name_cmt').val()
	var mail_user_cmt = el.find('#mail_user_cmt').val();
	var post_area = el.find('.post-area').val();

	if (user_name_cmt != str_user_name &&
	    mail_user_cmt != str_mail &&
	    validate(mail_user_cmt) &&
	    post_area != i18.addComment){
	    
	    $.ajax({
		type : "POST",
		url : app_name + '/comments/new_comment',
		data : {
		    "id" : el.attr('alt'),
		    "cmt" : post_area,
		    "username" : user_name_cmt,
		    "mail" : mail_user_cmt
		},
		success: function(){
		    el.parent().find("#hidden-comments").slideDown();
		    el.parent().find('.show-more-comments').remove();
		    var ok_append;
		    ok_append = '<li>';
		    ok_append += '<div id="comment-header">';
		    ok_append += '<span id="user_name">' + user_name_cmt + '</span>';
		    ok_append += '<span id="comment_date">' + i18.commentPosted + '</span>';
		    ok_append += '</div>';
		    ok_append += '<span id="comment-content">' + post_area + '</span>';
		    ok_append += '</li>';
		    el.parent().find('#hidden-comments').append(ok_append);
		    el.find('.post-area').val(i18.addComment);
		    $('#user_infos').remove();
		}
	    });
	}
	else{
	    if (user_name_cmt == str_user_name ||
		mail_user_cmt == str_mail ||
		post_area == i18.addComment){
		notify(i18.fieldEmpty);
	    }
	    else
		notify(i18.wrongMailFormat);	
	}
    });
}

function show_comments(){
}

function show_more_comments(){
    $(".show-more-comments").each(function(e){
	var thise = $(this);
	$(this).click(function(){
	    var find = $(this).parent().find('#hidden-comments');
	    find.slideDown();
	    //find.append('<li>Hide</li>');
	    $(this).remove();
	});
    });
}

/*
 * Main entry
 */
function comment_text_gest(user_infos){

    $('#back-to-top').click(function(){
	
  $('html,body').animate({scrollTop: 0}, 600);
  });

    show_more_comments();
    $(".post-area").each(function(e){
	var str_cmt = i18.addComment;
	var search = $(this);
	search.val(str_cmt);
	search.focus(function(){
	    if(this.value == str_cmt) {
		this.value = '';
	    }
	    append_to_comment(search.parent(), user_infos);
	});
	search.blur(function(){
	    if (this.value == '') {
		this.value = str_cmt;
	    }	
	});	
    });
}


