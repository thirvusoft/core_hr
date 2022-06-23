
frappe.listview_settings['Job Opening'] = {
	get_indicator:function(doc){
		if(doc.status==="Open") {
			return [("Open"), "green", "status,=,Open"];
		} else if(doc.status==="Closed") {
			return [("Closed"), "red", "status,=,Closed"];
		}
	}
};