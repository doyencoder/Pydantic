# Pydantic Tutorials

Small, focused examples that showcase [Pydantic v2](https://docs.pydantic.dev/latest/) features: field constraints, custom validators, model-level checks, computed fields, nested models, and serialization helpers.

## Contents
- [computed_field.py](computed_field.py): computes BMI with `computed_field`, shows derived fields without storing them.
- [field_validator.py](field_validator.py): validates email domain, normalizes names, and enforces age limits with `field_validator`.
- [model_validator.py](model_validator.py): uses `model_validator` to require emergency contacts for patients over a certain age.
- [nested_model.py](nested_model.py): demonstrates nested models by embedding an address inside a patient record.
- [pydantic_validator.py](pydantic_validator.py): illustrates field constraints, optional URL fields, and strict numeric validation.
- [serialization.py](serialization.py): highlights `model_dump` options, default handling, and selective serialization of fields.

## Setup
1) Create a virtual environment: `python -m venv .venv`
2) Activate it (PowerShell): `.venv\\Scripts\\activate`
3) Install dependencies: `pip install -r requirements.txt` ([requirements.txt](requirements.txt))

## Run Examples
- `python field_validator.py`
- `python computed_field.py`
- `python model_validator.py`
- `python nested_model.py`
- `python pydantic_validator.py`
- `python serialization.py`

## Extend
- Add pytest cases covering success and failure paths.
- Wrap the scripts into reusable functions or a small CLI.
- Include docstrings and richer type hints for helper functions.
- Demonstrate `model_dump_json` with include/exclude variations.
