from requests import Response


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, attr_name, expected_value):
        resp_as_dist = response.json()
        assert attr_name in resp_as_dist, f'Name {attr_name} not in response'
        assert resp_as_dist[attr_name] == expected_value, f'Wrong value. Expected value {expected_value}, ' \
                                                          f'actual {resp_as_dist[attr_name]}'

    @staticmethod
    def assert_json_contents_fields(response: Response, fields, values):
        parsed_response = response.json()
        for key in fields:
            assert key in parsed_response, f'Field {key} is not in json'
            for name in key:
                assert name == values, f'Expected {values}, actual {parsed_response[key]}'

    @staticmethod
    def assert_key(dict_to_check, key, error_message):
        assert key in dict_to_check, error_message

    @staticmethod
    def assert_key_is_not_in_response(response, key):
        assert key not in response, f'{key} is in response!'

       # assert keys in parsed_response, f'Field {keys} is not in {values} json'
