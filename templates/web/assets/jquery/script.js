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

	if (window.location.pathname.endsWith("/member/all/")){
		loaddata("../_group/", "ALL");
	}

	if (window.location.pathname.endsWith("/event/")){
		var start_date = document.getElementById("form1-g-start_date").value;
		var end_date = document.getElementById("form1-g-end_date").value;

		loaddata("../event/_daterange/", start_date + "--" + end_date);
	}
});