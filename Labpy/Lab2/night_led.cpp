const int BLED = 9;          // Blue LED on pin 9
const int GLED = 10;         // Green LED on pin 10
const int RLED = 11;         // Red LED on pin 11
const int TEMP = 0;          // Temp Sensor is on pin A0
const int LOWER_BOUND = 139; // Lower Thresholdconst
int UPPER_BOUND = 147;       // Upper Threshold
int val = 0;                 // Variable to hold analog reading

void setup()
{
    pinMode(BLED, OUTPUT); // Set Blue LED as Output
    pinMode(GLED, OUTPUT); // Set Green LED as Output
    pinMode(RLED, OUTPUT); // Set Red LED as Output
}

void loop()
{
    val = analogRead(TEMP);
    if (val < LOWER_BOUND)
    {
        digitalWrite(RLED, LOW);
        digitalWrite(GLED, LOW);
        digitalWrite(BLED, HIGH);
    }
    else if (val > UPPER_BOUND)
    {
        digitalWrite(RLED, HIGH);
        digitalWrite(GLED, LOW);
        digitalWrite(BLED, LOW);
    }
    else
    {
        digitalWrite(RLED, LOW);
        digitalWrite(GLED, HIGH);
    digitalWrite(BLED, LOW);
    }
}
