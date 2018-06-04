from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _



@frappe.whitelist()
def get_details(doc,method,cost_center_name='',company=''):
	cost_center = frappe.new_doc("Cost Center")
	
	# cost_center_name=test.cost_center_name 
	
	# b = 0
	order_types = doc.order_types
	customer_name = doc.customer_name
	name = doc.name
	# a = order_types
	
	if order_types =="Project":
		
		cost_center.cost_center_name= customer_name+str(name)
		default_cost_center = frappe.db.get_value('Company', doc.company, 'cost_center')
		parent_cost_center = frappe.db.get_value('Cost Center', default_cost_center, 'parent_cost_center')

		cost_center.parent_cost_center= parent_cost_center
		cost_center.company=cost_center.company
		cost_center.name=name
		# cost_center.cost_center_name=cost_center.cost_center_name
	
		cost_center.insert(ignore_permissions=True)
		cost_center.save(ignore_permissions=True)

		project = frappe.new_doc("Project")
		project.project_name=customer_name+str(name)
		project.customer = customer_name
		project.sales_order = name
		
		project.status="Open"
		frappe.msgprint("Project " + project.project_name +" is created")

		project.cost_center = cost_center.name
		project.insert(ignore_permissions=True)
		project.save(ignore_permissions=True)
		frappe.db.commit()
		
	if order_types=="Trading":
		frappe.msgprint("You Have Selected"+" "+order_types+" "+"Order Types")
	# frappe.msgprint("out side if")
	# if order_types =="Project":
	# 	frappe.msgprint("You Have Selected"+" "+order_types+" "+"Order Types")