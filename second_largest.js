// a, b, c, d variables are already defined
// if (a>b>c>d) {
//     console.log("Second Largest Number:",b)
// } else if (a>b>d>c) {
//     console.log("Second Largest Number:",b)
// } else if (a>c>b>d) {
//     console.log("Second Largest Number:",c)
// } else if (a>c>d>b) {
//     console.log("Second Largest Number:",c)
// } else if (a>d>b>c) {
//     console.log("Second Largest Number:",d)
// } else if (a>d>c>b) {
//     console.log("Second Largest Number:",d)
// } else if (b>a>c>d) {
//     console.log("Second Largest Number:",a)
// } else if (b>a>d>c) {
//     console.log("Second Largest Number:",a)
// } else if (b>c>a>d) {
//     console.log("Second Largest Number:",c)
// }else if (b>c>d>a) {
//     console.log("Second Largest Number:",c)
// }else if (b>d>a>c) {
//     console.log("Second Largest Number:",d)
// }else if (b>d>c>a) {
//     console.log("Second Largest Number:",d)
// } else if (c>a>b>d) {
//     console.log("Second Largest Number:",a)
// } else if (c>a>d>b) {
//     console.log("Second Largest Number:",a)
// } else if (c>b>a>d) {
//     console.log("Second Largest Number:",c)
// }else if (c>b>d>a) {
//     console.log("Second Largest Number:",c)
// }else if (c>d>a>b) {
//     console.log("Second Largest Number:",d)
// }else if (c>d>b>a) {
//     console.log("Second Largest Number:",d)
// } else if (d>a>b>c) {
//     console.log("Second Largest Number:",a)
// } else if (d>a>c>b) {
//     console.log("Second Largest Number:",a)
// } else if (d>b>a>c) {
//     console.log("Second Largest Number:",b)
// }else if (d>b>c>a) {
//     console.log("Second Largest Number:",b)
// }else if (d>c>a>b) {
//     console.log("Second Largest Number:",d)
// }else if (d>c>b>a) {
//     console.log("Second Largest Number:",d)
// }

let arr=[]
arr.push(a)
arr.push(b)
arr.push(c)
arr.push(d)
arr.sort((a,b)=>parseInt(a)-parseInt(b))
console.log("Second Largest Number:",arr[2])
