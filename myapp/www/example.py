import frappe
from distutils.spawn import find_executable


no_cache=1


# def get_context(context):
#     print(data_list)
#     for users in data_list:
#         context.data_list=users 
   

@frappe.whitelist()
def get_details(get_email):
    print("\n\n", get_email, "\n\n")
    return get_email
    