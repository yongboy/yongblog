function confirmDelete(url){
	if(confirm("Are you sure to delete this blog ?")){
		location = url;
	}
}

function checkForm(){
	var title = document.getElementById("title");
	if(title.value==""){
		alert("The title value is null!");
		return false;
	}
}

function getHtml(){
	alert(navigator.userAgent);
}