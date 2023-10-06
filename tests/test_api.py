# This file lists down all the tests for Reqres API. 
# The tests are written using pytest framework.

import http

from lib.schema import (
    ListResourceResponse,
    ResourceMetadata,
    SuccessfulLoginResponse,
    SuccessfulRegistrationResponse,
)


def test_register_successful(httpx_client, test_assets_payloads, test_response):
    """This tests if we are able to successfully register a user"""
    # We need to extract payload from the JSON input file
    data = test_assets_payloads.get("register_successful", None)
    assert data is not None

    # We need to make a POST request to the API.
    response = httpx_client.post("/api/register", json=data)

    # Any test validations go down here
    assert response.status_code == http.HTTPStatus.OK
    
    # We need to validate the response schema.
    # We have pre-defined schemas in lib/schema.py
    # We can use the schemas to validate the response.
    # When we initialize the Pydantic model, it validates the data.
    # In this case, it validates if the response data matches the schema.
    # As a part of the validation, it checks if the field id is present and is of type
    #  int.
    # It also checks if the field token is present and is of type str.
    # If the validation fails, it raises a ValidationError.
    actual = SuccessfulRegistrationResponse.model_validate(response.json())
    expected = SuccessfulRegistrationResponse.model_validate(test_response.get
                                                ("register_successful_response", None))
    assert actual == expected
    


def test_login_successful(httpx_client, test_assets_payloads, test_response):
    """This tests if we are able to successfully Login a user"""
    # We need to extract payload from the JSON input file
    data = test_assets_payloads.get("login_successful", None)
    assert data is not None

    # We need to make a POST request to the API.
    response = httpx_client.post("/api/login", json=data)

    assert response.status_code == http.HTTPStatus.OK
    # We need to validate the response schema.
    # We have pre-defined schemas in lib/schema.py
    # We can use the schemas to validate the response.
    # When we initialize the Pydantic model, it validates the data.
    # In this case, it validates if the response data matches the schema.
    # As a part of the validation, it checks if the field token is present and
    #  is of type str.
    # If the validation fails, it raises a ValidationError.
    actual = SuccessfulLoginResponse.model_validate(response.json())
    expected = SuccessfulLoginResponse.model_validate(test_response.get
                                            ("login_successful_response", None))
    assert actual == expected


def test_list_resource(httpx_client, test_response):
    """This test is to check if the response contains a valid resources"""
    # We need to make a GET request to the API.
    response = httpx_client.get("/api/unknown")
    assert response.status_code == http.HTTPStatus.OK

    # We need to validate the response schema.
    # We have pre-defined schemas in lib/schema.py
    # We can use the schemas to validate the response.
    # When we initialize the Pydantic model, it validates the data.
    # In this case, it validates if the response data matches the schema.
    parsed_response = ListResourceResponse.model_validate(response.json())
    expected = ResourceMetadata.model_validate(test_response.get
                                            ("test_resource_meta_response", None))
    
    # We would like to check if the response contains a valid resource.
    assert expected in parsed_response.data


