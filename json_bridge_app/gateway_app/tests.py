import http
import json
from django.test import TestCase

from gateway_app.constants import CONSTANTS


class GatewayTests(TestCase):
    def test_http_gateway_valid_json_post(self):
        data = {CONSTANTS["test_case_key"]: CONSTANTS["test_case_value"]}
        response = self.client.post("/api/ui/", json.dumps(data),
                                    content_type="application/json")

        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertEqual(response.json(), {"message": data})

    def test_http_gateway_valid_big_json_post(self):
        data = [{f'{CONSTANTS["test_case_key"]}{index}':
                f'{CONSTANTS["test_case_value"]}{index}'} for index in range(1, 10000)]

        response = self.client.post("/api/ui/", json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertEqual(response.json(), {"message": data})

    def test_http_gateway_invalid_json_post(self):
        response = self.client.post("/api/ui/", "invalid_json", content_type="application/json")
        self.assertEqual(response.status_code, http.HTTPStatus.BAD_REQUEST)
        self.assertEqual(response.json(), {"error": CONSTANTS["json_error"]})

    def test_http_gateway_method_not_allowed_get(self):
        response = self.client.get("/api/ui/")
        self.assertEqual(response.status_code, http.HTTPStatus.METHOD_NOT_ALLOWED)
        self.assertEqual(response.json(), {"message": CONSTANTS["invalid_method"]})

    def test_http_gateway_method_not_allowed_put(self):
        response = self.client.put("/api/ui/")
        self.assertEqual(response.status_code, http.HTTPStatus.METHOD_NOT_ALLOWED)
        self.assertEqual(response.json(), {"message": CONSTANTS["invalid_method"]})

    def test_http_gateway_method_not_allowed_delete(self):
        response = self.client.delete("/api/ui/")
        self.assertEqual(response.status_code, http.HTTPStatus.METHOD_NOT_ALLOWED)
        self.assertEqual(response.json(), {"message": CONSTANTS["invalid_method"]})

    def test_http_gateway_method_not_allowed_patch(self):
        response = self.client.patch("/api/ui/")
        self.assertEqual(response.status_code, http.HTTPStatus.METHOD_NOT_ALLOWED)
        self.assertEqual(response.json(), {"message": CONSTANTS["invalid_method"]})

    def test_http_gateway_method_not_allowed_options(self):
        response = self.client.options("/api/ui/")
        self.assertEqual(response.status_code, http.HTTPStatus.METHOD_NOT_ALLOWED)
        self.assertEqual(response.json(), {"message": CONSTANTS["invalid_method"]})

# python manage.py test gateway_app.tests
