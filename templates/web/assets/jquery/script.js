$(document).ready(function(){

	$(".alphabet").on('change', function(){
		loaddata("../_group/", $(this).val());
	});

	$(".membership").on('change', function(){
		loaddata("../_status/", $(this).val());
	});

	$(".gender").on('change', function(){
		loaddata("../_gender/", $(this).val());
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

	if (window.location.pathname === "/" || window.location.pathname === "/welcome/"){
		events = ["birthdays", "first-timers", "evangelism", "outreach"]
		
		events.prototype.forEach(function(event){
			loadinfo("welcome/_newsfeed/", event);
		});
	}

	if (window.location.pathname === "/api/"){
		loadapi("model/member.json");
		loadapi("model/event.json");
		loadapi("model/event-type.json");
		loadapi("model/academic-institution.json");
		loadapi("model/attendance.json");
		loadapi("model/gender.json");
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

	$('#myInput').keyup(function() {
		var input, filter, table, tr, td, i;
		input = document.getElementById("myInput");
		filter = input.value.toUpperCase();
		table = document.getElementById("table-data");
		tr = table.getElementsByTagName("tr");

		for (i = 0; i < tr.length; i++) {
			td = tr[i].getElementsByTagName("td")[0];
			if (td) {
				if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
					tr[i].style.display = "";
				} 
				else {
					tr[i].style.display = "none";
				}
			}
		}
	});

});