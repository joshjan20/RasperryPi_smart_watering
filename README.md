# Plant Watering System Using Raspberry Pi and Arduino

This project involves building a smart plant watering system using a combination of a **Raspberry Pi**, **Arduino Uno**, and various sensors to monitor soil moisture, temperature, and lighting conditions of houseplants. The system notifies the user via a connected app whether the plant needs watering, offering remote control and automation through **Google Firebase**.

---

## Components Used:

- **Raspberry Pi**
- **Arduino Uno**
- **DHT11 Temperature and Humidity Module (1 piece)**
- **Photoresistor (1 piece)** - For light detection
- **Soil Moisture Sensor (1 piece)** - To measure soil moisture levels
- **NPN Transistor (PN2222, 1 piece)**
- **Diode Rectifier (1 piece)**
- **LEDs (2 pieces)**
- **Resistors (4 pieces)**
- **Fan Blade and 3-6V Motor (1 piece)**
- **Breadboard** - For connecting components
- **Jumper Wires**
- **PL app and Google Firebase access** - For controlling the watering system remotely

---


## Project Overview:

This smart plant watering system is designed to help monitor the soil moisture of your plants and notify you if watering is required. It is particularly helpful for users who may forget to water their plants or for those who want to remotely manage their plants through cloud-based controls.

- **Moisture Sensor**: The soil sensor monitors the moisture levels in the plant pot. If the soil moisture falls below a pre-set threshold, the system will send a notification through Google Firebase, indicating that the plant needs watering.
  
- **Temperature and Humidity**: The DHT11 sensor measures the temperature and humidity of the environment, providing additional data for plant care.

- **Lighting Conditions**: The photoresistor detects light levels, which can be critical for plants requiring specific light conditions.

---

## Key Features:

- **Automated Monitoring**: The system constantly monitors soil moisture, temperature, and light levels, ensuring your plant receives optimal care.
  
- **Firebase Integration**: The status of your plants is monitored in real-time via **Google Firebase**, allowing users to remotely check on plant health and control the watering system via a connected app.
  
- **Remote Control**: The system can be controlled remotely, allowing users to activate or deactivate watering from anywhere.

---

## How It Works:

1. **Moisture and Temperature Sensing**: The soil moisture sensor and DHT11 module constantly check the condition of the plant. When the soil moisture falls below a certain threshold, the system sends a notification via Firebase, informing the user that watering is needed.

2. **Light Monitoring**: The photoresistor checks the lighting conditions, ensuring the plant is in a suitable light environment.

3. **Automation**: Depending on the moisture level, the Raspberry Pi triggers the watering system to automatically water the plant, or the user can manually control the watering through the Firebase interface.

4. **Notifications**: The system sends updates about the plant's environment to the Firebase database, which can be accessed through a mobile app or web interface.

---

## Applications:

- **Home Automation**: Ideal for people who may forget to water their plants or travel frequently.
- **Gardening at Scale**: With expansion, the system can be scaled for use in gardens or greenhouses.

---

## References:

For additional guides and tutorials on connecting Arduino and Raspberry Pi to Firebase, visit the following resources:

1. [Arduino Temperature Sensor Guide](https://www.tutorialspoint.com/arduino/arduino_temperature_sensor.htm)
2. [Send Data to Firebase using Raspberry Pi](https://tutorial.cytron.io/2020/12/09/send-data-to-firebase-using-raspberry-pi/)
3. [Connecting Arduino to Firebase](https://www.instructables.com/Connecting-Arduino-to-Firebase-to-Send-Receive-Dat/)

---

This project serves as a great starting point for creating a fully automated smart watering system using basic IoT principles.