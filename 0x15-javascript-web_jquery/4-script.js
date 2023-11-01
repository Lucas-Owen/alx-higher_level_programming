const toggleHeader = $('DIV#toggle_header');
toggleHeader.click((event) => {
  if (toggleHeader.hasClass('red')) { toggleHeader.toggleClass('green'); } else { toggleHeader.toggleClass('red'); }
});
