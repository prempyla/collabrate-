class TemperatureSensor {
  private temperature: number;
  private alertThreshold: number;

  constructor(temperature: number) {
    if (temperature < -50 || temperature > 150) {
      throw new Error("Temperature out of range");
    }
    this.temperature = temperature;
    this.alertThreshold = 0; 
  }

  setAlertThreshold(threshold: number): void {
    if (threshold < -50 || threshold > 150) {
      throw new Error("Temperature out of range");
    }
    this.alertThreshold = threshold;
  }

  increaseTemperature(delta: number): void {
    const newTemperature = this.temperature + delta;

    if (newTemperature < -50 || newTemperature > 150) {
      throw new Error("Temperature out of range");
    }

    this.temperature = newTemperature;

    if (this.temperature > this.alertThreshold) {
      console.log("Alert! Temperature exceeds threshold");
    }
  }

  readTemperature(): number {
    return this.temperature;
  }
}
