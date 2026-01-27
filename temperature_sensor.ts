class TemperatureSensor {
  private temperature: number;

  constructor(temperature: number) {
    this.setTemperature(temperature);
  }

  readTemperature(): number{
    return this.temperature;
  }
  setTemperature(temp: number): void{
    if (temp < -50 || temp > 150) {
        throw new Error("Temperature out of realistic range");
    }
    this.temperature = temp
  }
  increaseTemperature(delta: number): void{
    this.setTemperature(this.temperature+delta)
  }
}
