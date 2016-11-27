$(document).ready(function(){

	$(".alphabet").click(function(){
		loaddata("../_group/", $(this).attr('id'));
	});

	$(".membership").click(function(){
		loaddata("../_status/", $(this).attr('id'));
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
});