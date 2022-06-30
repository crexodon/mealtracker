import logging
import json

import azure.functions as func


def main(req: func.HttpRequest, doc: func.DocumentList) -> func.HttpResponse:
    logging.info('Mahlzeit Order Get Id Request')

    id = req.route_params.get('id')
    orders_json = []

    for order in doc:
        if(order['id'] == id):
            order_json = {
           "id": order['id'],
           "description": order['description']
            }
            orders_json.append(order_json)
        else:
            return func.HttpResponse(status_code=404)
        

    return func.HttpResponse(
            json.dumps(orders_json),
            status_code=200,
            mimetype="application/json"            
    )