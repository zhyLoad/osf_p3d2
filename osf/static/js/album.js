$(document).ready(function(){
	var photos = [];
	var csrftoken = getCookie('csrftoken');

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
	$('#uploader_input').live('change', function(event) {
	   $.ajaxFileUpload({
	                		url: basePath+'/album/upload/photo', 
	                		secureuri:false,
							data: { 'csrfmiddlewaretoken': getCookie('csrftoken'), },
	                		fileElementId:'uploader_input',
	                		success: function (data, status){
	                				data = jQuery(data).find('pre:first').text();
	                				data = jQuery.parseJSON(data);
	                				var $imgCard = $('<div class="card" id="card'+data.id+'">'+
				    									'<a class="image" href="#">'+
				      										'<img src="'+img_base_url+data.key+album_thumbnail+'">'+
				    									'</a>'+
				    									'<div class="content">'+
				    										'<textarea rows="" cols="" placeholder="添加描述..."></textarea>'+
				    									'</div>'+
				    									'<div class="extra meta">'+
															'<a href="#"><i class="delete icon"></i>删除</a>'+
				    									'</div>'+
				  									'</div>');
	                				$('#uploadedphotos').append($imgCard);

	                    			if(typeof(data.error) != 'undefined')
	                   				{
				                        if(data.error != '')
				                        {
				                            alert(data.error);
				                        }else
				                        {
				                            alert(data.msg);
				                        }
	                    			}
	                		},
	                		error: function (data, status, e){
	                    			alert(e);
	                		}
	            		}
	        		) ;
	});

	$('#saveAlbumBtn').click(function(event) {
		$(this).addClass('loading');
		$('#uploadedphotos .card').each(function(index, el) {
			var photo_id = $(this).attr('id').substring(4);
			var photo_desc = $(this).find('textarea:first()').val();
			photos.push({"id":photo_id, "desc":photo_desc});
		});
		var album_desc = $('#album_desc').val();

		$.ajax({
			url: basePath+'/album/create',
			type: 'POST',
			dataType: 'json',
			contentType:'application/json;charset=UTF-8',
			data: JSON.stringify({album_desc: album_desc, photos: photos, tags: tags, csrfmiddlewaretoken: getCookie('csrftoken'),})
		})
		.done(function(data) {
			var status = data.status;
			//var author = data.album.user_id;
			if(SUCCESS_ALBUM_CREATE == status || SUCCESS_ALBUM_UPDATE == status) {
				self.location = basePath;
			}
		})
		.fail(function() {
			console.log("error");
		})
		.always(function() {
			console.log("complete");
		});
		
	});
	
	$('.delete.icon').live('click', function(){
		var card = $(this).parents('.card');
		var photo_id = $(card).attr('id').substring(4);
		var that = this;
		$.ajax({
			url: basePath+'/album/delete/photo/'+photo_id,
			type: 'GET',
			dataType: 'json'
		})
		.success(function(data){
			if(data.status == SUCCESS_PHOTO_DELETE){
				$(card).remove();
			}
			
		});
		return false;
	});

})