# Fuzzy matching template
GET bbuy_products/_search
{
  "query": {
    "match": {
      "name.hyphens":{
        "query": "iphone4",
        "fuzziness": 2,
        "prefix_length": 2
      }

    }
  },
  "_source": "name"
}
