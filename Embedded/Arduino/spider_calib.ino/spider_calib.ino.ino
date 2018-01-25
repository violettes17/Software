/*
 * RedOhm
 * 
 * 
 * Positionne un servomoteur à son centre 
 *              donc à 90°
 *              
 * Le 06/12/2016
 * H.Mazelin              
 */
 
 
// Cette librairie permet à une carte Arduino de contrôler des servomoteurs
#include <Servo.h>
 
// Crée un objet de type "Servo", nommé -> monservo
Servo monservo;
 
// le bouton est connecté à la broche 2 de la carte Arduino
const int bouton=2;
// Variable qui enregistre l'état du bouton
int etatdubouton;
 
/* 
 * Un programme Arduino doit impérativement contenir cette fonction .
 * Elle ne sera exécuter une seule fois au démarrage du microcontroleur
 * Elle sert à configurer globalement les entrées sorties  
 *  
 */
 
 
 
void setup() {
 
 
//le bouton est une entrée
 // pinMode(bouton,INPUT);
//on initialise l'état du bouton comme "relaché"
  etatdubouton=LOW;
  
}
 
/*
 *Le programme principal s’exécute par une boucle infinie appelée Loop () 
 * 
 */
 
 
void loop() {
 
// lecture de l'etat du bouton
// etatdubouton=digitalRead(bouton);
 
//test si le bouton a un niveau logique HAUT
//if (etatdubouton == HIGH)
//{
// associe le servomoteur a la broche 3  
   monservo.attach(3);
// Positionne mon servomteur a 90
   //monservo.write(30);
   delay(1000);
   //monservo.write(90);
   delay(1000);
   monservo.write(150);
   delay(1000);
   
// Réalise une pause dans l'exécution du programme pour une durée 
// de 20 millisecondes
// permettant au servomteur d'atteindre sa position  
   delay(20);
//}
 
//else 
//{
 
// Dissocie la variable monservo de sa broche   
// monservo.detach();
 
//}
 
 
  
 
}
