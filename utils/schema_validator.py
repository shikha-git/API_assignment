import json
import os
from jsonschema import validate, ValidationError

def load_schema(schema_file):
    base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "schemas")
    schema_path = os.path.join(base_path, schema_file)

    with open(schema_path, "r", encoding="utf-8") as f:
        user_schema = json.load(f)
    return user_schema

def assert_json_schema(data, schema):
    user_schema = load_schema(schema)

    try:
        validate(instance=data, schema=user_schema)
        print("✅ JSON response matches schema!")
    except ValidationError as e:
        print("❌ Schema validation error:", e.message)