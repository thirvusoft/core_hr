import frappe
from erpnext.accounts.doctype.payment_entry.payment_entry import get_payment_entry
def create_payment_entry(doc,action):
        ts_value=frappe.get_doc("Core HR Settings")
        if ts_value.ts_employee_advance_automation==1:
                payment_doc = get_payment_entry(doc.doctype,doc.name)
                company = frappe.get_doc('Company',doc.company)
                abbr=company.abbr
                payment_doc.posting_date=doc.posting_date
                payment_doc.paid_from = 'Cash - '+abbr
                payment_doc.save()
                payment_doc.submit()