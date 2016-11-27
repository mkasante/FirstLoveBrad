$(document).ready(function(){

	$(".alphabet").click(function(){
		loaddata("../_group/", $(this).attr('id'));
	});

	$(".membership").click(function(){
		loaddata("../_status/", $(this).attr('id'));
	});

	$(".event_date").click(function(){
		loaddata("../event/_daterange/", $(this).attr('id'));
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

	if (window.location.pathname.endsWith("/member/all/")){
		loaddata("../_group/", "ALL");
	}

	if (window.location.pathname.endsWith("/event/")){
		var today = new Date().toDateString().split(" ")
		var dd = today[2]
		var mm = today[1]
		var yyyy = today[3]
		today = dd + " " + mm + " " + yyyy

		loaddata("../event/_daterange/", "01 Jan 2015-" + today);
	}
});