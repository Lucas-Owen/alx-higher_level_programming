const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
const listMovies = $('UL#list_movies');
$.ajax({
  type: 'GET',
  url,
  success: function (movies) {
    $.each(movies.results, (i) => listMovies.append('<li>' + movies.results[i].title + '</li>'));
  }
});
