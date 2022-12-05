
from numpy import indices
from elasticsearch import Elasticsearch, RequestsHttpConnection

def update(index_name,doc_id,comment_status):
    #connecting to ES cluster   
    es=Elasticsearch("http://localhost:9200")
    
    if es.ping():
        print("Connection to Elasticsearch cluster established")
    else:
        print("Connection failed")
    

    #create index if not already present
    if es.indices.exists(index=index_name)==False:
        es.indices.create(index=index_name)
        print("INDEX_NAME:", index_name,"index created.")
        #Insert data into index
        doc1={ "rating" : 4.4, "comment" : "good resource", "resourceID" : "iisc.ac.in/89a36273d77dac4cf38114fca1bbe64392547f86/rs.iudx.io/pune-env-flood", "userID" : "a709a897--4521-86fb-60d7ba6fb888", "status" : "pending" }
        doc2={ "rating" : 2, "comment" : "It sucks", "resourceID" : "iisc.ac.in/89a36273d77dac4cf38114fca1bbe64392547f86/rs.iudx.io/pune-env-flood", "userID" : "b709a897-c1df-4521-86fb-60d7ba6fb888", "status" : "pending" }
        doc3={ "rating" : 1.1, "comment" : "It makes no fucking sense", "resourceID" : "iisc.ac.in/89a36273d77dac4cf38114fca1bbe64392547f86/rs.iudx.io/pune-env-flood", "userID" : "c709a897-c1df-4521-86fb-60d7ba6fb888", "status" : "pending" }

        es.index(index=index_name,body=doc1,id="1a")
        es.index(index=index_name,body=doc2,id="2b")
        es.index(index=index_name,body=doc3,id="3c")
    else:
        #es.indices.delete(index=index_name)
        print("Index already exists")

    #call make_es_database.py to store fresh documents(where status = "pending") for testing
    
    #display all indices
    # indices=es.indices.get_alias("*")
    # for index in indices:
    #     print(index)


    doc_ = es.get(index=index_name, id=doc_id)
    print(doc_['_source'])
    doc={
        "doc":{
            "status":comment_status
        }
    }
    es.update(index=index_name,id=doc_id, body=doc)
    es.indices.refresh(index=index_name)
    update_doc = es.get(index=index_name, id=doc_id)
    print(update_doc['_source'])
    print("Database Updated")


