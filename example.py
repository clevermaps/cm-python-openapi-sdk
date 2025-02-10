from openapi_client.models.view_dto import ViewDTO

with open("./data/view_example.json", "r") as file:
    json_data = file.read()

view_dto_instance = ViewDTO.from_json(json_data)

print(view_dto_instance)