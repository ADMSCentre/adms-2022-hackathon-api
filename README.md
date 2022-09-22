# Australian Ad Observatory Dashboard API



The purpose of this `readme` file is to educate and encourage usage of the Australian Ad Observatory's database API, for the purpose of exploring advertisement data collected for the duration of the research project. The API has a few major functions, which are detailed as follows:

_**Note:** All 'HTTP API Responses' shown here are derived from the escaped JSON outputs of the respective response's 'body' content_.

_**Note:** All functionality is IP-gated, meaning that if a client sends more than the acceptable amount of requests to the API within a short window of time, their further attempts will be throttled._



### API Endpoint

The Australian Ad Observatory Dashboard HTTP API implements all of its functionality through POST requests on the following endpoint:

​		__API Endpoint URL:__ `https://i7dy5tidoi.execute-api.us-east-2.amazonaws.com/default/fta-dashboard-instance`

### Datatypes

| Symbol    | Description                     |
| --------- | ------------------------------- |
| 🆂         | String datatype                 |
| 🅱         | Boolean datatype                |
| 🅸         | Integer datatype                |
| 🅾         | Object datatype                 |
| [ 🆂 ... ] | List of the associated datatype |



### Authenticating By User Credentials To Retrieve A Session Token

Prior to the hackathon, you would've received a set of user credentials that help us authenticate your usage of the API, as well as the Australian Ad Observatory interactive dashboard:

| Input               | Description                                                  | Datatype |
| ------------------- | ------------------------------------------------------------ | -------- |
| `action`            | To call the authentication function, specify the `authenticate` action. | 🆂        |
| `data` ↣ `username` | Your username credential.                                    | 🆂        |
| `data` ↣ `password` | Your password credential.                                    | 🆂        |

In order to begin usage with the API, you'll need to provide your credentials, such that you can be issued a session token:

| Output          | Description                                                  | Datatype |
| --------------- | ------------------------------------------------------------ | -------- |
| `success`       | Whether or not the session token could be successfully generated. | 🅱        |
| `session_token` | The session token that should be retained for further usage. | 🆂        |

___Example HTTP API Request___

```json
{
  "action" : "authenticate",
  "data" : {
    "username" : "a_test_user",
    "password" : "a_test_users_password"
  }
}
```

___Example HTTP API Response___

```json
{
  "success": true, 
  "session_token": "aa97406a-1529-4a56-9d84-47e93bc3bf65"
}
```

_Note: Your session token is valid for 3 days after it is generated. After that, you will need to re-authenticate to generate a new session token._



### Querying The Ads Database For Platform Items

Once you have a session token, you can begin querying the Australian Ad Observatory ads database. Numerous filters have been built into the API to help you find the ads that match your search criteria. Complete details of the query function capabilities are given as follows:

