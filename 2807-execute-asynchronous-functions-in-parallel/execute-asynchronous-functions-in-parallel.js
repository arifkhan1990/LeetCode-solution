/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = [];
        let isComplete = 0;

        functions.forEach((func, index) => {
            func().then(
                value => {
                    results[index] = value;
                    isComplete++;
                    if(isComplete === functions.length) {
                        resolve(results);
                    }
                },
                error => {
                    reject(error);
                }
            );
        });
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */