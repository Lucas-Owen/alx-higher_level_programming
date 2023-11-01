const url = "https://swapi-api.alx-tools.com/api/films/?format=json";
const list_movies = $("UL#list_movies")
$.ajax({
	type: "GET",
	url: url,
	success: function(movies) {
		$.each(movies, (movie) => list_movies.append("<li>" + movie.title + "</li>"))
	}
});
