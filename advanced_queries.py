import json

#best_filds
def multi_match_agg_best(query, fields=['author_name']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 986,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "best_fields"
			}
		},
		"aggs": {
			"Genre Filter": {
				"terms": {
					"field": "genre.keyword",
					"size": 10
				}
			},
			"Music Filter": {
				"terms": {
					"field": "music.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyrics Filter": {
				"terms": {
					"field": "lyrics.keyword",
					"size": 10
				}
			}
		}
	}

	q = json.dumps(q)
	return q


def multi_match_agg_sort_best(query, sort_num, fields=['title','song_lyrics']):
	print ('sort num is ',sort_num)
	q = {
		"size": sort_num,
		"sort": [
			{"views": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "best_fields"
			}
		},
		"aggs": {
			"Genre Filter": {
				"terms": {
					"field": "genre.keyword",
					"size": 10
				}
			},
			"Music Filter": {
				"terms": {
					"field": "music.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyrics Filter": {
				"terms": {
					"field": "lyrics.keyword",
					"size": 10
				}
			}
		}
	}
	q = json.dumps(q)
	return q

#cross_filds
def multi_match_agg_cross(query, fields):
	print ("QUERY FIELDS")
	print (fields)
	print(query)
	q = {
		"size": 103,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"BirthPlace Filter": {
				"terms": {
					"field": "birth_place.keyword",
					"size": 10
				}
			},
			"Book Filter": {
				"terms": {
					"field": "book_list.keyword",
					"size": 10
				}
			},
			"Author Filter": {
				"terms": {
					"field": "author_name.keyword",
					"size": 10
				}
			},
			"Category Filter": {
				"terms": {
					"field": "category.keyword",
					"size": 10
				}
			}
		}
	}

	q = json.dumps(q)
	return q


def multi_match_agg_sort_cross(query, sort_num, fields=['title','song_lyrics']):
	print ('sort num is ',sort_num)
	q = {
		"size": sort_num,
		"sort": [
			{"views": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"Genre Filter": {
				"terms": {
					"field": "sinhala_genre.keyword",
					"size": 10
				}
			},
			"Music Filter": {
				"terms": {
					"field": "sinhala_music.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "sinhala_artist.keyword",
					"size": 10
				}
			},
			"Lyrics Filter": {
				"terms": {
					"field": "sinhala_lyrics.keyword",
					"size": 10
				}
			}
		}
	}
	q = json.dumps(q)
	return q


#phrase_filds
def multi_match_agg_phrase(query, fields=['author_name']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 986,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"BirthPlace Filter": {
				"terms": {
					"field": "birth_place.keyword",
					"size": 10
				}
			},
			"Book Filter": {
				"terms": {
					"field": "book_list.keyword",
					"size": 10
				}
			},
			"Author Filter": {
				"terms": {
					"field": "author_name.keyword",
					"size": 10
				}
			},
			"Category Filter": {
				"terms": {
					"field": "category.keyword",
					"size": 10
				}
			}
		}
	}
    
	q = json.dumps(q)
	return q


def multi_match_agg_sort_phrase(query, sort_num, fields=['title','song_lyrics']):
	print ('sort num is ',sort_num)
	q = {
		"size": sort_num,
		"sort": [
			{"views": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"Genre Filter": {
				"terms": {
					"field": "genre.keyword",
					"size": 10
				}
			},
			"Music Filter": {
				"terms": {
					"field": "music.keyword",
					"size": 10
				}
			},
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyrics Filter": {
				"terms": {
					"field": "lyrics.keyword",
					"size": 10
				}
			}
		}
	}
	q = json.dumps(q)
	return q

