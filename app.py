from typing import Annotated

from fastapi import Depends, FastAPI, Form, Request
from fastapi.concurrency import run_in_threadpool
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from uvicorn import run as app_run

# Importing constants and pipeline modules from the project
from src.constants import APP_HOST, APP_PORT
from src.pipline.prediction_pipeline import VehicleData, VehicleDataClassifier
from src.pipline.training_pipeline import TrainPipeline

# --- Setup & Configuration ---
app = FastAPI(title="Vehicle Insurance Prediction App")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Pydantic Models ---
class VehicleInputSchema(BaseModel):
    """
    Pydantic model to validate and type-cast incoming form data automatically.
    """

    Gender: str
    Age: int
    Driving_License: int
    Region_Code: float
    Previously_Insured: int
    Annual_Premium: float
    Policy_Sales_Channel: float
    Vintage: int
    Vehicle_Age_lt_1_Year: int
    Vehicle_Age_gt_2_Years: int
    Vehicle_Damage_Yes: int

    @classmethod
    def as_form(
        cls,
        Gender: str = Form(...),
        Age: int = Form(...),
        Driving_License: int = Form(...),
        Region_Code: float = Form(...),
        Previously_Insured: int = Form(...),
        Annual_Premium: float = Form(...),
        Policy_Sales_Channel: float = Form(...),
        Vintage: int = Form(...),
        Vehicle_Age_lt_1_Year: int = Form(...),
        Vehicle_Age_gt_2_Years: int = Form(...),
        Vehicle_Damage_Yes: int = Form(...),
    ):
        """
        Dependency helper to construct the model from Form data.
        """
        return cls(
            Gender=Gender,
            Age=Age,
            Driving_License=Driving_License,
            Region_Code=Region_Code,
            Previously_Insured=Previously_Insured,
            Annual_Premium=Annual_Premium,
            Policy_Sales_Channel=Policy_Sales_Channel,
            Vintage=Vintage,
            Vehicle_Age_lt_1_Year=Vehicle_Age_lt_1_Year,
            Vehicle_Age_gt_2_Years=Vehicle_Age_gt_2_Years,
            Vehicle_Damage_Yes=Vehicle_Damage_Yes,
        )


# --- Routes ---


@app.get("/", tags=["UI"])
async def index(request: Request):
    # This renders the Form (index.html)
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/train", tags=["ML Operations"])
async def train_route_client():
    """
    Triggers model training.
    Uses run_in_threadpool to ensure the heavy training logic
    doesn't block the async event loop.
    """
    try:
        train_pipeline = TrainPipeline()
        # prevent blocking the server during training
        await run_in_threadpool(train_pipeline.run_pipeline)
        return Response("Training successful!!!")
    except Exception as e:
        return Response(f"Error Occurred! {str(e)}", status_code=500)


@app.post("/", tags=["ML Operations"])
async def predict_route_client(
    request: Request,
    form_data: Annotated[VehicleInputSchema, Depends(VehicleInputSchema.as_form)],
):
    try:
        # ... (Your existing prediction logic remains the same) ...
        vehicle_data = VehicleData(**form_data.model_dump())
        vehicle_df = vehicle_data.get_vehicle_input_data_frame()
        model_predictor = VehicleDataClassifier()
        value = await run_in_threadpool(model_predictor.predict, dataframe=vehicle_df)

        status = "Response-Yes" if value[0] == 1 else "Response-No"

        # CHANGE HERE: Render "result.html" instead of "index.html"
        return templates.TemplateResponse(
            "result.html", {"request": request, "context": status}
        )

    except Exception as e:
        return templates.TemplateResponse(
            "result.html", {"request": request, "context": f"Error: {e}"}
        )


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)
