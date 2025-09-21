# EyeSpy - AI-Powered Fake News Detection

A cutting-edge multimodal system for detecting fake news and manipulated content using artificial intelligence.

## Features

- **Text Analysis**: Advanced NLP algorithms detect linguistic patterns and misinformation indicators.
- **Image Forensics**: (Coming Soon) Computer vision techniques to identify digital manipulation and deepfakes.
- **Real-time Processing**: Lightning-fast analysis with confidence scores.
- **Modern UI**: Sleek, responsive frontend with dark theme.

## How to Run

### Prerequisites

- Docker
- Python 3

### Instructions

1.  **Start the backend and database:**

    Open a terminal and run the following command from the `EyeSpy/backend` directory:

    ```bash
    ./docker_setup.bat
    ```

    This will start a MongoDB container, set up the database, and run the Flask backend server.

2.  **Start the frontend:**

    Open another terminal and run the following command from the `EyeSpy/frontend` directory:

    ```bash
    python serve.py
    ```

    This will start a simple Python web server for the frontend.

3.  **Access the application:**

    Open your web browser and go to `http://localhost:8080`.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND LAYER                          │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐    ┌─────────────────┐                    │
│  │   Text Input    │    │  Image Upload   │                    │
│  │   Text Area     │    │   File Input    │                    │
│  └─────────────────┘    └─────────────────┘                    │
│           │                       │                             │
│           └───────────┬───────────┘                             │
│                       │                                         │
│              ┌─────────────────┐                               │
│              │ JavaScript API  │                               │
│              │   fetch() calls │                               │
│              └─────────────────┘                               │
└─────────────────────────┼───────────────────────────────────────┘
                          │ HTTP/REST API
                          │ (JSON/FormData)
┌─────────────────────────▼───────────────────────────────────────┐
│                    APPLICATION LAYER                           │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                 Flask Routes                                │ │
│  │  POST /api/predict                                          │ │
│  │  GET  /api/health                                          │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────┬───────────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────────┐
│                    BUSINESS LOGIC LAYER                       │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │              FakeNewsDetector Class                         │ │
│  │                                                             │ │
│  │  ┌─────────────────┐  ┌─────────────────┐                  │ │
│  │  │  Text Analysis  │  │ Image Analysis  │                  │ │
│  │  │     Engine      │  │     Engine      │                  │ │
│  │  └─────────────────┘  └─────────────────┘                  │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────┬───────────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────────┐
│                    DATA/MODEL LAYER                           │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────┐  │
│  │  TF-IDF         │    │  Logistic       │    │  MongoDB    │  │
│  │  Vectorizer     │    │  Regression     │    │  Database   │  │
│  │  (vectorizer.jb)│    │  (model.jb)     │    │             │  │
│  └─────────────────┘    └─────────────────┘    └─────────────┘  │
└─────────────────────────────────────────────────────────────────┘

```

## Dependencies

- Flask
- Flask-CORS
- numpy
- scikit-learn
- joblib
- Pillow
- pymongo
- pandas
- gunicorn

All Python dependencies are listed in `backend/requirements.txt`.

## License

MIT License - Feel free to use and modify for your projects.
