const addItem = $('DIV#add_item');
const myList = $('UL.my_list');
addItem.click(event => myList.append('<li>Item</li>'));
