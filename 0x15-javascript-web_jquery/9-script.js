$(function () {
	const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
	const hello = $("DIV#hello")
	$.ajax({
		type: "GET",
		url: url,
		success: function(data) {
			hello.text(data.hello);
		}
	});
});
