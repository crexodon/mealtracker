import logging

import azure.functions as func


def main(req: func.HttpRequest, doc:func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Mahlzeit Customer Put Id Request')

    # customer id
    id = req.route_params.get('id')
    name = ""


    
    # get name from json body
    if req.get_json():
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    # when id then write into DB
    if id:
        new_docs = func.DocumentList() 
        newproduct_dict = {
            "id": id,
            "name": name
        }
        new_docs.append(func.Document.from_dict(newproduct_dict))
        doc.set(new_docs)

        return func.HttpResponse(status_code=200)
    else:
        return func.HttpResponse(status_code=400)
