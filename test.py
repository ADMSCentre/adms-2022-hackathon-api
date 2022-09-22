import json
import requests

'''
	The Australian Ad Observatory API endpoint
'''
api_endpoint_url = 'https://i7dy5tidoi.execute-api.us-east-2.amazonaws.com/default/fta-dashboard-instance'

'''
	This function executes the API request, and returns the result
'''
def dashboard_API_request(request_payload, api_endpoint_url=api_endpoint_url):
	return json.loads(requests.post(api_endpoint_url, 
		data=bytes(json.dumps(request_payload), encoding='utf-8')).content.decode('utf-8'))

'''
	Retrieve the session token
'''
session_token_payload = dashboard_API_request({
		"action" : "authenticate",
		"data" : {
			"username" : "<YOUR USERNAME>",
			"password" : "<YOUR PASSWORD>"
		}
	})
session_token = session_token_payload["session_token"]

'''
	Retrieve all the available WAIST interest codes
'''
waist_interest_codes_payload = dashboard_API_request({
		"action" : "waist_interest_codes",
		"data" : {
			"session_token" : session_token
		}
	})
print(json.dumps(waist_interest_codes_payload,indent=3))

'''
	Search for platform items about 'Dogs'
'''
platform_items_payload = dashboard_API_request({
		"action" : "platform_items",
		"data" : {
			"session_token" : session_token,
			"query" : {
				"remove_missing_entries": True,
				"pagination_id" : 0,
				"filters" : {
					"waist_interest_codes" : [
						"Dogs"
					]
				}
			}
		}
	})
first_platform_item = list(platform_items_payload["data"]["presigned_urls"].values())[0]

'''
	Load up the first platform item in the results
'''
platform_item_json = json.loads(requests.get(first_platform_item).content)
image_fname = platform_item_json["media"]["image_urls"][0]
print(json.dumps(platform_item_json,indent=3))

'''
	Load up the corresponding image URL for the platform item
'''
retrieve_media_payload = dashboard_API_request({
	"action" : "retrieve_media",
		"data" : {
			"media" : [
				image_fname
			],
			"session_token" : session_token
		}
	})
associated_image_url = retrieve_media_payload["presigned_urls"][image_fname]

'''
	Save the image to file
'''
img_data = requests.get(associated_image_url).content
with open(image_fname, 'wb') as handler:
	handler.write(img_data)























