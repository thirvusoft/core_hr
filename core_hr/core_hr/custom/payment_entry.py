import frappe
def create_additional_salary(doc,action):
    ts_value=frappe.get_doc("Core HR Settings")
    if ts_value.ts_employee_advance_automation==1:
        for i in doc.references:
            if(i.reference_doctype=='Employee Advance'):
                advance_doc=frappe.get_doc('Employee Advance',i.reference_name)
                if advance_doc.repay_unclaimed_amount_from_salary == 1:
                    additional_salary_doc=frappe.new_doc('Additional Salary')
                    additional_salary_doc.employee = doc.party
                    additional_salary_doc.salary_component = 'Advance Amount'
                    additional_salary_doc.payroll_date=doc.posting_date
                    additional_salary_doc.amount=i.allocated_amount
                    additional_salary_doc.ref_doctype='Employee Advance'
                    additional_salary_doc.ref_docname=i.reference_name
                    additional_salary_doc.insert()
                    additional_salary_doc.submit()
                    frappe.db.commit()