| Input                                                        | Description                                                  | Datatype  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | --------- |
| `action `                                                    | To call the query function, specify the `platform_items` action. | 🆂         |
| `data` ↣ `session_token`                                     | The session token retrieved from authentication, which enables the query. | 🆂         |
| `data` ↣ `query ` ↣ `type`                                   | The type of query that is being executed; there are presently 7 query types that are acceptable. The initial 6 types are so named by the properties for which the returned platform items are attributes: `advertiser_id`, `platform_item_id`, `creative_id`, `collation_id`, `business_id`, `archive_id`. The remaining type, `open_search`, returns all platform items that coincide with the filters of the query. As a shorthand, inhibiting the `type` key of the request payload defaults to the `open_search` type. | 🆂         |
| `data` ↣ `query ` ↣ `value`                                  | This is the value that will be queried with respect to the `type` key, and is ignored when the `type` key is declared as `open_search`. | 🆂         |
| `data` ↣ `query ` ↣ `pagination_id`                          | It is common that when results are returned by the API, that not all results can be loaded at once. To overcome this, a pagination ID can be inserted to offset the index of results that should be returned. When unspecified, the `pagination_id` defaults to a value of `0` (i.e. the first page of results returned for the specific query). | 🆂         |
| `data` ↣ `query ` ↣ `remove_missing_entries`                 | When the results are returned from the query, certain platform items may still be unprocessed and unable to load from the URLs returned in the response's `presigned_urls` list. By specifying `true` for `remove_missing_entries`, said unprocessed platform items are automatically removed. Note that this will slow down API request processing times. | 🅱         |
| `data` ↣ `query ` ↣ `number_of_results_to_get`               | The number of results to return from the API - by default, this is set to `50`, with an upper limit of `5000` results that can be returned within a singled request. | 🅸         |
| `data` ↣ `query ` ↣ `filters` ↣ `demographics` ↣ `gender`    | The `gender` key filters platform items observed by demographics of the associated value(s). The appropriate values to filter (which should be provided in list form) are as follows: `["Male", "Female", "Other", "Prefer not to say"]`. When the `gender` key is inhibited, all genders are accepted. | [ 🆂 ... ] |
| `data` ↣ `query ` ↣ `filters` ↣ `demographics` ↣ `age`       | The `age` key filters platform items observed by demographics of the associated value(s). The appropriate values to filter (which should be provided in list form) are as follows: `["18 - 24",  "25 - 34", "35 - 44", "45 - 54", "55 - 64", "65 - 74", "75 and over", "Prefer not to say"]`. When the `age` key is inhibited, all ages are accepted. | [ 🆂 ... ] |
| `data` ↣ `query ` ↣ `filters` ↣ `demographics` ↣ `state`     | The `state` key filters platform items observed by demographics of the associated value(s). The appropriate values to filter (which should be provided in list form) are as follows: `["QLD", "NSW", "VIC", "NT", "SA", "TAS", "ACT", "WA", "Prefer not to say"]`. When the `state` key is inhibited, all states are accepted. | [ 🆂 ... ] |
| `data` ↣ `query ` ↣ `filters` ↣ `demographics` ↣ `income_bracket` | The `income_bracket` key filters platform items observed by demographics of the associated value(s). The appropriate values to filter (which should be provided in list form) are as follows: `["$1 - $15,599", "$15,600 - $20,799", "$20,800 - $25,999", "$26,000 - $33,799", "$33,800 - $41,599", "$41,600 - $51,999", "$52,000 - $64,999", "$65,000 - $77,999", "$78,000 - $90,999", "$91,000 - $103,999", "$104,000 - $155,999", "$156,000 or more", "Prefer not to say"]`. When the `income_bracket` key is inhibited, all income brackets are accepted. | [ 🆂 ... ] |
| `data` ↣ `query ` ↣ `filters` ↣ `demographics` ↣ `level_education` | The `level_education` key filters platform items observed by demographics of the associated value(s). The appropriate values to filter (which should be provided in list form) are as follows: `["Less than year 12 or equivalent", "Year 12 or equivalent", "Vocational Qualification", "Bachelor degree level", "Doctorate", "Postgraduate degree level", "Prefer not to say"]`. When the `level_education` key is inhibited, all levels of education are accepted. | [ 🆂 ... ] |
| `data` ↣ `query ` ↣ `filters` ↣ `demographics` ↣ `language`  | The `language` key filters platform items observed by demographics of the associated value(s). The appropriate values to filter (which should be provided in list form) are as follows: `["English", "Punjabi", "Australian Kriol", "Mandarin", "Cantonese", "Other (please specify)", "Tamil", "Hindi", "Arabic", "Filipino / Tagalog", "German", "Vietnamese", "Spanish", "Greek", "Prefer not to say"]`. When the `language` key is inhibited, all languages are accepted. | [ 🆂 ... ] |
| `data` ↣ `query ` ↣ `filters` ↣ `demographics` ↣ `employment_status` | The `employment_status` key filters platform items observed by demographics of the associated value(s). The appropriate values to filter (which should be provided in list form) are as follows: `["Employed full time", "Unemployed and not looking for work", "Employed part time", "Unemployed and looking for work", "At home carer full time", "Retired", "Prefer not to say"]`. When the `employment_status` key is inhibited, all employment statuses are accepted. | [ 🆂 ... ] |
| `data` ↣ `query ` ↣ `filters` ↣ `demographics` ↣ `identify_aboriginal_torres_strait` | The `identify_aboriginal_torres_strait` key filters platform items observed by demographics of the associated value(s). The appropriate values to filter (which should be provided in list form) are as follows: `["True", "False", "Unknown"]`. When the `identify_aboriginal_torres_strait` key is inhibited, all manners of identity are accepted. | [ 🆂 ... ] |
| `data` ↣ `query ` ↣ `filters` ↣ `demographics` ↣ `party_preference` | The `party_preference` key filters platform items observed by demographics of the associated value(s). The appropriate values to filter (which should be provided in list form) are as follows: `["Greens", "Labor", "One Nation", "Liberal", "None", "Other (please specify)", "National", "Undecided", "Prefer not to say"]`. When the `party_preference` key is inhibited, all party preferences are accepted. | [ 🆂 ... ] |
| `data` ↣ `query ` ↣ `filters` ↣ `raw_texts`                  | The `raw_texts` filter can be used to filter for advertisements that contain one or more texts within their body, advertiser details, or associated political disclaimer. | [ 🆂 ... ] |
| `data` ↣ `query ` ↣ `filters` ↣ `waist_interest_codes`       | The `waist_interest_codes` filter queries for advertisements that contain one or more WAIST interest codes as part of their targeting data. Note that to determine the WAIST interest codes can be queried, please refer to the __'Determining All WAIST Interest Codes That Can Be Queried'__ section of this help documentation. | [ 🆂 ... ] |
| `data` ↣ `query ` ↣ `filters` ↣ `time_range` ↣ `start`       | The `time_range` filter queries for advertisements that were observed within a given time range. As part of this filter, the `start` key specifies the beginning of the time range, and is interpreted as a UNIX timestamp (in seconds). | 🅸         |
| `data` ↣ `query ` ↣ `filters` ↣ `time_range` ↣ `end`         | The `time_range` filter queries for advertisements that were observed within a given time range. As part of this filter, the `end` key specifies the end of the time range, and is interpreted as a UNIX timestamp (in seconds). | 🅸         |

