from requests import Response


class Assertions:
    @staticmethod
    # TODO create assertions

    def assert_json_contents_fields(response: Response, fields):
        parsed_response = response.json()
        for key in fields:
            assert key in parsed_response, f'Field {key} is not in json'





       # assert keys in parsed_response, f'Field {keys} is not in {values} json'
