var callbacks = {
	swal: function(result){
		swal(result);
		result.button.removeClass('c-trans');
		result.button.find(".spinner").remove();
	},
	findPlate: function(result){
		$('#carPlate').attr('value',result['plate']);
	},
	smsSent: function(result){
		modal = $('#sms-modal');
		modal.find('.glyphicon-ok').fadeIn();
		result.button.hide();
	},
	msgSent: function(result){
		result.button.html('发送成功');
		result.button.removeClass('btn-primary');
		result.button.addClass('btn-success');
		result.button.addClass('disabled');
	},
	outingDecide: function(result){
		result.button.html(result['decision']);
		result.button.addClass('disabled');
		result.button.parent().find(".decide-btn").addClass('no-show');
		result.button.removeClass('no-show');
	},
	showpic: function(result){
		modal = $('#cj'+result['data'][0]);
		if(result['data'][1]) modal.find('#gk').attr('src',"data:image/jpeg;base64,"+result['data'][1]);
		if(result['data'][2])modal.find('#sfz').attr('src',"data:image/jpeg;base64,"+result['data'][2]);
		if(result['data'][3])modal.find('#cj').attr('src',"data:image/jpeg;base64,"+result['data'][3]);
		modal.find('#s12').html(result['data'][4]);
		modal.find('#s23').html(result['data'][5]);
		modal.find('#s13').html(result['data'][6]);
	},
	xkxq: function(result){
		modal = $('#m'+result['xh']);
		modal.find('#t'+result['xh']).html(result['table']);
	},
	create_pinfo: function(result){
		modal = $('#person-info');
		modal.find('input[name=xm]').val(result['person'][1]);
		modal.find('input[name=xb]').val(result['person'][2]);
		modal.find('input[name=xym]').val(result['person'][4]);
		modal.find('input[name=zym]').val(result['person'][6]);
		modal.find('input[name=ssnj]').val(result['person'][7]);
		modal.find('input[name=bm]').val(result['person'][8]);
	},
	kczh: function(result){
		result.button.hide();
		$('#kczh-table').html(result['table']);
		$("#kczh-table").find('table').tablesorter();
	},
	getDebt: function(result){
		$('#modal'+result['cid']).find('.modal-body').find('.detail').html(result['html']);
	},
	meeting: function(result){
		$('#error').html(result['error']);
	},
	foundPersons: function(result){
		$('#found-persons').html(result['table']);
		$("#tijiaobtn").addClass("no-show");	
		$(document).ready(function(){
			$('.checker').click(function(){
				if($(this).hasClass('fa-circle-o')){
					$(".fa-dot-circle-o").removeClass('fa-dot-circle-o');
					$(this).addClass('fa-dot-circle-o');
					$("#tijiaobtn").removeClass("no-show");	
					$('input[name=gh]')[0].value = $(this).attr('gh')
					$('input[name=xm]')[0].value = $(this).attr('xm')
					$('input[name=xyh]')[0].value = $(this).attr('xyh')
					$('input[name=department]')[0].value = $(this).attr('department')
				}
			});
		});
	},
	debtSearchCustomer: function(result){
		$('#customer-name').val(result['customer-name']);
		$('#customerId').val(result['customerId']);
		$('#customer-cell').val(result['customer-cell']);
		$('#customer-email').val(result['customer-email']);
	},
	redirect: function(result){
		if(result['link']=='refresh'){
			window.location.href = window.location.href;
		}else{
			window.location.href = result['link'];	
		}
	},

}