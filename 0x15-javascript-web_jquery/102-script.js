$(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/';
  const button = $('INPUT#btn_translate');
  const hello = $('DIV#hello');

  button.click(event => {
    const lang = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: url + '?lang=' + lang,
      success: function (data) {
        hello.text(data.hello);
      }
    });
  });
});