Once the request payload has been sent, the response will return the platform items that correspond to the associated query, along with statistics regarding the request:

| Output                                     | Description                                                  | __Datatype__ |
| ------------------------------------------ | ------------------------------------------------------------ | ------------ |
| `success`                                  | Whether or not the query succeeded.                          | 🅱            |
| `data` ↣ `results ` ↣ `platform_item_ids`  | The list of platform item IDs that have been returned by the query. | [ 🆂 ... ]    |
| `data` ↣ `results ` ↣ `n_total`            | The total number of platform items that have been returned by the query, and not the response itself. Note that this value may be an integer when the number of results is known. Where the total number of results is exceptionally large, a string of value `Unknown` is returned. | 🅸 \| 🆂       |
| `data` ↣ `results ` ↣ `n_paginated`        | The number of platform items that have been paginated in the response to the request, as a subset of the total number of platform items that have been returned by the query. | 🅸            |
| `data` ↣ `results ` ↣ `next_pagination_id` | When there are many platform items to be returned from the API response, not all can be returned at once. For this purpose, paginations deliver subsets of the total results. For any given pagination, a `next_pagination_id` is returned when the returned results are not equivalent to the total results. The value of the `next_pagination_id` can then be fed back into another request as the `pagination_id` to receive the next pagination of the total results for the relative query. | 🆂            |
| `data` ↣ `errors `                         | Depending on whether or not the query is correctly specified, the response may yield errors, which are contained in the `errors` object list. | [ 🅾 ... ]    |
| `data` ↣ `errors ` ↣ 🅾 ↣ `type`            | For any error object, the `type` of error provides a code that can be used to distinguish the error that has been returned by the API. | 🆂            |
| `data` ↣ `errors ` ↣ 🅾 ↣ `details`         | For any error object, the `details` of error provide useful information to help debug the error. | 🆂            |
| `data` ↣ `time_taken`                      | The `time_taken` to resolve the query.                       | 🅵            |
| `data` ↣ `presigned_urls`                  | The `presigned_urls` contain the list of URL objects that correspond to the JSON data of the platform items. Any object takes the form `{ "platform_item_id" : "https://some_url" }`, where the `platform_item_id` is the platform item ID of the associated item, and the value is the corresponding URL. Note that some platform items may be unprocessed prior to retrieval, and so it should be noted that their corresponding links may not work in some circumstances. | [ 🅾 ... ]    |

___Example HTTP API Request___

