from elasticsearch import Elasticsearch, RequestsHttpConnection
index_name = "cat-rating"

#connecting to ES cluster   
es=Elasticsearch("http://localhost:9200")
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
    es.indices.delete(index=index_name)
    es.indices.create(index=index_name)
    #Insert data into index
    doc1={ "rating" : 4.4, "comment" : "good resource", "resourceID" : "iisc.ac.in/89a36273d77dac4cf38114fca1bbe64392547f86/rs.iudx.io/pune-env-flood", "userID" : "a709a897--4521-86fb-60d7ba6fb888", "status" : "pending" }
    doc2={ "rating" : 2, "comment" : "It sucks", "resourceID" : "iisc.ac.in/89a36273d77dac4cf38114fca1bbe64392547f86/rs.iudx.io/pune-env-flood", "userID" : "b709a897-c1df-4521-86fb-60d7ba6fb888", "status" : "pending" }
    doc3={ "rating" : 1.1, "comment" : "It makes no fucking sense", "resourceID" : "iisc.ac.in/89a36273d77dac4cf38114fca1bbe64392547f86/rs.iudx.io/pune-env-flood", "userID" : "c709a897-c1df-4521-86fb-60d7ba6fb888", "status" : "pending" }

    es.index(index=index_name,body=doc1,id="1a")
    es.index(index=index_name,body=doc2,id="2b")
    es.index(index=index_name,body=doc3,id="3c")
    print("Index prepared")

# es.indices.delete(index="cat-rating")
# es.indices.delete(index="cat_rating")
