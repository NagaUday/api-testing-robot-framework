import requests
import logging
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

class CustomerKeywords:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    @keyword("Customer Login")
    def customer_login(self, smid):
        url = "https://ucr.bypass.api/login"
        payload = {
            "smid": smid,
            "technical_user": "bnppf-tech-user"
        }
        headers = {
            "Content-Type": "application/json"
        }

        try:
            logging.info(f"Sending login request for SMID: {smid}")
            response = requests.post(url, json=payload, headers=headers)

            if response.status_code != 200:
                logging.error(f"Failed: {response.status_code} - {response.text}")
                raise Exception("Login API failed")

            token = response.json().get("login_token")
            if not token:
                raise Exception("Login token not found in response")

            BuiltIn().set_global_variable("${TOKEN}", token)
            BuiltIn().set_global_variable("${TOKEN_STATUS}", "SUCCESS")
            logging.info("Token successfully retrieved.")

        except Exception as e:
            logging.exception("Exception occurred during customer login")
            BuiltIn().set_global_variable("${TOKEN_STATUS}", "FAILURE")
            raise e