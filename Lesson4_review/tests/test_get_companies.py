import random
import pytest
import requests
from data.credentional import AllData
from src.assertions import Assertions
from data.urls import BaseUrl


class TestGetCompanies:
    url = BaseUrl()
    assertions = Assertions()
    cred = AllData()
    urls = BaseUrl()

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.parametrize("status", cred.company_status)
    def test_get_companies_with_valid_status(self, status):
        url = f"api/companies?status={status}&limit=3&offset=0"
        response = requests.get(f"{self.urls.base_url}/{url}")
        self.assertions.assert_status_code(response, 200)

    @pytest.mark.smoke
    @pytest.mark.parametrize("status", cred.company_status)
    def test_get_companies_is_json(self, status):
        url = f"api/companies?status={status}&limit=3&offset=0"
        response = requests.get(f"{self.urls.base_url}/{url}")
        self.assertions.assert_response_is_json(response)

    @pytest.mark.smoke
    @pytest.mark.parametrize("status", cred.company_status)
    def test_get_companies_has_valid_keys(self, status):
        url = f"api/companies?status={status}&limit=3&offset=0"
        response = requests.get(f"{self.urls.base_url}/{url}")
        self.assertions.assert_json_has_keys(response, self.cred.names)

    def test_get_companies_with_invalid_status(self):
        status = self.cred.invalid_status
        url = f"api/companies?status={status}&limit=3&offset=0"
        response = requests.get(f"{self.urls.base_url}/{url}")
        self.assertions.assert_status_code(response, 422)

    @pytest.mark.regression
    @pytest.mark.parametrize("status", cred.company_status)
    def test_get_companies_with_valid_limit(self, status):
        url = f"api/companies?status={status}&limit={random.randint(1, 3)}&offset=0"
        response = requests.get(f"{self.urls.base_url}/{url}")
        self.assertions.assert_status_code(response, 200)

    @pytest.mark.regression
    @pytest.mark.parametrize("status", cred.company_status)
    def test_get_companies_with_valid_offset(self, status):
        url = f"api/companies?status={status}&limit=3&offset={random.randint(0, 3)}"
        response = requests.get(f"{self.urls.base_url}/{url}")
        self.assertions.assert_status_code(response, 200)
