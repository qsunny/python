"""
https://tortoise.github.io/examples/basic.html
This example demonstrates most basic operations with single model
pip install tortoise-orm[asyncmy]
"""


from tortoise import Tortoise, fields, run_async
from tortoise.models import Model


class Event(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField(description="Name of the event that corresponds to an action")
    datetime = fields.DatetimeField(null=True, description="Datetime of when the event was generated")

    class Meta:
        table = "t_event"
        table_description = "This table contains a list of all the example events"

    def __str__(self):
        return self.name


async def run() -> None:
    await Tortoise.init(db_url="mysql://root:password@47.115.0.1:3308/temp_test", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas(safe=True)

    event = await Event.create(name="Test")
    await Event.filter(id=event.id).update(name="Updated name")

    print(await Event.filter(name="Updated name").first())
    # >>> Updated name

    await Event(name="Test 2").save()
    print(await Event.all().values_list("id", flat=True))
    # >>> [1, 2]
    print(await Event.all().values("id", "name"))
    # >>> [{'id': 1, 'name': 'Updated name'}, {'id': 2, 'name': 'Test 2'}]


if __name__ == "__main__":
    run_async(run())




