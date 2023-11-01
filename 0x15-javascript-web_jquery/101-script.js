$(function () {
  const myList = $('UL.my_list');
  const addItem = $('DIV#add_item');
  const removeItem = $('DIV#remove_item');
  const clearList = $('DIV#clear_list');
  addItem.click(event => myList.append('<li>Item</li>'));
  removeItem.click(event => $('UL.my_list LI:last-child').remove());
  clearList.click(event => $('UL.my_list LI').remove());
});
