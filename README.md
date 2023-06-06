# TruchiRrana
## Project Description
TruchiRrana is a Frog shaped robot that facilitates communication between hearing and deaf people.

The main idea behind TruchiRrana is to serve as a bidirectional intermediary for communication between hearing and deaf people, even if they are not in the same room. This is achieved through the frog-like form and behavior of the robot, which moves by jumping.

For example, in a household where there are hearing parents and a deaf child, they can use TruchiRrana to communicate. The parents can speak into the application incorporated in a phone the frog carries and it will jump to the child's room, displaying the message in sign language (which is the language the child understands). Conversely, the child can respond by using sign language, which the camera on the robot's phone will capture and process, resulting in audio that the parents can hear.

TruchiRrana provides a unique solution for facilitating communication between hearing and deaf individuals in a convenient and accessible way. This project aims to provide a useful tool for improving communication and reducing barriers for the deaf community.
## Demo
![Video Demo](https://vimeo.com/833401522?share=copy)
## Table of Contents
 + [Components](#Components)
 + [Hardware Scheme](#Hardware-Scheme)
 + [Software Architecture](#Software-Architecture)
 + [Amazing Contributions](#Amazing-Contributions)
 + [Authors](#Authors)
## Components
List of the hardware components used in the project:
+ x2 [VEX robotics 2-wire motor](https://www.cosues.com/vex-v5-motor-393-de-2-cables). 45.96€
+ [7.2V VEX robotics battery](https://www.cosues.com/vex-v5-bateria-nimh-de-7-2v-y-3000mah). 47.18€
+ [Raspoberry Pi 4](https://www.electan.com/raspberrypi4-p-10264.html). 59.75€
+ [Arduino UNO](https://www.electan.com/arduinouno-p-2977.html). 22.75€
+ [HC-SR04 Ultrasonic Sonar Distance Sensor](https://www.electan.com/sensor-distancia-por-ultrasonidos-hcsr04-p-6275.html). 2.13€
+ [three-axis magnetic field module](https://solectroshop.com/es/compas-magnetometro/456-brujula-digital-gy-271-5883-compas-magnetometro-hcm5883l.html). 3.32€
+ Mobile phone
## Hardware Scheme
![[Module diagram](https://github.com/OriolMarion/TruchiRrana/images/Captura.PNG)](https://github.com/OriolMarion/TruchiRrana/blob/main/images/hardware_scheme.jpeg)
## Software Architecture
![[Module diagram](https://github.com/OriolMarion/TruchiRrana/images/Captura.PNG)](https://github.com/OriolMarion/TruchiRrana/blob/main/images/module_diagram.PNG)
### Inputs
There are three types of input, all operating through the android application Speech To Sign, designed and programmed to enhance the interactivity of this robot. The first input is the microphone, used to record voice. The second input is the camera, used to capture signs made by people. And finally, there is the input used to select the origin and destination of the robot's path.
### Cloud
In the cloud, we have implemented several functionalities to alleviate the stress on the robot's hardware. On one hand, we perform voice input translation to text, which is subsequently translated into a language chosen by the user on their phone. All of this is accomplished through the utilization of Google API's SpeechToText and Translation services. The resulting text is then converted into images representing the signs corresponding to each letter in the text.
On the other hand, by utilizing the camera's input, images are transmitted to a server virtual machine hosted in the cloud. This virtual machine contains code programmed with advanced computer vision techniques to identify the signs depicted in the images. Through this process, we can extract text from the identified signs. By employing the TextToSpeech API, we can convert this text into audio for playback.
### Movement
To enable autonomous movement for the robot, the first step involves creating an image of the room's floor plan. Subsequently, the user can overlay the image with drawn walls and obstacles that the robot needs to navigate around. Additionally, the starting and ending points on the floor plan must be selected. Finally, a pathfinding algorithm is employed to calculate the optimal movement path for the robot.
## Amazing Contributions
### Jump
We have built a robot that has the ability to jump. This mechanism is complex to understand and we have been able to adapt it to our needs. We have shown that, even with a low budget, a skip mechanism can be implemented.
### Social relevance
TruchiRrana makes a contribution of social relevance since the fact of communicating with people who speak a minority language such as Sign Language is no longer an impediment. Also, encourage the intention to learn this language through games.
### All terrain
Being a robot that jumps, this allows it to cross physical barriers that a classic robot with wheels would have difficulty overcoming.
### Versatility
It can be used in different areas to facilitate the inclusion of people with hearing disabilities. From a doctor's visit to going to class, the frog can make communication more enjoyable. In addition, the learning mode makes it a useful tool for people who live together.
## Authors
 + Itziar Beltrán Simón
 + Martí Capel Ruiz
 + Oriol Marión Escudé
 + Serena Sánchez Garcia
