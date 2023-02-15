from fastapi import FastAPI

app = FastAPI(openapi_url="/api/v1/city_name/openapi.json", docs_url="/api/v1/city_name/docs")


@app.get("/city-to-zipcode/{city_name}")
async def city_to_zipcode(city_name: str):
    # sample zip code 
    zip_code = "12345"
    return {"city_name": city_name, "zip_code": zip_code}
