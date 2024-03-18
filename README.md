## Face Physiognomy

An AI-Powered technology that analyzes facial expressions from static images as well as video feed in order to reveal information about the subject’s emotional state. It is a hybrid model which follows of two steps. The first step is detecting faces from the given image using the Haar Cascades object detector. The second step uses a Deep Convolutional Neural Network (DCNN) to extract features from the face for the purpose of classifying the emotion of the subject as happy, sad, angry, neutral or surprised.

*Please give a star if you like the project.*

- [Dataset](#dataset)
- [Quick Start](#quick-start)
- [Docker Usage](#docker-usage)
- [Results](#results)
- [Repository Structure](#repository-structure)
- [Contributing] (#contributing)
- [License] (#license)
- [References](#references)

---
### Dataset
The dataset used to train the model: https://www.kaggle.com/datasets/msambare/fer2013

<br>

### Quick Start
- Create a virtual environment following the steps provided [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- All the requirements can be installed by running `pip3 install -r requirements.txt`
- Running the command `python3 app.py` would locally start the website

<br>

### Docker Usage
To use the application via docker
- ```docker pull shrenikjainn9/face-physiognomy:latest```
- ```docker run -p 5000:5000 shrenikjainn9/face-physiognomy:latest```

<br>

### Results
Upon running `app.py`, the results are as shown below. (Refer `./static/created_images/`)

<p align="center">
  <img src="https://github.com/shrenik-jain/face-physiognomy/blob/main/static/assets/images/website.png" width="850px" height="400px"/></p>
 <br>
 <br>
<p align="center">
  <img src="https://github.com/shrenik-jain/face-physiognomy/blob/main/static/assets/images/upload_image.png" width="640px" height="480px"/></p>

<br>

### Repository Structure
```
├── app.py
├── Dockerfile
├── Jenkinsfile
│
├── model_config
│   ├── model.json
│   └── model_weights.h5
│
├── notebooks
│   ├── Model_Training.ipynb
│   └── model_training.py
│
├── Procfile
│
├── static
│   ├── assets
│   │   ├── css
│   │   ├── fonts
│   │   ├── images
│   │   └── js
│   │
│   └── created_images
│
├── templates
│   ├── image_upload.html
│   └── index.html
│
└── utils
    ├── camera.py
    └── model.py
```

<br>

### Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. For major changes, it's recommended to discuss them first by opening an issue.

To contribute to this project:
1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with descriptive commit messages
4. Push your changes to your forked repository
5. Submit a pull request to the main repository

Please ensure that your code follows the project's coding style and that you have added relevant tests and documentation.

<br>

### License
This project is licensed under the MIT License.

<br>

### References
- **Templates**
    - [Bootstrap](https://getbootstrap.com)
    - [Templatemo Breezed](https://templatemo.com/tm-543-breezed)

- **Fonts & Icons**
    - [Google Fonts](https://fonts.google.com/)
    - [Font Awesome](https://fontawesome.com/)

<br>

Developed by [*Shrenik Jain*](https://shrenik-jain.github.io/)
