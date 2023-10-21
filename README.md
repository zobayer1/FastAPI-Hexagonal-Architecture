FastAPI Hexagoonal Architecture Demo
====================================

This is a FastAPI demo application implementing the Hexagonal Architecture.

Breakdown
---------

The `services` module holds our domain implementations. We expose various interfaces (implemented using abstract classes) as ports that can be used by the adapters from the driving and driven modules.

In this example, the path operation endpoint function `save_data` acts as the driving adapter and the concrete subclass `MemoryDataPort` of port abstruct class `MyDataPort` acts as the driven adapter.

Path operation method `save_data` invokes the save method from the concrete implementation class `MyServiceImpl`. A dependency on the driven class `MemoryDataport` is injected from the path operation function to the domain business logic implementation using FastAPI's `Depends` mechanism.

The difference between a 3-tier architecture and hexagonal architecture is that, the adapter `MemoryDataPort` implements interfaces from the domain's port instead of the domain logic implementing an interface from a lower level.


Installation
------------

Create a Python 3.11 virtual environment and install dependencies from the requirements file.

```sh
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run Server
----------

Run Uvicorn server

```sh
uvicorn app.main:app --reload
```

Visit [http://localhost:8000/?data=true]() and tweak the parameter `data`.

Run Tests
---------

To run the tests, simply run pytest.

```sh
pytest -s
```

References
----------

- Read more about [hexagonal architecture](https://netflixtechblog.com/ready-for-changes-with-hexagonal-architecture-b315ec967749).
- A short video on [Hexagonal, onion, and clean architecture](https://www.youtube.com/watch?v=JubdZIdLQ4M)
- Domain driven design: [Hexagonal architecture](https://vaadin.com/blog/ddd-part-3-domain-driven-design-and-the-hexagonal-architecture)
- More [examples using python](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html)
