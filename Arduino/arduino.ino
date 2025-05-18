const int pines[8] = {2, 3, 4, 5, 6, 7 ,8, 9};     
int i;

void setup() {
  Serial.begin(9600);  // Inicia comunicación serial
  for (i = 0; i <= 7; i++) {
    pinMode(pines[i], INPUT);
  }
}

void loop() {
  String binario = "";
  
  for (i = 0; i <= 7; i++) {
    int valore = digitalRead(pines[i]);
    binario += String(valore);
  }

  // Obtenemos el tiempo desde que Arduino fue encendido
  unsigned long tiempo = millis();

  // Enviar una sola línea con binario y timestamp separados por coma
  Serial.print(binario);
  Serial.print(",");
  Serial.println(tiempo);

  delay(100);  // Espera para evitar saturación
}
