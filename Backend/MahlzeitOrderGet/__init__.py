import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, doc: func.DocumentList) -> func.HttpResponse:
    logging.info('Mahlzeit Order Request')
    
    orders_json = []

    for order in doc:
        logging.info(order['id'])
        order_json = {
           "id": order['id'],
           "description": order['description']
        }
        orders_json.append(order_json)

    return func.HttpResponse(
            json.dumps(orders_json),
            status_code=200,
            mimetype="application/json"            
    )