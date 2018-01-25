


// Cette librairie permet à une carte Arduino de contrôler des servomoteurs
#include <Servo.h>
 
// Crée un objet de type "Servo", nommé -> monservo
#define PAVD  0
#define PAVG -30
#define PARG 20
#define PARD -10
#define EAVD  0
#define EAVG 0
#define EARG 0
#define EARD 0

Servo monservo;
Servo patte_avant_droit;
Servo patte_avant_gauche;
Servo patte_arriere_droit;
Servo patte_arriere_gauche;
Servo epaule_avant_droit;
Servo epaule_avant_gauche;
Servo epaule_arriere_droit;
Servo epaule_arriere_gauche;

 


#include <SoftwareSerial.h>


#include <Grove_I2C_Motor_Driver.h>
#define LED 2 //connect LED to digital pin2 

// default I2C address is 0x0f
#define I2C_ADDRESS 0x0f

 int up ;  // elevation
 int i;   //toggle
int  coup_d_epaule ;   // amplitude du mouvement vers l'avant de l'épaule
int  leve_patte ;    // amplitude de levée de la patte, genre french cancan



void setup() {

   init_debout_assis();
   init_avance();
	
	// initialize the digital pin2 as an output.
  //pinMode(LED, OUTPUT);     

 Motor.begin(I2C_ADDRESS, F_31372Hz);
 
// associe les servomoteurs aux membres du herisson
   //monservo.attach(3);
   // en accrochant les servos en tournant en sens inverse des aiguilles au dessus du herisson
   patte_avant_droit.attach(3);
   patte_avant_gauche.attach(4);
   patte_arriere_gauche.attach(5);
   patte_arriere_droit.attach(6);
   
   epaule_avant_droit.attach(7);
   epaule_avant_gauche.attach(8);
   epaule_arriere_gauche.attach(9);
   epaule_arriere_droit.attach(10);
   
   
}

void loop() { 
                digitalWrite(LED, HIGH);   // set the LED on
                //remontée de la vrille
                //Motor.StepperRun(50*7);
                //delay(1000);               // for 500ms
                digitalWrite(LED, LOW);   // set the LED off
                //descente de la vrille
                //Motor.StepperRun(-50*7);
                //delay(1000);
    //debout_assis();
    avance( patte_avant_droit, epaule_avant_droit);
    delay(500);
    avance( patte_arriere_droit, epaule_arriere_droit);
    delay(500);
    poussee( patte_avant_droit, epaule_avant_droit);
    delay(500);
    poussee( patte_arriere_droit, epaule_arriere_droit);
    delay(500);
    avance( patte_avant_gauche, epaule_avant_gauche);
    delay(500);
    avance( patte_arriere_gauche, epaule_arriere_gauche);
    delay(500);
    poussee( patte_avant_gauche, epaule_avant_gauche);
    delay(500);
    poussee( patte_arriere_gauche, epaule_arriere_gauche);
    delay(500);
 
// Dissocie la variable monservo de sa broche   
// monservo.detach();




}


void init_debout_assis()
{
    up = -2;
    i=0;
  }

void debout_assis()
{
                 if (i<11) {
                i=i+1;
               } else
               {
                i=0;
               }

   patte_avant_droit.write(60+i*up+PAVD); // la patte a 30° pour toucher le corps, à 150° patte étirée vers l'exterieur
   patte_avant_gauche.write(60+i*up+PAVG); // la patte a 30° pour toucher le corps, à 150° patte étirée vers l'exterieur
   patte_arriere_gauche.write(60+i*up+PARG); // la patte a 30° pour toucher le corps, à 150° patte étirée vers l'exterieur
   patte_arriere_droit.write(60+i*up+PARD); // la patte a 30° pour toucher le corps, à 150° patte étirée vers l'exterieur
   
   epaule_avant_droit.write(90+EAVD);  // epaule a 90° centre hexagone
   epaule_avant_gauche.attach(90+EAVG);  // epaule a 90° centre hexagone
   epaule_arriere_gauche.attach(90+EARG);  // epaule a 90° centre hexagone
   epaule_arriere_droit.attach(90+EARD);  // epaule a 90° centre hexagone
   
  }

void init_avance()
{
  coup_d_epaule = 30;
  leve_patte = 30;
}

 
void avance( Servo my_patte, Servo my_epaule)
{
  
   my_patte.write(60+leve_patte+PAVD); // la patte a 30° pour toucher le corps, à 150° patte étirée vers l'exterieur
   delay(300);
   my_epaule.write(90+coup_d_epaule+EAVD);  // epaule a 90° centre hexagone
   delay(300);
   my_patte.write(60+PAVD); // la patte a 30° pour toucher le corps, à 150° patte étirée vers l'exterieur
   delay(300);
  }
  
void poussee( Servo my_patte, Servo my_epaule)    // remettre l'épaule à sa position d'origine
{
   my_epaule.write(90+EAVD);  // epaule a 90° centre hexagone
   delay(300);
 
  }


// End of file


/* origin 1 */

/*
 * steppermotor_test.ino
 * Example sketch for Grove - I2C Motor Driver v1.3
 *
 * Copyright (c) 2012 seeed technology inc.
 * Website    : www.seeed.cc
 * Author     : Jerry Yip
 * Create Time: 2017-02
 * Change Log :
 *
 * The MIT License (MIT)
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */



 /* origin 2 */

 /*
 * RedOhm
 * 
 * 
 * Positionne un servomoteur 
 *              
 * Le 06/12/2016
 * H.Mazelin              
 */
