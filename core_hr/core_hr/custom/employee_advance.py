import frappe
def create_payment_entry(doc,action):
        payment_doc=frappe.new_doc('Payment Entry')
        payment_doc.payment_type='Pay'
        payment_doc.party_type = 'Employee'
        payment_doc.party = doc.employee
        payment_doc.posting_date = doc.posting_date
        payment_doc.posting_date = doc.posting_date
        payment_doc.paid_from_account_currency = doc.currency
        payment_doc.mode_of_payment = doc.mode_of_payment
        payment_doc.paid_amount=doc.advance_amount
        payment_doc.received_amount=doc.advance_amount
        payment_doc.source_exchange_rate=1.0
        payment_doc.target_exchange_rate=1.0
        payment_doc.paid_to=doc.advance_account
        payment_doc.paid_from=doc.advance_account
        payment_doc.append(
		"references",
		{
                        "reference_doctype": 'Employee Advance',
                        "reference_name": doc.name,
                        "total_amount": doc.advance_amount,
                        "outstanding_amount": doc.advance_amount,
                        "allocated_amount": doc.advance_amount,
                },
        )

        payment_doc.insert()
        payment_doc.submit()        
        frappe.db.commit()