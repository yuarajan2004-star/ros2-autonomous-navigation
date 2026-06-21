# AutoNav Coding Standards

## Python Style

* Follow PEP8
* Maximum line length: 100 characters
* Use descriptive variable names
* Avoid hardcoded values

## ROS2 Nodes

Every node should contain:

* Node description
* Parameter definitions
* Logging messages
* Error handling

## Logging

Use:

```python
from autonav_utils import AutoNavLogger
```

Instead of:

```python
print("message")
```

## Parameters

Store all configurable values in YAML files.

Do not hardcode:

* frequencies
* frame names
* planner settings
* controller settings

## Testing

Every new feature must include:

* Unit tests
* Integration tests

before merging.
