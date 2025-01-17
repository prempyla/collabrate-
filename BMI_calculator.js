
// Your code here
let BMI=weight/(height*height);
console.log("Your BMI is",BMI.toFixed(2))
if (BMI<18.5) {
    console.log("Health Category: Underweight")
} else if (18.5<=BMI && BMI<24.9) {
    console.log("Health Category: Normal weight")
} else if (25<=BMI && BMI<29.9) {
    console.log("Health Category: Overweight")
} else {
    console.log("Health Category: Obesity")
}
