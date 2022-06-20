frappe.db.get_single_value("Core HR Settings","ts_job_opening_indicator").then(value =>{
    if(value==1){
		frappe.listview_settings['Job Opening'] = {
			get_indicator:function(doc){
				if(doc.status==="Open") {
					return [("Open"), "green", "status,=,Open"];
				} else if(doc.status==="Closed") {
					return [("Closed"), "red", "status,=,Closed"];
				}
			}
		};
	}
})