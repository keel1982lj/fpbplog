function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function checkSubmit(){ 
  $('.loading').attr('disabled','true');
  $('.submit').attr('disabled','true');
  $('.submit').append('<span class="spinner abs-center"></span>');
} 
$(document).ready(function(){
	$("a[rel*=leanModal]").leanModal({closeButton:".modal-close"});
	$(".tablesorter").tablesorter();
	$( ".the-date" ).datepicker();
	$('.loading').click(function(){
		$(this).addClass("no-show");
		$(this).parent().append('<span class="spinner abs-center"></span>');
	});
	$("[form]").submit(function( event ) {
	  	event.preventDefault();
	    var inputs = $(this).find( "input,select,textarea" );
	    var address = $(this).attr( "action" );
	    var data = {};
	    var okSubmit = true;
	    var button = $(this).find('button');
	    inputs.each(function(i){
	    	if($(this).val()){
	    		if($(this).attr('type')=='radio'||$(this).attr('type')=='checkbox'){
	    			if($(this)[0].checked == true){
	    				data[$(this).attr('name')] = $(this).val();
	    			}
	    		}else{
	    			data[$(this).attr('name')] = $(this).val();
	    		}
	    	}  
	    	if($(this).attr('data-invalid')==""){
	    		okSubmit = false;	
	    	}
	    });
	    if(okSubmit){
	    	button.prop('disabled', true);
		    button.addClass('c-trans');
			button.append('<span class="spinner abs-center"></span>')	 
		    $.ajax({
				type: "POST",
				url: address,
				data: data,
				success: function(result){
					button.removeClass('c-trans');
					button.find(".spinner").remove();
					result.button = button;
					button.prop('disabled', false);
					callbacks[result['callback']](result);
				}
			});
		}
	});
	$('[trigger]').click(function(){
		if($(this).attr('trigger')!='null'){
			var address = $(this).attr('trigger');
			$(this).attr('trigger','null');
			if($(this).is('[loading]')){
				$(this).prop('disabled', true);
				$(this).addClass('c-trans');
				$(this).append('<span class="spinner abs-center"></span>')
			}
			var data = {};
			var button = $(this);
			data['csrfmiddlewaretoken'] = csrftoken;
		  	$.each(this.attributes, function() {
			    if(this.name.indexOf('data-')==0) {
			      	if(this.value == "true"){
			    		data[this.name.substring(5)] = true;
			    	}else if(this.value == "false"){
			    		data[this.name.substring(5)] = false;
			    	}else{
			      		data[this.name.substring(5)] = this.value;
			      	}
			    }
			});
			$.ajax({
				type: "POST",
				url: address,
				data: data,
				success: function(result){
					if(button.is('[reset]')){
						button.attr('trigger','/int/ajax/');
					}
					button.removeClass('c-trans');
					button.find(".spinner").remove();
					result.button = button;
					callbacks[result['callback']](result);
				}
			});
		}
	});
});