
// Your code here
for (let i=0; i<inputArr.length; i++) {
    if (inputArr[i]>0) {
        console.log("The number is positive.")
    } else if (inputArr[i]<0) {
        console.log("The number is negative.")
    } else if (inputArr[i]===0) {
        console.log("The number is zero.")
    } else {
        console.log("The element is not an integer.")
    }
}
