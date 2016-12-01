$(document).ready(function(){

	$(".alphabet").on('change', function(){
		loaddata("../_group/", $(this).val());
	});

	$(".membership").on('change', function(){
		loaddata("../_status/", $(this).val());
	});

	$(".event_date#btn-date").click(function(){
		var start_date = document.getElementById("form1-g-start_date").value;
		var end_date = document.getElementById("form1-g-end_date").value;

		loaddata("../event/_daterange/", start_date + "--" + end_date);
	});

	$(".event_types").on('change', function(){
		loaddata("../event/_eventtype/", $(this).val());
	});

	function tt(text, suburl, id)
	{
		 $('#table-data tbody').text("");
		 $('#table-data tbody').append(text);
		 $('#data-count').text($("#table-data > tbody > tr").length);
	}

	function loaddata(suburl, id){

		$.ajax({
			// type: "POST",
			url: suburl + id, 
			success: function(result){
				tt(result, suburl, id);
    		}
    	});
	}

	function loadinfo(suburl, id){

		$.ajax({
			// type: "POST",
			url: suburl + id, 
			success: function(result){
				$('#anouncements').append(result);
    		}
    	});
	}


	if (window.location.pathname.endsWith("/member/all/")){
		loaddata("../_group/", "ALL");
	}

	if (window.location.pathname.endsWith("/event/")){
		var start_date = document.getElementById("form1-g-start_date").value;
		var end_date = document.getElementById("form1-g-end_date").value;

		loaddata("../event/_daterange/", start_date + "--" + end_date);
	}

	if (window.location.pathname === "/"){
		loadinfo("welcome/_newsfeed/", "birthdays");
		loadinfo("welcome/_newsfeed/", "first-timers");
		loadinfo("welcome/_newsfeed/", "evangelism");

		loadapi("welcome/__api/member");
		loadapi("welcome/__api/event");
		loadapi("welcome/__api/academic-institution");
		loadapi("welcome/__api/attendance");

	}
	else if (window.location.pathname === "/welcome/"){
		loadinfo("_newsfeed/", "birthdays");
		loadinfo("_newsfeed/", "first-timers");
		loadinfo("_newsfeed/", "evangelism");

		loadapi("__api/member");
		loadapi("__api/event");
		loadapi("__api/academic-institution");
		loadapi("__api/attendance");		
	}

	function loadapi(url){

		$.ajax({
			// type: "POST",
			url: url, 
			success: function(result){
				$('#anouncements').append(result);
    		}
    	});
	}
});