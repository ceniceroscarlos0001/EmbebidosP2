const int pines[8] = {2, 3, 4, 5, 6, 7 ,8, 9};     
int i;

void setup() {
  Serial.begin(9600);
  for (i = 0; i <= 7; i++) {
    pinMode(pines[i], INPUT_PULLUP);  // entradas con pull-up interno activado
  }
}

void loop() {
  String binario = "";

  for (i = 0; i <= 7; i++) {
    int valore = !digitalRead(pines[i]);  // invertimos porque pull-up da HIGH por defecto
    binario += String(valore);
  }

  unsigned long tiempo = millis();
  Serial.print(binario);
  Serial.print(",");
  Serial.println(tiempo);

  delay(100);
}
