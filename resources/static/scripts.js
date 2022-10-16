document.getElementById("button").addEventListener("click", submitURL);
document.getElementById("convert").addEventListener("click", convertURL);
document.getElementById("download").addEventListener("click", downloadURL);
document.getElementById("darkmode").addEventListener("click", changeTheme);
document.getElementById("download").disabled = true;

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

if(urlParams != null && queryString != "") {
	let url = urlParams.get('url');
	let mode = urlParams.get('mode');
	document.getElementById('url').value = url;
	document.getElementById("download").disabled = false;
	document.getElementById("prev").setAttribute("src", url.replace("watch?v=", "embed/"));
	document.getElementById("option-1").checked = (mode == "audio");
	document.getElementById("option-2").checked = (mode == "video");
}

function submitURL() {
	let url = document.getElementById("url").value;
	document.getElementById("prev").setAttribute("src", url.replace("watch?v=", "embed/"));
	document.getElementById("convert").disabled = false;
}

function convertURL() {
	let url = document.getElementById("url").value;
	let mode = document.getElementById("option-1").checked ? "audio" : "video";
	if(url != "")
		window.location=`/download?url=${url}&mode=${mode}`;
}

function downloadURL() {
	let mode = document.getElementById("option-1").checked ? "audio" : "video";
	window.location=`/file?mode=${mode}`;
}

function changeTheme() {
	let dark = document.getElementById("darkmode").checked;
	if (dark) {

	}
}
