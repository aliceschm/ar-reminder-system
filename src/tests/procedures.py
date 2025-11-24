from src.procedures.update_invoices import update_invoices

try:
    update_invoices()
    print('Success!')
except Exception as e:
    print(e)

