class Order {
    itemName: string
    price: number 
    isPaid: boolean 
    status: string 
    constructor(item: string){
        this.itemName = item
        this.price = 0
        this.isPaid = false
        this.status = 'CREATED'
    }
}

class OrderService {
    createOrder(itemName: string): Order {
        const order = new Order(itemName)
        order.status = 'ORDERED'
        return order
    }
}

class PricingService {
    calculate(order: Order): Order {
        let count = 0
        for(let item of order.itemName){
            count += item.charCodeAt(0)
        }
        order.price = count
        order.status = "PRICED"
        return order
    }
}

class PaymentService {
    pay(order: Order): Order{
        order.isPaid = true
        order.status = 'PAID'
        return order
    }
}
class KitchenService {
    prepare(order: Order): Order{
        order.status =  "PREPARED"
        return order
    }
}

class NotificationService {
    send(order: Order): string{
        return `Order Confirmed: ${order.itemName} | Price: ${order.price} | Status: ${order.status}`
    }
}

class PizzaShop {
    private orderService = new OrderService()
    private pricingService = new PricingService()
    private paymentService = new PaymentService()
    private kitchenService = new KitchenService()
    private notificationService = new NotificationService()

  processOrder(itemName: string): Order {
    let order = this.orderService.createOrder(itemName)
    order = this.pricingService.calculate(order)
    order = this.paymentService.pay(order)
    order = this.kitchenService.prepare(order)

    console.log(this.notificationService.send(order))

    return order;
  }
}
