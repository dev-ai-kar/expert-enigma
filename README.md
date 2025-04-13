# Expert Enigma


```mermaid
graph TD
    User[User] -->|Draws or Uploads Digit| Frontend[Frontend (React)]
    Frontend -->|Processes Drawing as Image| Backend[Backend (Django)]
    Backend -->|Processes Image and Classifies Digit| Backend
    Backend -->|Sends Classification Result| Frontend
    Frontend -->|Displays Result| User
```

Expert Enigma is a web-based application designed to process and analyze handwritten digits. It leverages a machine learning model to recognize and classify digit images uploaded by users.

## Project Structure

This repository contains the **backend** of the application, which is built using Django. The backend handles image processing, model inference, and API endpoints for communication with the frontend.

### Backend Features
- Processes uploaded images and prepares them for model inference.
- Utilizes a pre-trained Convolutional Neural Network (CNN) model for digit recognition.
- Provides API endpoints for the frontend to interact with the backend.

## Frontend Repository

The **frontend** for this project is located at [Sketch-Frontend](https://github.com/dev-ai-kar/Sketch-Frontend). The frontend is a React application that provides a user-friendly interface for drawing any digit, processing it as an image, and viewing results.

Please visit the [Sketch-Frontend](https://github.com/dev-ai-kar/Sketch-Frontend) repository for the frontend code and setup instructions.

## How It Works

1. **User Interaction**: Users draw any handwritten digit or upload images through the React-based frontend interface.
2. **Image Processing**: The frontend processes the drawing as an image and sends it to the backend.
3. **Model Inference**: The backend processes the image, resizes it to the required dimensions, converts it to grayscale, and passes it to the CNN model for digit classification.
4. **Result Display**: The backend sends the classification result back to the frontend, where it is displayed to the user.

## Setup Instructions

### Backend Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/dev-ai-kar/expert-enigma.git
   cd expert-enigma
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Django server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
Follow the setup instructions in the [Sketch-Frontend](https://github.com/dev-ai-kar/Sketch-Frontend) repository.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
