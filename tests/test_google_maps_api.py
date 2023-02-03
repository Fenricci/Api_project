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

        print("Метод GET for Post request")
        result_get: requests.Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_post, 200)

        print("Метод PUT")
        result_put = requests.Response = GoogleMapsApi.update_new_place(place_id)
        Checking.check_status_code(result_post, 200)

        print("Метод GET for Put request")
        result_get: requests.Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_post, 200)

        print("Метод DELETE")
        result_delete: requests.Response = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_post, 200)

        print("Метод GET for Delete request")
        result_get: requests.Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_post, 404)
