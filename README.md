# Raspberry Pi 4 Facial Recognition
This is the code I wrote/edited for my computer science IA. The goal of this project is to use a raspberry pi to automatically scan students' faces and keep a running record of the names of the students entering the classroom on time, tardy and absent. Ultimately, sending the list of students to the teacher for attendance. The faces used in this project are not real students due to the violation of GDPR, therefore, this [kaggle celebrity face dataset](https://www.kaggle.com/hereisburak/pins-face-recognition) is used. 

## How to Use It
1. Clone this repo onto your local machine(raspberry pi)
2. cd into the directory where the code is located
3. Install necessary python packages with the following code
```bash
conda env create -f environment.yml
```
4. Modify the email sender, receiver, and the time the model is running
5. Run main.py

[Here](https://drive.google.com/file/d/19n9mDA6z-8FbnIklpfJ3xLX_XINBU29d/view?usp=sharing) is a link to my writings and code formatted as IB requested.
