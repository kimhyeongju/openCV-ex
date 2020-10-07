#include "motor.h"

Motor::Motor(int in1, int in2, int en) : in1(in1), in2(in2), end(en){
    pinMode(in1, OUTPUT);
    pinMode(in2, OUTPUT);
    pinMode(en, OUTPUT);
}

void Motor::forward(int speed=200){

}

void Motor::backward(int speed=200){

}

void Motor::stop(){

}

void Motor::setSpeed(int speed){
    
}