# coding=utf-8
from datetime import datetime

from elasticsearch import Elasticsearch
from elasticsearch import helpers

def set_mapping(es, index_name="content_engine", doc_type_name="en"):
    my_mapping = {
                "properties": {
                    "Num": {
                        "type": "keyword"
                    },
                    "Journal_Name": {
                        "type": "text"
                    },
                    "Song_Name": {
                        "type": "text"
                    },
                    "Singer": {
                        "type": "text"
                    },
                    "Album_Name": {
                        "type": "text"

                    }
                }
    }


create_index = es.indices.create(index=index_name,body=my_mapping)		#{u'acknowledged': True}
mapping_index = es.indices.put_mapping(index=index_name, doc_type=doc_type_name, body=my_mapping)		#{u'acknowledged': True}
if create_index["acknowledged"]!=True or mapping_index["acknowledged"]!=True:
    print("Index creation failed...")




def set_data(index_name="content_engine", doc_type_name="en"):
# def set_data(es, input_file, index_name="content_engine", doc_type_name="en"):
    actions = []

    f = open('data_content.txt')
    i = 1
    for line in f:
        line = line.strip().split(' ')
        action = {
            "_index": index_name,
            "_type": doc_type_name,
            "_id": i,
            "_source": {
                u"Num": line[0].decode('utf8'),
                u"Journal_Name": line[1].decode('utf8'),
                u"Song_Name": line[2].decode('utf8'),
                u"Singer": line[3].decode('utf8'),
                u"Album_Name": line[4].decode('utf8'),

            }
        }
        i += 1

        actions.append(action)

        success, _ = bulk(es, ACTIONS, index=index_name, raise_on_error=True)
        print('Performed %d actions' % success)

    #     if (len(actions) == 500):
    #         helpers.bulk(es, actions)
    #         del actions[0:len(actions)]
    #
    # if (len(actions) > 0):
    #     helpers.bulk(es, actions)

    if __name__ == '__main__':
        es = Elasticsearch()
        set_mapping(es)
        set_data