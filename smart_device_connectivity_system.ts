interface Connectable {
    connect(): void;
    disconnect(): void;
}

abstract class SmartDevice {
    id: string;

    constructor(id: string) {
        this.id = id;
    }

    info(): void {
        console.log(`Device ID: ${this.id}`);
    }
    abstract performAction(): void;
}

// SmartLight class
class SmartLight extends SmartDevice implements Connectable {
    connect(): void {
        console.log(`SmartLight connected`);
    }
    disconnect(): void {
        console.log(`SmartLight disconnected`);
    }
    performAction(): void {
        console.log(`Changing brightness`);
    }
}

// SmartLock class
class SmartLock extends SmartDevice implements Connectable {
    connect(): void {
        console.log("SmartLock connected");
    }
    disconnect(): void {
        console.log("SmartLock disconnected");
    }
    performAction(): void {
        console.log("Locking/Unlocking door");
    }
}
