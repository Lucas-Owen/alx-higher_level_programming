$(function () {
	const my_list = $("UL.my_list")
	const add_item = $("DIV#add_item");
	const remove_item = $("DIV#remove_item");
	const clear_list = $("DIV#clear_list");
	add_item.click( event => my_list.append("<li>Item</li>"));
	remove_item.click( event => $("UL.my_list LI:last-child").remove());
	clear_list.click( event => $("UL.my_list LI").remove());
});
