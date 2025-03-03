import pickle
import json
import re
from typing import List, Tuple, Any

import streamlit as st

# Load the config file,
configuration_file = r"app_configuration.json"

with open(configuration_file, 'r') as file:
    config = json.load(file)

# Directly assign each key to a variable
status_options = config["status_options"]
item_type_options = config["item_type_options"]
country_options = config["country_options"]
application_options = config["application_options"]
product = config["product"]

# Artifacts from dictionary.
price_artifacts = config["price_artifacts"]
status_artifacts = config["status_artifacts"]


@st.cache_data
def load_model_artifacts(artifacts_dict: dict):
    """
    Loads model artifacts (model, scaler, and transformer) using pickle. Returns the
    data in order else raises the errors.
    :param artifacts_dict: Dictionary containing paths to model, scaler, and transformer.
    :return: A tuple containing the model, scaler, and transformer.
    :raises: KeyError if any required key is missing.
    :raises: FileNotFoundError if any file is not found.
    :raises: pickle.PickleError if there is an error unpickling any file.
    :raises: Exception for any other unexpected errors.
    """
    def _load_artifact(file_path):
        f_data = open(file_path, 'rb')
        pickle_output = pickle.load(f_data)
        f_data.close()
        return pickle_output

    return_pack = []
    try:
        for item in artifacts_dict:
            return_pack.append(_load_artifact(artifacts_dict[item]))
        return tuple(return_pack)

    except KeyError as e:
        print(f"Missing required key in artifacts dictionary: {e}")
        raise
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        raise
    except pickle.PickleError as e:
        print(f"Error unpickling file: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error loading model artifacts: {e}")
        raise


def pattern_validation(inputs: List[str]) -> Tuple[bool, Any]:
    """
    Pattern validation function for checking if all inputs are numbers.
    Non-capturing group of "one or more digits" or "floating point numbers".

    :param inputs: List of strings to validate.
    :return: Tuple containing a boolean indicating success or failure, and the invalid item if any.
    """
    pattern_string = r"^(?:\d+|\d*\.\d+)$"
    for item in inputs:
        if not re.match(pattern_string, item):
            return False, item
    return True, None


def input_validation(button: bool, var_list: List[str]) -> bool:
    """
    Validates the pattern of the input variables.

    :param button: Boolean indicating if the validation should proceed.
    :param var_list: List of variables to check.
    :return: True if all inputs are valid, otherwise False.
    """
    valid_result, invalid_item = pattern_validation(var_list)

    if button and not valid_result:
        if not invalid_item:
            st.write("## :red[❌ Please enter a valid number, space is not allowed.]")
        else:
            st.write(f"## :red[❌ You have entered an invalid value: {invalid_item}]")
        return False

    return valid_result if button else False
