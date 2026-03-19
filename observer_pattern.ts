interface Observer {
  name: string;
  update(temp: number): void;
}

interface Subject {
  attach(observer: Observer): void;
  detach(observer: Observer): void;
  notify(): void;
}

class DisplayObserver implements Observer {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
  update(temp: number): void {
    console.log("DISPLAY " + this.name + ": " + temp);
  }
}

class AlertObserver implements Observer {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
  update(temp: number): void {
    if (temp > 50) console.log("ALERT " + this.name + ": HIGH");
  }
}

class LoggerObserver implements Observer {
  name: string;
  private logs: number[] = [];
  constructor(name: string) {
    this.name = name;
  }
  update(temp: number): void {
    this.logs.push(temp);
  }
  getLogs(): number[] {
    return this.logs;
  }
}

class TemperatureSensor implements Subject {
  private observers: Observer[] = [];
  private temperature: number = 0;

  attach(observer: Observer): void {
    this.observers.push(observer)
  }

  detach(observer: Observer): void {
    this.observers = this.observers.filter(ele => ele.name !== observer.name)
  }

  notify(): void {
    this.observers.forEach(app => app.update(this.temperature))
  }

  setTemperature(temp: number): void {
    this.temperature = temp;
    this.notify();
  }
}
