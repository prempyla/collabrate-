interface Notifier {
  notify(message: string): void;
}

class EmailNotifier implements Notifier{
    notify(message: string): void{
        console.log(`[EMAIL] ${message}`)
    }
}

class SMSNotifier implements Notifier{
    notify(message: string): void{
        console.log(`[SMS] ${message}`);
    }
}

class PushNotifier implements Notifier{
    notify(message: string): void{
        console.log(`[PUSH] ${message}`);
    }
}

function sendNotification(n: Notifier, msg: string) {
    n.notify(msg);
}
