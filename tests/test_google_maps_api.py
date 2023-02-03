import json

import requests
from utils.api import GoogleMapsApi
from utils.checking import Checking


class TestCreatePlace:

    def test_create_new_place(self):
        print("Метод POST")
        result_post: requests.Response = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        token = json.loads(result_post.text)
        print(list(token))

        print("Метод GET for Post request")
        result_get: requests.Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        print("Метод PUT")
        result_put = requests.Response = GoogleMapsApi.update_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ["msg"])

        print("Метод GET for Put request")
        result_get: requests.Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])

        print("Метод DELETE")
        result_delete: requests.Response = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ["status"])

        print("Метод GET for Delete request")
        result_get: requests.Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])

        