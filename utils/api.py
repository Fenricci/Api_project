from utils .http_methods import HTTPMethods

base_url = "https://rahulshettyacademy.com/"
key = "?key=qaclick123"

class GoogleMapsApi():
    '''Метод для создания новой локации'''
    @staticmethod
    def create_new_place():
        json_body_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "maps/api/place/add/json" # Ресурс для метода post
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HTTPMethods.post(post_url, json_body_for_create_new_place)
        print(result_post.text)
        return result_post

    '''Метод для проверки новой локации'''
    @staticmethod
    def get_new_place(place_id):

        get_resource = "/maps/api/get/json"  # Ресурс метода GET
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = HTTPMethods.get(get_url)
        print(result_get.text)
        return result_get