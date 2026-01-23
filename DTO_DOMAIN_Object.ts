interface ProductDto {
    id: number;
    name: string;
    price: number;
}

class Product {
    private id: number;
    private name: string;
    private price: number;

    constructor(id: number, name: string, price: number) {
        if (id < 0) throw new Error("Invalid input found.")
        if (price < 0) throw new Error("Invalid input found.")
        this.id = id;
        this.name = name;
        this.price = price;
    }

    applyDiscount(percent: number): void {
        if (percent < 0 || percent > 100) {
            return
        } else {
            const percentage_marks = (this.price * (percent/100))
            this.price -= percentage_marks
        }
    }

    getPrice(): number {
        return this.price
    }
}

function createProductFromDto(dto: ProductDto) {
    const created = new Product(dto.id, dto.name, dto.price);
    return created
}
