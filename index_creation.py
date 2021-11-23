from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json,re,os
client = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'book-author-index'


def createIndex():
    settings = {
        "settings": {
            "index":{
                "number_of_shards": "1",
                "number_of_replicas": "1"
            },
            "analysis" :{
                "analyzer":{
                    "sinhala-analyzer":{
                        "type": "custom",
                        "tokenizer": "icu_tokenizer",
                        "filter":["edge_ngram_custom_filter"]
                    }
                },
                "filter" : {
                    "edge_ngram_custom_filter":{
                        "type": "edge_ngram",
                        "min_gram" : 2,
                        "max_gram" : 50,
                        "side" : "front"
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                    "author_name": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "date_of_birth": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "birth_place": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "school": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "book_list": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "about_author": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "language": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "author_name_english": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                    "birth_place_english": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                    
            }
        }
    }


    # index = Index(INDEX,using=client)
    # result = index.create()
    result = client.indices.create(index=INDEX , body =settings)
    print (result)


def read_translated_authors():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file1 = os.path.join(THIS_FOLDER, 'data')
    my_file = os.path.join(my_file1, 'formatted_authors.json')
    
    with open(my_file,'r',encoding='utf-8-sig') as tra_file:
        tra_authors = json.loads(tra_file.read())
        results_list = [a for num, a in enumerate(tra_authors) if a not in tra_authors[num + 1:]]
        return results_list


def clean_function(song_lyrics):
    if (song_lyrics):
        processed_list = []
        song_lines = song_lyrics.split('\n')
        
        for place,s_line in enumerate(song_lines):
            process_line = re.sub('\s+',' ',s_line)
            punc_process_line = re.sub('[.!?\\-]', '', process_line)
            processed_list.append(punc_process_line)
        
        sen_count = len(processed_list)
        final_processed_list = []
        
        for place,s_line in enumerate(processed_list):
            if (s_line=='' or s_line==' '):
                if (place!= sen_count-1 and (processed_list[place+1]==' ' or processed_list[place+1]=='')) :
                    pass
                else:
                    final_processed_list.append(s_line)
            else:
                final_processed_list.append(s_line)
        final_song_lyrics = '\n'.join(final_processed_list)
        return final_song_lyrics
    else:
        return None

def data_generation(author_array):
    for author in author_array:

        author_name = author["author_name"]
        author_name_english = author["author_name_english"]
        date_of_birth = author['date_of_birth']
        birth_place = author["birth_place"]
        birth_place_english = author["birth_place_english"]
        school = author["school"]
        book_list = author["book_list"]
        about_author = author["about_author"]
        category = author["category"]
        language = author["language"]
        

        yield {
            "_index": INDEX,
            "_source": {
                "author_name": author_name,
                "author_name_english": author_name_english,
                "date_of_birth": date_of_birth,
                "birth_place": birth_place,
                "birth_place_english": birth_place_english,
                "school": school,
                "book_list": book_list,
                "about_author": about_author,
                "category": category,
                "language": language
            },
        }


createIndex()
translated_authors = read_translated_authors()
helpers.bulk(client,data_generation(translated_authors))