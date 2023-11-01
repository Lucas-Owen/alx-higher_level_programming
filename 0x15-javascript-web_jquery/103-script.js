$(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/';
  const button = $('INPUT#btn_translate');
  const hello = $('DIV#hello');

  function getTranslation () {
    const lang = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: url + '?lang=' + lang,
      success: function (data) {
        hello.text(data.hello);
      }
    });
  }
  button.click(getTranslation);
  $('INPUT#language_code').keypress((event) => {
    if (event.keyCode === 13) { getTranslation(); }
  });
});
