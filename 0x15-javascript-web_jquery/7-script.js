const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
const character = $('DIV#character');
$.ajax({
  type: 'GET',
  url,
  success: function (data) {
    character.text(data.name);
  }
});
