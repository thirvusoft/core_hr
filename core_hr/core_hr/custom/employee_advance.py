import frappe
from erpnext.hr.doctype.employee_advance.employee_advance import make_bank_entry
def create_payment_entry(doc,action):
    ts_employee_advance_automation = frappe.db.get_single_value("Core HR Settings", "ts_employee_advance_automation")
    if ts_employee_advance_automation==1:
                
                payment_doc = make_bank_entry(doc.doctype,doc.name)
                pd = frappe.new_doc('Journal Entry')
                # company = frappe.get_doc('Company',doc.company)
                # abbr=company.abbr
                # payment_doc.posting_date=doc.posting_date
                # payment_doc.paid_from = doc.advance_account
                pd.update(payment_doc)
                pd.insert()
                # payment_doc.submit()