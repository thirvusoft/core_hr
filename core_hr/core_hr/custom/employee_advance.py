import frappe
from erpnext.hr.doctype.employee_advance.employee_advance import make_bank_entry
def create_payment_entry(doc,action):
    ts_employee_advance_automation = frappe.db.get_single_value("Core HR Settings", "ts_employee_advance_automation")
    if ts_employee_advance_automation==1:
                payment_doc = make_bank_entry(doc.doctype,doc.name)
                pd = frappe.new_doc('Journal Entry')
                pd.update(payment_doc)
                for row in pd.accounts:
                    row.location=doc.location
                pd.voucher_type="Journal Entry"
                pd.insert()
                pd.submit()