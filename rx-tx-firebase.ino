#include <ArduinoJson.h>

#include <FirebaseArduino.h>
/*
* * Copyright (C) 2018 GT Silicon Pvt Ltd
 *
 * Licensed under the Creative Commons Attribution 4.0
 * International Public License (the "CCBY4.0 License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * https://creativecommons.org/licenses/by/4.0/legalcode
 *
 *
* */

#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>

extern "C" {
#include "user_interface.h"
}


#define FIREBASE_HOST "oblu-iot-160658.firebaseio.com"
#define FIREBASE_AUTH "a7XqhoUO2cBTS68bSU7ywqBhPDp7WtFJNA1m6t1d"


const char* ssid = "iPhone"; //type your ssid (Router)
const char* password = "qwerty@2"; //type your password of the Router

void sys_init(); //Initialization of the system
int m = 0;

WiFiServer server(9876); // Server is bound to port number 9876
WiFiClient client;

void setup() {
  sys_init();
}

void loop() {
  delay(100);
  // Check if a client has connected
  client = server.available();
  if (!client) { // If not connected it will stay in the loop
    return;
  }
  


   while(client.connected()){
//    delay(10);
    while (client.available() > 0) {
      byte inByte = client.read(); // oblu reads from system/workstation
      Serial.write(inByte); // Oblu writes to the system
    }
    while (Serial.available() > 0) {
      size_t len = Serial.available();
      char buf[len];
      for(size_t i = 0; i < len; i++){
        buf[i] = Serial.read();
      }
      client.write(buf, len); // system writes to oblu via rxtx(UART)
      char num[4]; //unpacked data
      
      // Tried to implement uploading data to to Firebase, to unpack the data from Oblu.
      
      /*num[0]=buf[0];
      num[1]=buf[1];
      num[2]=buf[2];
      num[3]=buf[3];
      int l=4;
      float *f[14];
      int n=0;
      while(l<60){
        num[0]=buf[l+3];
        num[1]=buf[l+2];
        num[2]=buf[l+1];
        num[3]=buf[l];
        l=l+4;
        f[n++]=(float*)num;
      }
     Firebase.setFloat("R_dx",num[0]);
     Firebase.setFloat("R_dy",num[1]);
     Firebase.setFloat("R_dz",num[2]);
     Firebase.setFloat("R_angle",num[3]);
     Firebase.setString("message", "hello world");*/
    }

  }
    String name = Firebase.pushInt("logs", m++);
}
  

 void sys_init(){
  Serial.begin(115200);
  delay(10);
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  //WiFi.begin(ssid);
  WiFi.begin(ssid, password);
   
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
   
  // Start the server
  server.begin();
  Serial.println("Server started");
 
  // Print the IP address
  Serial.print("Local IP:");
  Serial.print(WiFi.localIP());
 }
