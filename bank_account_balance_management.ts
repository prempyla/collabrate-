class BankAccount {
  // write your code here
  private balance: number;
  private transactions: string[] = [];

  constructor(balance: number) {
    if (balance < 0) throw new Error("Initial balance cannot be negative");
    this.balance = balance;
    this.transactions = [];
  }

  deposit(amount: number): void {
    if (amount <= 0) throw new Error("Deposit amount must be positive");
    this.balance += amount;
    this.transactions.push(`Deposited ${amount}`);
  }

  withdraw(amount: number): void {
    if (amount <= 0) throw new Error("Withdrawal amount must be positive")
    if (amount > this.balance) throw new Error("Insufficient balance")
    this.balance -= amount;
    this.transactions.push(`Withdrew ${amount}`);
  }

  getBalance(): number{
    return this.balance;
  }
  getTransactionHistory(): string[] {
    return [...this.transactions]
  }
}
