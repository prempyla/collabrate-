// TODO: Define PaymentStrategy interface
interface PaymentStrategy {
    validate(details: any): boolean;
    processPayment(amount: number, details: any): string;
    getStrategyName(): string;
}

// TODO: Implement CreditCardStrategy
class CreditCardStrategy implements PaymentStrategy {
    public readonly name = "CreditCard"
    details: any

    validate(details: {cardNumber: string, cvv: string, expiryDate: string}): boolean {
        if(details.cardNumber.length != 16 || details.cvv.length != 3) {
            return false
        }
        const [mm, yy] = details.expiryDate.split("/")
        if (!mm || !yy || mm.length != 2 || yy.length != 2) {
            return false
        } 
        return true
    }

    processPayment(amount: number, details: any): string {
        if (this.validate(details)) {
            return `Payment of $${amount.toFixed(2)} processed via Credit Card ending in ${details.cardNumber.slice(-4)}`
        } else {
            return "Invalid credit card details"
        }
    }

    getStrategyName(): string {
        return this.name
    }
}

// TODO: Implement PayPalStrategy
class PayPalStrategy implements PaymentStrategy {
    public readonly name = "PayPal"
    validate(details: {email: string, password: string}): boolean {
        if(!details.email.includes("@") || !details.email.includes(".") || details.password.length < 8 ) {
            return false
        } else {
            return true
        }
    }

    processPayment(amount: number, details: any) {
        if (this.validate(details)) {
            return `Payment of $${amount.toFixed(2)} processed via PayPal account ${details.email}`
        } else {
            return "Invalid PayPal credentials"
        }
    }

    getStrategyName() {
        return this.name
    }
}

// TODO: Implement BankTransferStrategy
class BankTransferStrategy implements PaymentStrategy {
    public readonly name = "BankTransfer"

    validate(details: {accountNumber: string, routingNumber: string, accountHolder: string}): boolean {
        if (details.accountNumber.length != 10 || details.routingNumber.length != 9 || !details.accountHolder.trim) {
            return false
        } else {
            return true
        }
    }

    processPayment(amount: number, details: any) {
        if (this.validate(details)) {
            return `Payment of $${amount.toFixed(2)} processed via Bank Transfer from account ${details.accountNumber}`
        } else {
            return "Invalid bank account details"
        }
    }

    getStrategyName() {
        return this.name
    }
}

// TODO: Implement PaymentService with strategy registry
class PaymentService {
    private strategies: { [key: string]: PaymentStrategy } = {};
    
    registerStrategy(strategy: PaymentStrategy): void {
        this.strategies[strategy.getStrategyName()] = strategy
    }
    
    processPayment(strategyName: string, amount: number, details: any): string {
        if (amount <= 0) {
            throw new Error("Error: Amount must be greater than zero")
        }
        if (!this.strategies[strategyName]) {
            throw new Error(`Error: Payment strategy ${strategyName} not found`)
        }
        const strategy = this.strategies[strategyName]
        return strategy.processPayment(amount, details)
    }
    
    listStrategies(): string {
        return Object.keys(this.strategies).join(",")
    }
}
