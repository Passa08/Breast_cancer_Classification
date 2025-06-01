# Breast Cancer Classification Project

A web-based application for breast cancer classification using deep learning. This project uses Django for the web interface and a trained deep learning model for cancer detection.

## Features

- Modern, user-friendly web interface
- Real-time breast cancer classification
- High accuracy predictions
- Easy-to-use upload functionality
- Detailed results visualization

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Passa08/Breast_cancer_Classification.git
cd Breast_cancer_Classification
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Model File Setup

⚠️ **Important**: The model file (`my_model.keras`) is not included in this repository due to size limitations.

To get the model file:
1. Download it from [insert your chosen storage location]
2. Place it in the `cancer_detection` directory
3. Ensure the file is named `my_model.keras`

## Running the Application

1. Ensure you have downloaded and placed the model file as described above
2. Navigate to the project directory:
```bash
cd cancer_detection
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

5. Open your browser and visit: `http://localhost:8000`

## Usage

1. Navigate to the detection page
2. Upload a mammogram image
3. Click "Analyze"
4. View the classification results

## Project Structure

```
cancer_detection/
├── cancer_project/    # Django project settings
├── main/             # Main application
├── predictor/        # Cancer prediction logic
├── static/          # Static files (CSS, images)
└── templates/       # HTML templates
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your chosen license]

## Contact

[Add your contact information] 