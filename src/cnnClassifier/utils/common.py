import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.
    Args:
        path_to_yaml (Path): Path to the yaml file.
    Returns:
        ConfigBox: ConfigBox object containing the yaml data.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
        return ConfigBox(yaml_data)
    except Exception as e:
        logger.error(f"Error reading yaml file: {e}")
        raise BoxValueError(f"Error reading yaml file: {e}")

@ensure_annotations
def save_json(path: Path, data: Any) -> None:
    """
    Saves data to a json file.
    Args:
        path (Path): Path to the json file.
        data (Any): Data to be saved.
    Returns:
        None
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        logger.info(f"Data saved to {path}")
    except Exception as e:
        logger.error(f"Error saving data to json file: {e}")
        raise BoxValueError(f"Error saving data to json file: {e}")
    
@ensure_annotations
def load_json(path: Path) -> Any:
    """
    Loads data from a json file.
    Args:
        path (Path): Path to the json file.
    Returns:
        Any: Data loaded from the json file.
    """
    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
        logger.info(f"Data loaded from {path}")
        return data
    except Exception as e:
        logger.error(f"Error loading data from json file: {e}")
        raise BoxValueError(f"Error loading data from json file: {e}")

@ensure_annotations
def save_bin(path: Path, data: Any) -> None:
    """
    Saves data to a binary file using joblib.
    Args:
        path (Path): Path to the binary file.
        data (Any): Data to be saved.
    Returns:
        None
    """
    try:
        joblib.dump(data, path)
        logger.info(f"Data saved to {path}")
    except Exception as e:
        logger.error(f"Error saving data to binary file: {e}")
        raise BoxValueError(f"Error saving data to binary file: {e}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.
    Args:
        path (Path): Path to the binary file.
    Returns:
        Any: Data loaded from the binary file.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Data loaded from {path}")
        return data
    except Exception as e:
        logger.error(f"Error loading data from binary file: {e}")
        raise BoxValueError(f"Error loading data from binary file: {e}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Gets the size of a file in a human-readable format.
    Args:
        path (Path): Path to the file.
    Returns:
        str: Size of the file in a human-readable format.
    """
    try:
        size_in_bytes = os.path.getsize(path)
        size_in_kb = size_in_bytes / 1024
        size_in_mb = size_in_kb / 1024
        if size_in_mb >= 1:
            return f"{size_in_mb:.2f} MB"
        elif size_in_kb >= 1:
            return f"{size_in_kb:.2f} KB"
        else:
            return f"{size_in_bytes} bytes"
    except Exception as e:
        logger.error(f"Error getting size of file: {e}")
        raise BoxValueError(f"Error getting size of file: {e}")

@ensure_annotations
def encode_image_to_base64(image_path: Path) -> str:
    """
    Encodes an image to a base64 string.
    Args:
        image_path (Path): Path to the image file.
    Returns:
        str: Base64 encoded string of the image.
    """
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        logger.info(f"Image at {image_path} encoded to base64")
        return encoded_string
    except Exception as e:
        logger.error(f"Error encoding image to base64: {e}")
        raise BoxValueError(f"Error encoding image to base64: {e}")

@ensure_annotations
def decode_image(encoded_string: str, output_path: Path) -> None:
    """
    Decodes a base64 string back to an image and saves it to the specified path.
    Args:
        encoded_string (str): Base64 encoded string of the image.
        output_path (Path): Path where the decoded image will be saved.
    Returns:
        None
    """
    try:
        with open(output_path, "wb") as image_file:
            image_file.write(base64.b64decode(encoded_string))
        logger.info(f"Base64 string decoded and saved as image at {output_path}")
    except Exception as e:
        logger.error(f"Error decoding base64 string to image: {e}")
        raise BoxValueError(f"Error decoding base64 string to image: {e}")

@ensure_annotations
def create_directory(path: Path):
    """
    Creates a directory if it does not exist.
    Args:
        path (Path): Path to the directory.
    Returns:
        None
    """
    try:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory created at {path}")
    except Exception as e:
        logger.error(f"Error creating directory: {e}")
        raise BoxValueError(f"Error creating directory: {e}")
    
@ensure_annotations
def get_folder_size(path: Path) -> str:
    """
    Gets the size of a folder in a human-readable format.
    Args:
        path (Path): Path to the folder.
    Returns:
        str: Size of the folder in a human-readable format.
    """
    try:
        total_size = 0
        root = Path(path)
        if not root.is_dir():
            raise NotADirectoryError(str(path))
        total_bytes = sum(
        f.stat().st_size
        for f in root.rglob("*")
            if f.is_file() and not f.is_symlink()
            )
        size_in_kb = total_bytes / 1024
        size_in_mb = size_in_kb / 1024
        if size_in_mb >= 1:
            return f"{size_in_mb:.2f} MB"
        elif size_in_kb >= 1:
            return f"{size_in_kb:.2f} KB"
        else:
            return f"{total_bytes} bytes"
    except Exception as e:
        logger.error(f"Error getting size of folder: {e}")
        raise BoxValueError(f"Error getting size of folder: {e}")