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

## File Structure

```
C:\USERS\SURAJ\DOWNLOADS\EYESPY\EYESPY

    architecture_diagram.md
    
+---backend

        app.py
        cloud_setup.py
        database.py
        database_extension.py
        dataset_loader.py
        docker_setup.bat
        fake_news_model.ipynb
        model.jb
        modelrun.py
        requirements.txt
        run_server.bat
        run_with_mongodb.bat
        setup_database.py
        vectorizer.jb
        
+---Datasets

        Fake.csv
        True_news.csv
        
+---frontend
        index.html
        serve.py
        test.html
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
