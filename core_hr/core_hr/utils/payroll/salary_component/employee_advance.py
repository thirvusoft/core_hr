import frappe
def salary_component_creation():
    if not frappe.db.exists("Salary Component","Employee Advance"):
        doc=frappe.new_doc("Salary Component")
        doc.salary_component = "Employee Advance"
        doc.salary_component_abbr = "EA"
        doc.type = "Deduction"
        doc.save()