```json
{
"action" : "platform_items",
"data" : {
	"session_token" : "session_token",
	"query" : {
    "type" : "advertiser_id",
    "value" : "1234567890",
		"pagination_id" : 0,
    "remove_missing_entries" : true,
		"number_of_results_to_get" : 50,
		"filters" : {
			"demographics" : {
        "gender" : [
          "Female"
        ],
        "age" : [
          "18 - 24", 
          "25 - 34", 
          "35 - 44"
        ],
        "state" : [
          "QLD",
          "NSW",
          "VIC"
        ],
       "income_bracket" : [
         "$41,600 - $51,999", 
         "$52,000 - $64,999", 
         "$65,000 - $77,999", 
         "$78,000 - $90,999"
       ],
        "level_education" : [
					"Prefer not to say",
					"Vocational Qualification",
					"Doctorate"
        ],
        "language" : [
          "Filipino / Tagalog",
          "German",
          "Vietnamese",
          "Prefer not to say",
          "Spanish",
          "Greek"
        ],
        "employment_status" : [
          "Employed full time",
          "Unemployed and not looking for work",
          "Employed part time"
        ],
        "identify_aboriginal_torres_strait" : [
          "True",
          "False",
          "Unknown"
        ],
        "party_preference" : [
          "Labor", 
          "One Nation"
        ]
      },
			"raw_texts" : [
        "A raw text query"
      ],
			"waist_interest_codes" : [
        "Dogs",
        "Cats",
        "Swimming"
      ],
			"time_range" : {
        "start" : 1,
        "end" : 99999999999
      }
		}
	}
}
```

___Example HTTP API Response___

```json
{
  "success": true,
  "data": {
    "results": {
      "platform_item_ids": [
        "23842904153620653",
        "23842967793430522",
        "23842980085660521",
        "23842995874860656",
      ],
      "n_total": "Unknown",
      "n_paginated": 50,
      "next_pagination_id": 4
    },
    "errors": [
      {
        "type" : "time_range_entry",
        "details" : "Please specify both a 'start' and 'end' for your time range."
      }
    ],
    "time_taken": 4.25278115272522,
    "presigned_urls": {
      "23842904153620653": "https://some_url",
      "23842967793430522": "https://some_url",
      "23842980085660521": "https://some_url",
      "23842995874860656": "https://some_url",
    }
  }
}
```



### Determining All WAIST Interest Codes That Can Be Queried

As part of submitting queries to the API, you may wish to filter by WAIST interest codes. As with platform items, the WAIST interest codes can also be retrieved by the API:

| __Input__                | __Description__                                              | __Datatype__ |
| ------------------------ | ------------------------------------------------------------ | ------------ |
| `action `                | To call the WAIST interest codes function, specify the `waist_interest_codes` action. | 🆂            |
| `data` ↣ `session_token` | The session token retrieved from the authentication, which enables the indexation of the WAIST interest codes. | 🆂            |

Once the request payload has been sent, the response will return WAIST interest codes that can be used to query platform items:

| __Input__              | __Description__                                              | Datatype  |
| ---------------------- | ------------------------------------------------------------ | --------- |
| `waist_interest_codes` | The list of WAIST interest codes that can be used to query platform items. | [ 🆂 ... ] |

___Example HTTP API Request___

```json
{
  "action" : "waist_interest_codes",
  "data" : {
    "session_token" : "aa97406a-1529-4a56-9d84-47e93bc3bf65"
  }
}
```

___Example HTTP API Response___

```json
{
  "waist_interest_codes": [
    "Aardvark",
    "ABC",
    "Apples",
    ...
  ]
}
```



### Retrieving The Associated Images Of Platform Items

As platform items retrieved from the API are given in JSON format, it is necessary to separately obtain media (i.e., images and video files). For this purpose, the media retrieval function can be used:

| Input                    | Description                                                  | Datatype  |
| ------------------------ | ------------------------------------------------------------ | --------- |
| `action`                 | To call the media retrieval function, specify the `retrieve_media` action. | 🆂         |
| `data` ↣ `media`         | The list of media files for which the corresponding URLs are to be obtained | [ 🆂 ... ] |
| `data` ↣ `session_token` | The session token retrieved from authentication, which enables the query. | 🆂         |

Once the request payload has been sent, the response will return the URLs that can be used to download the associated media:

| Output           | Description                                                  | Datatype  |
| ---------------- | ------------------------------------------------------------ | --------- |
| `success`        | Whether or not the media retrieval request was successful.   | 🅱         |
| `presigned_urls` | The session token that should be retained for further usage. | [ 🅾 ... ] |

___Example HTTP API Request___

```json
{
  "action" : "retrieve_media",
  "data" : {
    "media" : [
      "100024082_305631337903425_8036143955644900122_n.jpg"
    ],
    "session_token" : "aa97406a-1529-4a56-9d84-47e93bc3bf65"
  }
}
```

___Example HTTP API Response___

```json
{
  "success" : true,
  "presigned_urls": [
    { "100024082_305631337903425_8036143955644900122_n.jpg" : "https://some_url" }
  ]
}
```



### Further Questions

If you require any further assistance using this API, feel free to contact Abdul Obeid at obei@qut.edu.au