Promise.myAll = function (arr) {
    // write your code here
    return new Promise((resolve,reject) => {
      const result = [];
      let completed = 0;
      for (let i = 0; i < arr.length; i++) {
        const promise = arr[i];
        Promise.resolve(promise)
          .then((data) => {
            result[i] = data;
            completed++;
            if (completed === arr.length) {
              resolve(result);
            }
          })
          .catch((err) => reject(err));
      }
    });
  }
