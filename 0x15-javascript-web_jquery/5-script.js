const add_item = $("DIV#add_item");
const my_list = $("UL.my_list")
add_item.click( event => my_list.append("<li>Item</li>"));
