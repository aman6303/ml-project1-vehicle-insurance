# Vehicle Insurance Prediction

An end to end machine learning project for predicting vehicle insurance claims using an automated ML pipeline with data validation, transformation, model training, and AWS cloud deployment capabilities.

## Features

- **Automated Data Pipeline**: Ingestion → Validation → Transformation → Model Training
- **Data Validation**: Schema-based validation with detailed YAML reports
- **Feature Engineering**: Automated data transformation and feature generation
- **Model Training**: Multiple model training with evaluation metrics
- **Cloud Integration**: AWS S3 storage and MongoDB data management
- **Web Interface**: FastAPI-based web application for predictions
- **Docker Support**: Containerized deployment
- **Prediction Pipeline**: Real-time prediction service

## Project Structure

```
├── src/
│   ├── components/          # ML pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   └── model_pusher.py
│   ├── pipline/            # Training and prediction pipelines
│   ├── entity/             # Configuration and artifact entities
│   ├── configuration/      # AWS and MongoDB connections
│   ├── cloud_storage/      # AWS S3 integration
│   ├── constants/          # all constants value used in this project
│   ├── data_access/        # Database access layer
│   ├── logger/             # Logging utilities
│   ├── exception/          # Custom exceptions
│   └── utils/              # Helper utilities
├── config/
│   └── schema.yaml         # Data schema configuration
├── templates/              # FastAPI (frontend) HTML templates
├── static/                 # CSS and JavaScript files
├── artifact/               # Pipeline artifacts and outputs
├── notebook/               # Jupyter notebooks for exploration
├── app.py                  # FastAPI web application
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Installation

### Prerequisites
- Python 3.8+
- MongoDB (for data storage)
- AWS Account (for S3, ECR storage and EC2 instance)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/aman6303/ml-project1-vehicle-insurance-prediction.git
cd ml-project1-vehicle-insurance-prediction
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
# Create .env file with:
AWS_ACCESS_KEY_ID=<your-key>
AWS_SECRET_ACCESS_KEY=<your-secret>
MONGODB_URL=<your-mongodb-url>
```

## Usage

### Running the Web Application

```bash
python app.py
```
Navigate to `http://localhost:5000` in your browser.

### Training the Model

```python
from src.pipline.training_pipeline import TrainingPipeline

pipeline = TrainingPipeline()
pipeline.run_pipeline()
```

### Making Predictions

```python
from src.pipline.prediction_pipeline import PredictionPipeline

pipeline = PredictionPipeline()
predictions = pipeline.predict(data)
```

## Configuration

Edit `config/schema.yaml` to define:
- Feature names and types
- Data validation rules
- Feature transformations
- Model parameters

## Docker Deployment

Build and run the Docker container:

```bash
docker build -t vehicle-insurance-ml .
docker run -p 5000:5000 vehicle-insurance-ml
```

## Pipeline Components

### Data Ingestion
- Loads raw data from configured source
- Splits into train/test sets
- Stores in feature store

### Data Validation
- Validates data against schema
- Detects missing values and outliers
- Generates validation reports (YAML)

### Data Transformation
- Feature scaling and normalization
- Categorical encoding
- Feature engineering
- Outputs transformed NumPy arrays

### Model Training
- Trains multiple algorithms
- Hyperparameter tuning
- Cross-validation
- Model evaluation and selection

### Model Evaluation
- Performance metrics
- Error analysis
- Comparison with baseline

### Model Pusher
- Saves best model to S3
- Version management
- Deployment packaging

## Technologies Used

- **ML Framework**: scikit-learn
- **Data Processing**: pandas, numpy
- **Web Framework**: Flask
- **Database**: MongoDB
- **Cloud Storage**: AWS S3
- **Containerization**: Docker
- **Logging**: Python logging module

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Submit a Pull Request

## License

This project is licensed under the LICENSE file - see the [LICENSE](LICENSE) file for details.


## Acknowledgments

- Data sourced from vehicle insurance datasets
- Built with automated ML pipeline architecture
- Inspired by industry best practices in MLOps