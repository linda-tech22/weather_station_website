from django.http import JsonResponse
from ninja import Router, Schema, NinjaAPI
from pydantic import ConfigDict

from .model import TemperatureReading


api = NinjaAPI()


class TemperatureReadingSchema(Schema):
    temperature: float = 10.0



@api.post("/temperature")
def create_temperature_reading(request, temperature_data: TemperatureReadingSchema):
    reading = TemperatureReading(temperature=temperature_data.temperature)
    reading.save()
    return JsonResponse({"status": {temperature_data.temperature}})

@api.get("/show")
def show_temp(request , temp_data: TemperatureReadingSchema):
    data = temp_data.temperature
    return f"hello  {data}"


@api.get("/hello")
def hello(request, name = " world "):
    return f"hello  {name }"







