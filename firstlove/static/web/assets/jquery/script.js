$(document).ready(function(){

	$(".alphabet").click(function(){
		loaddata($(this).attr('id'));
	});

	function tt(text, id)
	{
		 $('#table-data tbody').text("");
		 $('#table-data tbody').append(text);
		 $('#data-count').text($("#table-data > tbody > tr").length);
	}

	function loaddata(id){

		$.ajax({
			// type: "POST",
			url: "../_group/" + id, 
			success: function(result){
				tt(result, id);
    		}
    	});
	}
	loaddata("ALL")
});