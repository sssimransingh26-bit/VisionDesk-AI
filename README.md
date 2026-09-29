# PPE Detection using YOLOv8

An AI-based **Personal Protective Equipment (PPE) Detection System** for construction-site safety. The project uses **YOLOv8** to detect PPE and identify missing safety equipment from construction-site images.

## Overview

The system analyzes construction-site images using a custom-trained YOLOv8 model and detects PPE such as helmets, gloves, vests, boots, and goggles.

A **Streamlit web application** is used to run the trained model and visualize detection results.

## Workflow

```text
Construction-Site Image
        ↓
      YOLOv8
        ↓
     best.pt
        ↓
   PPE Detection
        ↓
PPE Status & Violations
```

## Features

* Custom-trained YOLOv8 model
* PPE and safety-violation detection
* Detects missing PPE
* Bounding boxes and confidence scores
* Streamlit-based interface

## PPE Classes

**Helmet, Gloves, Vest, Boots, Goggles, None, Person, No Helmet, No Goggles, No Gloves, No Boots**

## Tech Stack

**Python, YOLOv8, Ultralytics, OpenCV, Pillow, NumPy, Streamlit**

## Project Structure

```text
PPE-Detection-yolov8/
├── app.py              # Streamlit application
├── best.pt             # Trained YOLOv8 model
├── .gitignore
└── README.md
```

## Installation

```bash
git clone https://github.com/sssimransingh26-bit/PPE-Detection-yolov8.git
cd PPE-Detection-yolov8
python -m venv venv
venv\Scripts\activate
pip install ultralytics streamlit pillow numpy opencv-python
```

## Run

```bash
python -m streamlit run app.py
```

Upload a construction-site image through the Streamlit interface to perform PPE detection.

## Model

`best.pt` is the custom-trained YOLOv8 model used for PPE detection.

## Future Improvements

Real-time video detection, CCTV integration, automated safety alerts, detection history, and integration with a safety-policy knowledge base.

## Project Context

Developed as part of an **Infosys training/project workflow**, this project represents the **Visual Intelligence / PPE Detection stage** of a larger construction-site safety compliance system.

