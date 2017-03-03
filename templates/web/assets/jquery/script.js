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
		var listdata = document.getElementById("list-data");
		$(listdata).html(text);
		$('#data-count').text(listdata.querySelectorAll("span a").length);
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
		events = ["birthdays", "first-timers", "evangelism", "outreach"]

		for(var i = 0; i < events.length; i++){
			loadinfo("welcome/_newsfeed/", events[i]);
		};
	}
	else if (window.location.pathname === "/welcome/"){
		events = ["birthdays", "first-timers", "evangelism", "outreach"]

		for(var i = 0; i < events.length; i++){
			loadinfo("_newsfeed/", events[i]);
		};
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
		var input = document.getElementById("myInput");
		var filter = input.value.toLowerCase();
		var memberlist = document.getElementsByClassName("datalist");
		for (var i=0; i < memberlist.length; i++)

		{
			var name = memberlist[i].querySelector("span a").innerText.toLowerCase();

			if (name.indexOf(filter) > -1){
				memberlist[i].style.display = "";
			}
			else {
				memberlist[i].style.display = "none";
			}
		}

		$('#data-count').text($('#list-data li:visible').size());
	});
});
