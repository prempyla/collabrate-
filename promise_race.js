Promise.myRace = function (arr) {
  return new Promise((resolve, reject) => {
    if (!arr || typeof arr[Symbol.iterator] !== 'function') {
      throw new TypeError('Promise.myRace requires an iterable input');
    }
    
    for (const promise of arr) {
      Promise.resolve(promise).then(resolve, reject);
    }
  });
}
