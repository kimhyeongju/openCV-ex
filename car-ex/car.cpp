#include "car.h"

Car::Car(int in1, int in2, int en1, int in3, int in4, int en2)
        :in1(in1), in2(in2), en1(en1),in3(in3),in4(in4),en2(en2){
        pinMode(in1, OUTPUT);
        pinMode(in2, OUTPUT);
        pinMode(en1, OUTPUT);
        pinMode(in3, OUTPUT);
        pinMode(in4, OUTPUT);
        pinMode(en2, OUTPUT);
    }


void forward(int speed;
void backward(int speed);
void turnLeft(int speed);   // r: forward, l: backward
void turnRight(int speed);  // r: backward, l: forward
void setSpeed(int rightSpeed, int leftSpeed);
void stop();